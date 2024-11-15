from time import sleep
import tiktokScript as tik
import twitterScript as twi
import instegramScript as inst
import uiautomator2 as u2
from start_adb import *
from concurrent.futures import ThreadPoolExecutor, as_completed
from common_area import *
from queue import Queue
import os
import time

# TODO: nonscrollable countdown
def like_comment_follow(device, max_duration=3600 * 1.5):  # 1 hour = 3600 seconds
    """
    Function to run Twitter and TikTok scripts on a specific phone.
    Each worker takes a 3-hour break after finishing its task, and the thread is reused by another worker.
    
    Parameters:
    device (uiautomator2.Device): The connected device.
    max_duration (int): Maximum time in seconds to spend on a device before switching.
    """
    start_time = time.time()
    try:
        print(f"Running tasks on device: {device}")
        
        # Run Twitter and TikTok scripts once
        print(f"Running Twitter script on device: {device}")
        twi.main(device)
        time.sleep(5)  # Delay between scripts

        print(f"Running TikTok script on device: {device}")
        tik.main(device)
        time.sleep(5)  # Delay between scripts

        print(f"{device} completed its tasks.")
        
        elapsed_time = time.time() - start_time
        print(f"Total time taken for {device}: {elapsed_time:.2f} seconds")

        if elapsed_time > max_duration:
            print(f"{device} exceeded max duration, switching to next device.")
    except Exception as e:
        print(f"Error while processing {device}: {e}")
        time.sleep(60)  # Wait before retrying on error

    # Independent 3-hour break for this worker
    print(f"{device} is sleeping for 3 hours before restarting tasks...")
    
    # Releasing the worker thread back into the queue while on break
    time.sleep(3 * 3600)  # 3 hours break for the worker
    
    # After break, put this worker back in the queue to be reused
    worker_queue.put(device)  # Put the device back in the queue



def report_twitter(device_id):
    """
    Function to run Twitter and TikTok scripts on a specific phone connected to a custom ADB server port.
    Parameters:
    device_id (str): The IP of the phone.
    """
    print(f"Attempting to connect to device: {device_id}")
    
    # Connect to the device
    d = u2.connect(device_id)
    
    if d is not None:
        for rep in twitter_posts_to_report:
            twi.report_post(d,rep[0],rep[1])
        
    else:
        print(f"Could not connect to device: {device_id}")

        
    # Sleep for 4 hours before the next cycle
    print(f"{device_id} completed its tasks. Sleeping for 4 hours...")
    sleep(4 * 3600)  # 4 hours break for this worker



def report_instagram(device_id):
    """
    Function to run Twitter and TikTok scripts on a specific phone connected to a custom ADB server port.
    Parameters:
    device_id (str): The IP of the phone.
    """
    print(f"Attempting to connect to device: {device_id}")
    
    # Connect to the device
    d = u2.connect(device_id)
    
    if d is not None:
        for rep in instagram_posts_to_report:
            inst.report_post(d,rep[0],rep[1])
    else:
        print(f"Could not connect to device: {device_id}")


def report_tiktok(device_id):
    """
    Function to run Twitter and TikTok scripts on a specific phone connected to a custom ADB server port.
    Parameters:
    device_id (str): The IP of the phone.
    """
    print(f"Attempting to connect to device: {device_id}")
    
    # Connect to the device
    d = u2.connect(device_id)
    
    if d is not None:
        for rep in tiktok_posts_to_report:
            tik.report_post(d,rep[0],rep[1])
    else:
        print(f"Could not connect to device: {device_id}")


def main():
    """
    Function to run the like_comment_follow function concurrently on multiple devices.
    This ensures devices are connected once, and the thread is reused for the next worker.
    """
    global worker_queue
    # Connect all devices before submitting tasks to the thread pool
    devices = start_and_connect_all_servers()  # This will return a list of connected devices (already u2.Device objects)

    # Define the maximum number of concurrent threads to limit CPU usage
    max_threads = 12  # Adjust this based on your system’s capabilities
    
    # Initialize a queue to manage workers
    worker_queue = Queue()

    # Put all the devices into the queue
    for device in devices:
        worker_queue.put(device)

    # Use ThreadPoolExecutor to manage thread pool
    with ThreadPoolExecutor(max_threads) as executor:
        # Function to pick up devices from the queue and assign tasks
        def worker_task():
            while True:
                device = worker_queue.get()  # Get the next available device
                if device is None:
                    break  # Stop when the device queue is empty (not expected in your case)
                like_comment_follow(device)  # Perform tasks on this device
                worker_queue.task_done()  # Mark task as done
        
        # Submit tasks to the thread pool
        futures = [executor.submit(worker_task) for _ in range(max_threads)]
        
        # Wait for all tasks to be done
        for future in as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"An error occurred: {e}")



def run_on_multiple_devices():
    """
    Function to run the like_comment_follow function concurrently on multiple devices.
    
    Parameters:
    device_ids (list): List of device IPs.
    """
    start_and_connect_all_servers()
    d = u2.connect("10.0.0.21"),  u2.connect("10.0.0.31")

    # Define the maximum number of concurrent threads to limit CPU usage
    max_threads = 1  # Adjust this based on your system’s capabilities
    
    # Use ThreadPoolExecutor to manage thread pool
    with ThreadPoolExecutor(max_threads) as executor:
        # Submit each device to the thread pool, and store the Future object with its associated device IP
        futures = {executor.submit(twi.report_twitter_posts, dev): dev for dev in d}
        
        # Keep the main thread alive while the workers run
        for future in futures:
            try:
                # Block until the worker completes, handling any exceptions
                future.result()
            except Exception as e:
                device_ip = futures[future]  # Retrieve the device IP associated with the Future
                print(f"An error occurred for device {device_ip}: {e}")


def main_for_1_phone():
    # Run the program on the specified device
    like_comment_follow("10.0.0.34")


# Uncomment the function you want to run
# run_on_multiple_devices()
main()
# main_for_1_phone()

