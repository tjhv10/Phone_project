import logging
import os
import subprocess
import uiautomator2 as u2
from time import sleep

# Configure logging
logging.basicConfig(
    level=logging.INFO,  # Log all messages of level DEBUG and above
    format="%(asctime)s - %(levelname)s - %(message)s",  # Include timestamp, level, and message
    handlers=[
        # logging.FileHandler(log_file, mode='w'),  # Write logs to a file
        logging.StreamHandler()  # Also print logs to the console
    ]
)

# Replace all `print` statements with `logging.info` or appropriate log levels
print = logging.info  # Redirect print to info-level logging 

def get_connected_devices():
    """
    Get a list of connected devices as uiautomator2.Device objects.
    """
    with open("logs.log", 'w') as _:
            pass  # Opening in write mode clears the file  
    try:
        print("Getting all connected devices...")
        result = subprocess.run(["adb", "devices"], capture_output=True, text=True)
        devices = []
        
        # Parse the output, skipping the first line as it's just a header
        for line in result.stdout.splitlines()[1:]:
            if "device" in line and not line.startswith("List of devices attached"):
                device_id = line.split()[0]
                # Connect to the device using uiautomator2 and append the device object to the list
                logging.info(f"Trying to connect to: {device_id}")
                device = u2.connect(device_id)
                logging.info(f"Connected to: {device_id}")
                devices.append(device)
                
        return devices if devices else []  # Return an empty list if no devices found
    except Exception as e:
        print(f"Error getting connected devices: {e}")
        return []  # Return an empty list in case of error
    

def get_connected_devices_ip():
    """
    Returns a list of connected device serial numbers along with their IP and port.
    """
    try:
        # Run 'adb devices -l' command to get the list of connected devices with more details
        result = subprocess.run(["adb", "devices", "-l"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        # Split the output and ignore the first line (which is the header)
        devices = result.stdout.decode().splitlines()[1:]
        
        # Parse each device info line
        device_info = []
        for device in devices:
            if device:
                device_id = device.split()[0]
                details = device.split()[1:]
                ip = None
                port = None
                
                # Look for the IP and port in the details
                for detail in details:
                    if "device" in detail:
                        continue  # Ignore the 'device' status
                
                device_info.append(device_id)
        
        return device_info

    except subprocess.CalledProcessError as e:
        print(f"Error listing connected devices: {e}")
        return []

# List of device IPs to connect to (you need to populate this list with actual IPs)
device_ips = get_connected_devices()
START_PORT = 5001
NUM_SERVERS = len(device_ips)

def start_adb_server(port):
    """
    Start an ADB server on a specified port.
    """
    # Set the environment variable for the ADB server port
    os.environ["ADB_SERVER_PORT"] = str(port)

    # Start the ADB server on the specified port
    subprocess.run(["adb", "start-server"], check=True)

    print(f"ADB server started on port {port}")

def connect_device(port, device):
    """
    Connect to a device using the specified ADB server port and uiautomator2.
    """
    # Run the adb connect command using the custom port
    result = subprocess.run(["adb", "-P", str(port), "connect", device.serial], stdout=subprocess.PIPE)

    # Check the result for success
    if "connected" in result.stdout.decode('utf-8'):
        print(f"Successfully connected to {device.serial} on port {port}")
    else:
        print(f"Failed to connect to {device.serial} on port {port}")

def start_and_connect_all_servers():
    """
    Start ADB servers on unique ports and connect to the corresponding devices.
    """

    if NUM_SERVERS == 0:
        print("No devices connected. Exiting.")
        return  # Exit if no devices are connected

    for i in range(1):
        # Calculate the port number (increment from the starting port)
        port = START_PORT + i
        
        # Start the ADB server on this port
        start_adb_server(port)
        
        # Wait briefly before connecting to the device
        sleep(1)
        
        # Connect the device with the current ADB server port
        connect_device(port, device_ips[i])
        
        # Wait briefly to avoid overwhelming the system
        sleep(1)

