import glob
import logging
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

# Set up logging
log_file = "logs.log"  # Specify the log file name
logging.basicConfig( 
    level=logging.INFO,  # Log all levels (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    format="%(asctime)s - %(levelname)s - %(message)s",  # Log format
    handlers=[
        logging.FileHandler(log_file, mode='w'),  # Log to a file
        logging.StreamHandler()  # Also print to console
    ]
)

# Replace print statements with logging functions
print = logging.info  # Use logging.info for standard output

def clean_log_files(directory):
    log_files = glob.glob(os.path.join(directory, "*.log"))  # Find all .log files in the directory 
    for log_file in log_files:
        with open(log_file, 'w') as _:
            pass  # Opening in write mode clears the file   

def like_comment_follow(device, max_duration=3600 * 2):
    """
    Function to run Twitter and TikTok scripts on a specific phone.
    """
    device_ip = device.wlan_ip  # Fetch the device's IP address dynamically
    start_time = time.time()
    try:
        logging.info(f"Running tasks on device with IP: {device_ip}")
        close_apps(device)
        sleep(3)
        open_vpn(device)
        logging.info(f"Running Twitter script on device with IP: {device_ip}")
        twi.main(device)
        # close_apps(device)
        # sleep(3)
        # open_vpn(device)
        # sleep(5)
        # tik.main(device)
        # sleep(5)
        # tik.report_account(device,random.choice(tiktok_accounts_to_report))
        # close_apps(device)
        # tik.report_post(device,random.choice(tiktok_posts_to_report)[0])
        # close_apps(device)
        logging.info(f"Device with IP {device_ip} completed its tasks.")
        
        elapsed_time = time.time() - start_time
        logging.info(f"Total time taken for device {device_ip}: {elapsed_time:.2f} seconds")

        if elapsed_time > max_duration:
            logging.info(f"Device with IP {device_ip} exceeded max duration, switching to next device.")
    except Exception as e:
        logging.error(f"Error while processing device with IP {device_ip}: {e}")
        sleep(60)

    logging.info(f"Device with IP {device_ip} is sleeping for 1 hours before restarting tasks...")
    sleep(1 * 3600)
    worker_queue.put(device)


def report_twitter(device_id):
    logging.info(f"Attempting to connect to device: {device_id}")
    d = u2.connect(device_id)
    if d is not None:
        for rep in twitter_posts_to_report:
            twi.report_post(d, rep[0], rep[1])
    else:
        logging.error(f"Could not connect to device: {device_id}")


def report_instagram(device_id):
    logging.info(f"Attempting to connect to device: {device_id}")
    d = u2.connect(device_id)
    if d is not None:
        for rep in instagram_posts_to_report:
            inst.report_post(d, rep[0], rep[1])
    else:
        logging.error(f"Could not connect to device: {device_id}")


def report_tiktok(device_id):
    logging.info(f"Attempting to connect to device: {device_id}")
    d = u2.connect(device_id)
    if d is not None:
        for rep in tiktok_posts_to_report:
            tik.report_post(d, rep[0], rep[1])
    else:
        logging.error(f"Could not connect to device: {device_id}")


def close_apps(device):
    device.app_stop("com.twitter.android")
    device.app_stop("com.zhiliaoapp.musically")
    logging.info(f"{device.wlan_ip} closed apps.")


def main():
    clean_log_files(".")
    global worker_queue
    start_and_connect_all_servers()

    max_threads = 15
    worker_queue = Queue()
    for device in device_ips:
        worker_queue.put(device)

    threads = []
    for i in range(max_threads):
        t = threading.Thread(target=worker_task)
        t.start()
        threads.append(t)

    logging.info("All tasks started!")

    try:
        worker_queue.join()
    except KeyboardInterrupt:
        pass

    for t in threads:
        t.join()

    logging.info("Done with all tasks!")


def main_for_1_phone():
    d1 = u2.connect("10.0.0.11")
    like_comment_follow(d1)


def run_on_multiple_devices():
    start_and_connect_all_servers()
    d = u2.connect("10.0.0.21"), u2.connect("10.0.0.31")

    max_threads = 1
    with ThreadPoolExecutor(max_threads) as executor:
        futures = {executor.submit(twi.report_twitter_posts, dev): dev for dev in d}
        for future in futures:
            try:
                future.result()
            except Exception as e:
                device_ip = futures[future]
                logging.error(f"An error occurred for device {device_ip}: {e}")


stop_event = threading.Event()


def open_vpn(d):
    logging.info(f"{threading.current_thread().name}: {d.wlan_ip} : Opened nordVPN!")
    d.app_start("com.nordvpn.android")
    sleep(10)
    while not search_sentence(d, "Pause Disconnect", "twi"):
        logging.info(f"{threading.current_thread().name}: {d.wlan_ip} : Trying to reconnect...")
        sleep(60)


def worker_task():
    while not stop_event.is_set():
        try:
            device = worker_queue.get(timeout=1)
            if device is None:
                break
            like_comment_follow(device)
            close_apps(device)
            worker_queue.task_done()
            time.sleep(5)
            worker_queue.put(device)
        except Empty:
            time.sleep(1)
        except Exception as e:
            if stop_event.is_set():
                logging.info(f"{threading.current_thread().name}: Stopping due to stop event.")
                break
            else:
                logging.error(f"Error in {threading.current_thread().name}: {e}")
                import traceback
                logging.error(traceback.format_exc())


try:
    main()
except KeyboardInterrupt:
    logging.info("\nMain thread: Stopping all workers.")
    stop_event.set()
