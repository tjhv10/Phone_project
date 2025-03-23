import os
import subprocess

def create_files_and_directories():
    # Paths to create
    files = ["logs.log", "result.txt", "env.py"]
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

def write_default_env_file():
    with open("env.py", "w") as env_file:
        env_file.write("import sys\n")
        env_file.write("TYPE = 'v'\n")
        env_file.write('gmtoolPath = "/home/goldfish/Desktop/genymotion/gmtool"\n')
        env_file.write('phoneRange = ""\n')
        env_file.write("""

# Define the dictionary with 'buttom' and 'top'
config = {
    'buttom': x,
    'top': y 
}

# Ensure that there is exactly one argument
if len(sys.argv) != 2:
    print("Usage: python3 env.py <buttom|top>")
    sys.exit(1)

# Get the argument passed to the script
arg = sys.argv[1]

# Check if the argument is valid and print the corresponding value
if arg in config:
    print(config[arg])
else:
    print(f"Error: '{arg}' is not a valid argument.")
    sys.exit(1)
        """)
    print("Default content written to env.py")

def write_initial_result_file():
    content = """
Likes - 0
Comments - 0
Follows - 0
Reposts - 0
Posts reported - 0
Accounts reported - 0
Actions - 0
    """
    with open("result.txt", "w") as f:
        f.write(content.strip())
    print("Content written to result.txt")


def run_setup_commands():
    # Commands to run
    commands = [
        "sudo apt-get install -y tesseract-ocr python3 python3-venv python3-pip adb",
        "sudo python3 -m venv .venv",
        "source .venv/bin/activate",
        "pip install opencv-python uiautomator2 easyocr numpy pillow selenium pytesseract requests fuzzywuzzy pandas python-Levenshtein openpyxl pyautogui",
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
    write_default_env_file()
    print("Environment setup complete.")
