import subprocess
import time
import pyautogui


def restart_vscode_and_run_script():
    print("Starting the restart process...")

    try:
        # Terminate all VS Code processes
        print("Checking for VS Code processes...")
        result = subprocess.run(["pgrep", "-f", "code"], stdout=subprocess.PIPE, text=True)
        pids = result.stdout.strip().split()

        if len(pids) > 0:
            print(f"VS Code processes found: {pids}. Terminating all related processes...")
            subprocess.run(["killall", "code"], check=True)  # Terminate all VS Code processes
            print("All VS Code processes terminated.")
        else:
            print("No VS Code processes were running.")

        # Wait for a short duration
        time.sleep(2)

        # Start VS Code and open the workspace
        print("Starting VS Code...")
        subprocess.run(["code", "/home/achiya/Desktop/Phone_project"], check=True)
        print("VS Code restarted.")

        # Wait for VS Code to initialize
        time.sleep(5)

        # Send command to VS Code terminal
        print("Sending command to VS Code terminal...")
        pyautogui.hotkey('ctrl', '`')  # Open terminal in VS Code
        time.sleep(2)
        pyautogui.typewrite('python /home/achiya/Desktop/Phone_project/run_scripts.py\n')
        print("Command sent to VS Code terminal.")

    except subprocess.CalledProcessError as e:
        print(f"Error during subprocess execution: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

    print("Waiting for 1 hour before next restart...")
    time.sleep(3600)  # Wait for 1 hour before restarting again


# Continuous restart process
while True:
    restart_vscode_and_run_script()
