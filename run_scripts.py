from time import sleep
import tiktokScript as tik
import twitterScript as twi
import instegramScript as inst
import uiautomator2 as u2
from start_adb import *
from concurrent.futures import ThreadPoolExecutor
from common_area import *
import os
import time

# TODO: nonscrollable countdown

def like_comment_follow(device_id):
    """
    Function to run Twitter and TikTok scripts on a specific phone connected to a custom ADB server port.
    Parameters:
    device_id (str): The IP of the phone.
    """
    while True:
        try:
            print(f"Attempting to connect to device: {device_id}")
            start_time = time.time()
            d = u2.connect(device_id).app_list_running
            
            if d is not None:
                for _ in range(2):
                    print(f"Running Twitter script on device: {device_id}")
                    twi.main(d)
                    time.sleep(5)  # Delay between scripts
                    print(f"Running TikTok script on device: {device_id}")
                    tik.main(d)
                    time.sleep(5)  # Delay between scripts

                print(f"Disconnecting from device: {device_id}")
                os.system(f'adb disconnect {device_id}')
            else:
                print(f"Could not connect to device: {device_id}")
            
            end_time = time.time()
            elapsed_time = end_time - start_time
            print(f"Total time taken to run the program: {elapsed_time:.2f} seconds")

            d.click(360, 1600)  # Go to home

            print(f"{device_id} completed its tasks. Sleeping for 3 hours...")
            time.sleep(3 * 3600)  # 3 hours break for this worker
        except Exception as e:
            print(f"Error while processing {device_id}: {e}")
            time.sleep(60)  # Wait before retrying on error


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
    
    Parameters:
    device_ids (list): List of device IPs.
    """


    start_and_connect_all_servers()
    # Define the maximum number of concurrent threads to limit CPU usage
    max_threads = 12  # Adjust this based on your system’s capabilities
    
    # Use ThreadPoolExecutor to manage thread pool
    with ThreadPoolExecutor(max_threads) as executor:
        # Submit each device to the thread pool
        futures = [executor.submit(like_comment_follow, dev) for dev in device_ips]  # ["10.0.0.6", "10.0.0.15"]   ] 
        
         # Keep the main thread alive while the workers run
        for future in futures:
            try:
                future.result()  # This will block until the worker completes, which is never in this case
            except Exception as e:
                print(f"An error occurred for device {futures[future]}: {e}")



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

