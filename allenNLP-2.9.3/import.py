import subprocess
import os

def scan_file_with_bandit(file_path):
    # Run Bandit on the specified file and capture the output
    result = subprocess.run(['bandit', '-f', 'text', file_path], capture_output=True, text=True)
    if result.stdout:
        print(f"Results for {file_path}:")
        print(result.stdout)
    else:
        print(f"No issues found in {file_path}.")

def main(folder_path):
    # Check if the folder exists
    if not os.path.exists(folder_path):
        print(f"The folder {folder_path} does not exist.")
        return

    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            if file_name.endswith('.py'):  # Change file extension to '.py' to scan Python files
                full_path = os.path.join(root, file_name)
                scan_file_with_bandit(full_path)

if __name__ == "__main__":
    folder_path = 'Expert_final'  # Adjust this to the path of your folder
    main(folder_path)
