import os
import re
import json
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from git import Repo
import sys

def slugify(title):
    # Allow - and + in the folder name, replace other non-alphanum with _
    return re.sub(r'[^a-z0-9\-\+]+', '_', title.lower().strip()).strip('_')

def decode_entities(text):
    try:
        text = text.encode('utf-8').decode('unicode_escape')
        text = text.replace('<', '<').replace('>', '>').replace('\u003c', '<').replace('\u003e', '>')
        return text
    except Exception:
        return text

def get_problem_data(url):
    # Set up headless browser
    options = Options()
    options.add_argument('--headless')  # Remove if you want to see the browser
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(url)

    # Wait for JS to load
    time.sleep(5)

    html = driver.page_source
    driver.quit()

    soup = BeautifulSoup(html, 'html.parser')

    # Try extracting from JSON first
    script_tag = soup.find('script', id='__NEXT_DATA__')
    prob_data = None
    if script_tag:
        try:
            data_str = script_tag.string
            data = json.loads(data_str)
            prob_data = data.get('props', {}).get('pageProps', {}).get('allData', {}).get('probData', {})
        except Exception as e:
            print("Error parsing JSON:", e)

    # 1. Get Title
    title = "Problem"
    # Try to get the title from the main h3 tag (with both classes)
    title_tag = soup.select_one('div.problems_header_content__title__L2cB2.g-mb-0 h3')
    if not title_tag:
        # fallback to just h3 with class
        title_tag = soup.select_one('h3.problems_header_content__title__L2cB2')
    if title_tag:
        title = title_tag.get_text(strip=True)
    elif prob_data:
        title = prob_data.get('problem_name', title)

    # 2. Header Info
    difficulty = accuracy = submissions = points = average_time = "N/A"
    desc_div = soup.select_one('div.problems_header_description__t_8PB')
    if desc_div:
        spans = [span.get_text(strip=True) for span in desc_div.find_all('span')]
        for s in spans:
            if 'Accuracy' in s:
                accuracy = s.split(":")[-1].strip()
            elif 'Submissions' in s:
                submissions = s.split(":")[-1].strip()
            elif 'Difficulty' in s or 'Level' in s:
                difficulty = s.split(":")[-1].strip()
            elif 'Points' in s:
                points = s.split(":")[-1].strip()
            elif 'Average Time' in s:
                average_time = s.split(":")[-1].strip()

    # 3. Problem Description (keep HTML for formatting)
    description_html = ""
    if prob_data:
        description_html = decode_entities(prob_data.get('problem_question', ''))
    else:
        content_div = soup.select_one('div.problems_problem_content__Xm_eO')
        if content_div:
            # Keep inner HTML for formatting
            description_html = ''.join(str(child) for child in content_div.children)

    # 4. Expected Complexities, Topic Tags, Related Articles
    expected_complexities = ""
    topic_tags = []
    company_tags = []
    related_interview_experiences = []
    related_articles = []

    # Check for expected complexities
    complexities_container = soup.select_one('div.problems_expected_complexities_text__h_eyi')
    if complexities_container:
        lines = [div.get_text(strip=True) for div in complexities_container.select('div.problems_normal_text__QiKrb')]
        if lines:
            expected_complexities = '\n'.join(f"- {line}" for line in lines)

    # Check for Topic Tags, Related Articles
    tags_container = soup.select_one('div.problems_accordion_tags_container__zk2Um')
    if tags_container:
        tag_boxes = tags_container.select('div.problems_accordion_tags__JJ2DX')
        for box in tag_boxes:
            header_div = box.select_one('div.problems_tag_container__kWANg > strong')
            if not header_div:
                continue
            tag_type = header_div.get_text(strip=True)

            content_div = box.select_one('div.ui.labels')
            if not content_div:
                continue
            a_tags = content_div.select('a')

            if "Topic Tags" in tag_type:
                topic_tags = [a.get_text(strip=True) for a in a_tags]
            elif "Company Tags" in tag_type:
                company_tags = [a.get_text(strip=True) for a in a_tags]
            elif "Related Interview Experiences" in tag_type:
                related_interview_experiences += [f"[{a.get_text(strip=True)}]({a.get('href')})" for a in a_tags]
            elif "Related Articles" in tag_type:
                related_articles += [f"[{a.get_text(strip=True)}]({a.get('href')})" for a in a_tags]


    # Build badge URLs
    badge_base = "https://custom-icon-badges.demolab.com/badge/"
    badge_mid = "-1F222E?style=for-the-badge&logoColor=white&logo="
    badge_difficulty = f'{badge_base}Difficulty: {difficulty}{badge_mid}fire'
    badge_accuracy = f'{badge_base}Accuracy: {accuracy}25{badge_mid}target'
    badge_submissions = f'{badge_base}Submissions: {submissions}{badge_mid}repo'
    badge_points = f'{badge_base}Points: {points}{badge_mid}award'
    badge_average_time = f'{badge_base}Average%20Time: {average_time}{badge_mid}clock'

    readme = f'<h1 align="center">{title}</h1>\n\n'
    readme += '<p align="center">\n'
    readme += f'  <img alt="Difficulty" title="Difficulty" src="{badge_difficulty}"/>\n'
    readme += f'  <img alt="Accuracy" title="Accuracy" src="{badge_accuracy}"/>\n'
    readme += f'  <img alt="Submissions" title="Submissions" src="{badge_submissions}"/>\n'
    readme += f'  <img alt="Points" title="Points" src="{badge_points}"/>\n'
    readme += f'  <img alt="Average Time" title="Average Time" src="{badge_average_time}"/>\n'
    readme += '</p>\n\n'

    readme += "## Problem Statement\n\n"
    if description_html:
        # Convert HTML to markdown-like, but keep formatting (bold, underline, code, etc.)
        desc_soup = BeautifulSoup(description_html, 'html.parser')
        def html_to_md(el, in_pre=False):
            # Helper to render formatting as HTML inside <pre>, Markdown outside
            def render_bold(children):
                content = ''.join([html_to_md(child, in_pre) for child in children])
                return f"<b>{content}</b>"
            def render_italic(children):
                content = ''.join([html_to_md(child, in_pre) for child in children])
                return f"<i>{content}</i>"
            def render_underline(children):
                content = ''.join([html_to_md(child, in_pre) for child in children])
                return f"<u>{content}</u>"
            def render_sup(children):
                content = ''.join([html_to_md(child, in_pre) for child in children])
                return f"<sup>{content}</sup>"
            def render_sub(children):
                content = ''.join([html_to_md(child, in_pre) for child in children])
                return f"<sub>{content}</sub>"
            if el.name == 'pre':
                content = ''.join([html_to_md(child, True) for child in el.children])
                return f"<pre>{content}</pre>\n"
            elif el.name == 'img':
                src = el.get('src', '')
                alt = el.get('alt', '')
                title = el.get('title', '')
                width = el.get('width')
                height = el.get('height')
                width_attr = f' width="{width}"' if width else ''
                height_attr = f' height="{height}"' if height else ''
                # Render as HTML img tag with width and height if present
                return f'<img src="{src}" alt="{alt}" title="{title}"{width_attr}{height_attr}/>'
            elif el.name in ['b', 'strong']:
                return render_bold(el.children)
            elif el.name == 'u':
                return render_underline(el.children)
            elif el.name in ['i', 'em']:
                return render_italic(el.children)
            elif el.name == 'sup':
                return render_sup(el.children)
            elif el.name == 'sub':
                return render_sub(el.children)
            elif el.name == 'ul':
                return '\n'.join([f"- {html_to_md(li, in_pre)}" for li in el.find_all('li', recursive=False)])
            elif el.name == 'ol':
                return '\n'.join([f"1. {html_to_md(li, in_pre)}" for li in el.find_all('li', recursive=False)])
            elif el.name == 'li':
                return ''.join([html_to_md(child, in_pre) for child in el.children])
            elif el.name == 'br':
                return '<br>'
            elif el.name == 'hr':
                return '<hr>'
            elif el.name and el.name.startswith('h') and len(el.name) == 2 and el.name[1].isdigit():
                level = int(el.name[1])
                content = ''.join([html_to_md(child, in_pre) for child in el.children])
                return f"{'#' * level} {content}" if not in_pre else f"<b>{content}</b>"
            elif el.name == 'a':
                content = ''.join([html_to_md(child, in_pre) for child in el.children])
                return f"<a href=\"{el.get('href')}\">{content}</a>" if in_pre else f"[{content}]({el.get('href')})"
            elif el.name == 'span':
                return ''.join([html_to_md(child, in_pre) for child in el.children])
            elif el.name == 'p':
                return ''.join([html_to_md(child, in_pre) for child in el.children]) + '\n'
            elif el.name is None:
                return str(el)
            else:
                return ''.join([html_to_md(child, in_pre) for child in el.children])
        # Join all top-level elements
        description = ''.join([html_to_md(child) for child in desc_soup.children]).strip()
        readme += description + "\n\n"
    else:
        readme += "Could not extract problem description.\n\n"

    if expected_complexities:
        readme += "## Expected Complexities\n" + expected_complexities + "\n"

    readme += "\n<hr>\n\n### Tags\n"
    readme += "- **Topic Tags:** {}\n".format(' '.join(f'`{tag}`' for tag in topic_tags) if topic_tags else "`None`")
    readme += "- **Company Tags:** {}\n".format(' '.join(f'`{tag}`' for tag in company_tags) if company_tags else "`None`")

    if related_articles:
        readme += "\n### Related Articles\n"
        for art in related_articles:
            readme += f"- {art}\n"
    if related_interview_experiences:
        readme += "\n### Related Interview Experiences\n"
        for exp in related_interview_experiences:
            readme += f"- {exp}\n"

    return title, readme, difficulty

def create_files(folder_name, title, problem_text):
    os.makedirs(folder_name, exist_ok=True)

    readme_path = os.path.join(folder_name, 'problem_statement.md')
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(problem_text)

    solution_path = os.path.join(folder_name, 'solution.py')
    open(solution_path, 'a').close()

    print(f"Created folder: {folder_name}")

def git_commit_and_push(folder_name, problem_title):
    try:
        repo = Repo('.')
        repo.index.add([folder_name])
        commit_msg = f"Added Problem Statement for '{problem_title}'"
        repo.index.commit(commit_msg)
        origin = repo.remote(name='origin')
        origin.push()
        print("Changes committed and pushed.")
    except Exception as e:
        print("Git operation failed:", str(e))

def main(url):
    print(f"Fetching data from {url}")
    try:
        title, problem_text, difficulty = get_problem_data(url)
        title_slug = slugify(title)
        difficulty_folder = slugify(difficulty) or "unspecified"
        folder_name = os.path.join(difficulty_folder, title_slug)
        create_files(folder_name, title, problem_text)
        git_commit_and_push(folder_name, title)
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python gfg_readme_generator.py <geeksforgeeks_url>")
    else:
        main(sys.argv[1])