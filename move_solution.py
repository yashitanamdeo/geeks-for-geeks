import os

BASE_DIR = 'C:/Users/yashi/Documents/geeks-for-geeks'
TARGET_FOLDERS = ['Easy', 'Medium', 'Hard', 'Basic']

success_log = []
failure_log = []

def move_content_and_delete(src_path, dest_path):
    try:
        with open(src_path, 'r', encoding='utf-8') as src_file:
            content = src_file.read()
        
        with open(dest_path, 'w', encoding='utf-8') as dest_file:
            dest_file.write(content)

        os.remove(src_path)  # Delete original after writing
        success_log.append((src_path, dest_path))
        print(f"✅ Moved & deleted: {src_path} → {dest_path}")
    except Exception as e:
        failure_log.append((src_path, dest_path, str(e)))
        print(f"❌ Error with {src_path} → {dest_path}: {e}")

def process_files():
    for folder in TARGET_FOLDERS:
        folder_path = os.path.join(BASE_DIR, folder)
        if not os.path.exists(folder_path):
            print(f"⚠️ Folder missing: {folder_path}")
            continue

        for item in os.listdir(folder_path):
            file_path = os.path.join(folder_path, item)

            if os.path.isfile(file_path) and item.endswith('.py'):
                problem_name = os.path.splitext(item)[0]
                target_folder = os.path.join(folder_path, problem_name)
                solution_file_path = os.path.join(target_folder, 'solution.py')

                if os.path.isdir(target_folder) and os.path.exists(solution_file_path):
                    move_content_and_delete(file_path, solution_file_path)
                else:
                    reason = "Folder or solution.py not found"
                    failure_log.append((file_path, solution_file_path, reason))
                    print(f"⚠️ Skipping {file_path}: {reason}")

def write_summary():
    with open("code_move_success_new.log", "w", encoding='utf-8') as f:
        for src, dest in success_log:
            f.write(f"{src} → {dest}\n")

    with open("code_move_failures_new.log", "w", encoding='utf-8') as f:
        for src, dest, reason in failure_log:
            f.write(f"{src} → {dest} | {reason}\n")

    print("\n📄 Summary written to 'code_move_success.log' and 'code_move_failures.log'")

if __name__ == "__main__":
    process_files()
    write_summary()
