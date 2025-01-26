import os
import subprocess

def create_files_and_directories():
    # Paths to create
    files = ["logs.log", "result.txt", "type.py", "range.txt"]
    directories = ["Screenshots"]

    # Create files
    for file in files:
        if not os.path.exists(file):
            with open(file, "w") as f:
                print(f"Created file: {file}")
        else:
            print(f"File already exists: {file}")

    # Create directories
    for directory in directories:
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f"Created directory: {directory}")
        else:
            print(f"Directory already exists: {directory}")

def run_setup_commands():
    # Commands to run
    commands = [
        "sudo apt-get install -y tesseract-ocr python3 python3-venv python3-pip adb",
        "sudo python3 -m venv .venv",
        "source .venv/bin/activate",
        "pip install opencv-python uiautomator2 easyocr numpy pillow selenium pytesseract requests fuzzywuzzy pandas python-Levenshtein openpyxl pyautogui"
        'git config --global user.email "achiyabennatan@gmail.com"',
        'git config --global user.name "tjhv10"'
    ]

    # Run each command
    for command in commands:
        try:
            print(f"Running: {command}")
            subprocess.run(command, shell=True, check=True, executable="/bin/bash")
            print(f"Completed: {command}")
        except subprocess.CalledProcessError as e:
            print(f"Error while running command: {command}\n{e}")

if __name__ == "__main__":
    print("Setting up environment...")
    create_files_and_directories()
    run_setup_commands()
    print("Environment setup complete.")
