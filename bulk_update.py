import os
import re
import subprocess

# Base folder containing Easy, Medium, Hard
BASE_DIR = 'C:/Users/yashi/Documents/geeks-for-geeks'
TARGET_FOLDERS = ['Basic', 'Easy', 'Medium', 'hard']
GFG_SCRIPT = 'C:/Users/yashi/Documents/geeks-for-geeks/gfg_readme_generator.py'

# Logs
success_log = []
failure_log = []

def extract_url_from_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                match = re.match(r'#\s*Problem Statement:\s*(https?://[^\s]+)', line.strip())
                if match:
                    return match.group(1)
    except Exception as e:
        print(f"Failed to read {file_path}: {e}")
    return None

def process_files():
    for folder in TARGET_FOLDERS:
        full_folder_path = os.path.join(BASE_DIR, folder)
        if not os.path.exists(full_folder_path):
            print(f"Skipping missing folder: {full_folder_path}")
            continue

        for root, _, files in os.walk(full_folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                print(f"\n📄 Processing file: {file_path}")
                url = extract_url_from_file(file_path)

                if url:
                    try:
                        result = subprocess.run(
                            ['python', GFG_SCRIPT, url],
                            capture_output=True,
                            text=True
                        )
                        if result.returncode == 0:
                            print("✅ Success:", url)
                            success_log.append((file_path, url))
                        else:
                            print("❌ Script failed:", result.stderr.strip())
                            failure_log.append((file_path, url, result.stderr.strip()))
                    except Exception as e:
                        print("❌ Execution failed:", str(e))
                        failure_log.append((file_path, url, str(e)))
                else:
                    print("⚠️ No problem statement URL found.")
                    failure_log.append((file_path, None, "URL not found"))

def write_summary():
    with open("bulk_generate_success_new.log", "w", encoding='utf-8') as f:
        for path, url in success_log:
            f.write(f"{path} | {url}\n")
    with open("bulk_generate_failures_new.log", "w", encoding='utf-8') as f:
        for path, url, reason in failure_log:
            f.write(f"{path} | {url or 'N/A'} | {reason}\n")
    print(f"\n✅ Summary written to 'bulk_generate_success.log' and 'bulk_generate_failures.log'")

if __name__ == "__main__":
    process_files()
    write_summary()
