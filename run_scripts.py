print("Downloading libraries...")
from time import sleep
import tiktokScript as tik
import twitterScript as twi
import instegramScript as inst
import uiautomator2 as u2
from start_adb import *
from concurrent.futures import ThreadPoolExecutor
from common_area import *
from queue import Queue
import time
import threading
from queue import Empty
from start_adb import device_ips


def like_comment_follow(device, max_duration=3600 * 2):  # 1 hour = 3600 seconds
    """
    Function to run Twitter and TikTok scripts on a specific phone.
    Each worker takes a 3-hour break after finishing its task, and the thread is reused by another worker.
    
    Parameters:
    device (uiautomator2.Device): The connected device instance.
    max_duration (int): Maximum time in seconds to spend on a device before switching.
    """
    device_ip = device.wlan_ip  # Fetch the device's IP address dynamically
    start_time = time.time()
    try:
        print(f"Running tasks on device with IP: {device_ip}")
        close_apps(device)
        sleep(3)
        open_vpn(device)
        print(f"Running Twitter script on device with IP: {device_ip}")
        twi.main(device)  # Assuming twi.main is the function for running the Twitter script
        sleep(5)  # Delay between scripts
        # open_vpn(device)
        # print(f"Running TikTok script on device with IP: {device_ip}")
        # tik.main(device)  # Assuming tik.main is the function for running the TikTok script hereeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee!!!!!!!!!!!!!!!!!!!!!!!!!!
        # sleep(5)  # Delay between scripts
        print(f"Device with IP {device_ip} completed its tasks.")
        
        elapsed_time = time.time() - start_time
        print(f"Total time taken for device {device_ip}: {elapsed_time:.2f} seconds")

        if elapsed_time > max_duration:
            print(f"Device with IP {device_ip} exceeded max duration, switching to next device.")
    except Exception as e:
        print(f"Error while processing device with IP {device_ip}: {e}")
        time.sleep(60)  # Wait before retrying on error

    # Independent 3-hour break for this worker
    print(f"Device with IP {device_ip} is sleeping for 0.5 hours before restarting tasks...")
    
    # Releasing the worker thread back into the pool while on break
    time.sleep(1 * 3600)  # 0.5 hours break for the worker
    
    # After break, return the device to the pool to be reused
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


def close_apps(device): 
    device.app_stop("com.twitter.android")     
    device.app_stop("com.zhiliaoapp.musically")
    print(device.wlan_ip + " closed apps.")

def main():
    """
    Function to run the like_comment_follow function concurrently on multiple devices.
    This ensures devices are connected once, and the thread is reused for the next worker.
    """
    global worker_queue
    start_and_connect_all_servers()

    # Define the maximum number of concurrent threads to limit CPU usage
    max_threads = 15  # Adjust this based on your system’s capabilities
    
    # Initialize a queue to manage workers
    worker_queue = Queue()

    # Put all the devices into the queue
    for device in device_ips:
        worker_queue.put(device)

    # Create and start worker threads manually
    threads = []
    for i in range(max_threads):
        t = threading.Thread(target=worker_task)
        t.start()
        threads.append(t)

    print("All tasks started!")

    try:
        # Wait for all tasks to be done (even after stopping)
        worker_queue.join()  # This will block until all tasks are finished
    except KeyboardInterrupt:
        # This will now be handled by the signal handler
        pass
    
    # Wait for threads to exit gracefully
    for t in threads:
        t.join()  # Ensure each thread finishes before proceeding

    print("Done with all tasks!")


def main_for_1_phone():
    # Run the program on the specified device
    d1 = u2.connect("10.0.0.11")
    # d2 = u2.connect("10.0.0.32")    
    # open_vpn(d1)
    # open_vpn(d2)
    # print(d.app_list_running())
    like_comment_follow(d1)


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


# Event to signal threads to stop
stop_event = threading.Event()

def open_vpn(d):
    print(f"{threading.current_thread().name}: {d.wlan_ip} : Opened nordVPN!") 
    d.app_start("com.nordvpn.android")
    sleep(10)
    while search_sentence(d, "Disconnect","twi"):
        print(f"{threading.current_thread().name}: {d.wlan_ip} : Trying to reconnect...") 
        sleep(120)  # 2 minute of delay after opening the VPN


def worker_task():
    while not stop_event.is_set():  # Check if the stop event is set
        try:
            # Get the next available device with a timeout of 1 second
            device = worker_queue.get(timeout=1)
            if device is None:
                break  # Stop if there are no devices to process
            
            # Perform tasks on this device
            like_comment_follow(device)
            close_apps(device)
            # for i in range(5):
            #     device.app_start("com.twitter.android")
            #     sleep(5)
            #     device.app_stop("com.twitter.android")


            worker_queue.task_done()  # Mark task as done
            time.sleep(5)  # Optional: Add a sleep delay between tasks
            worker_queue.put(device)  # Re-add the device to the queue for the worker to process again
        except Empty:
            # print(f"{threading.current_thread().name}: No devices in the queue. Waiting for tasks...")
            time.sleep(1)  # Optional: Prevent tight loop in case of repeated queue emptiness
        except Exception as e:
            if stop_event.is_set():
                print(f"{threading.current_thread().name}: Stopping due to stop event.")
                break  # Exit the loop when the stop event is set
            else:
                print(f"Error in {threading.current_thread().name}: {e}")
                print("Traceback details:")
                import traceback
                traceback.print_exc()  # Print the full traceback



try:
    # Uncomment the function you want to run
    # run_on_multiple_devices()
    # main_for_1_phone()
    main()    
    # test()
except KeyboardInterrupt:
    print("\nMain thread: Stopping all workers.")
    stop_event.set()
