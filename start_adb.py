import os
import subprocess
import uiautomator2 as u2
from time import sleep

def get_connected_devices():
    """
    Get a list of connected devices as uiautomator2.Device objects.
    """
    try:
        print("Getting all connected devices...")
        result = subprocess.run(["adb", "devices"], capture_output=True, text=True)
        devices = []
        
        # Parse the output, skipping the first line as it's just a header
        for line in result.stdout.splitlines()[1:]:
            if "device" in line and not line.startswith("List of devices attached"):
                device_id = line.split()[0]
                # Connect to the device using uiautomator2 and append the device object to the list
                device = u2.connect(device_id)
                devices.append(device)
                
        return devices if devices else []  # Return an empty list if no devices found
    except Exception as e:
        print(f"Error getting connected devices: {e}")
        return []  # Return an empty list in case of error

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

