import logging
import traceback
from time import sleep
import tiktokScript as tik
import twitterScript as twi
import instegramScript as inst
import uiautomator2 as u2
from start_adb import *
from concurrent.futures import ThreadPoolExecutor
from common_area_items import *
from queue import Queue
import time
import threading
from queue import Empty
from start_adb import device_ips
from common_area_functions import *


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

  

def like_comment_follow(d):
    """
    Function to run Twitter and TikTok scripts on a specific phone.
    """
    device_ip = d.wlan_ip  # Fetch the device's IP address dynamically
    try:
        logging.info(f"Running tasks on device with IP: {device_ip}")
        close_apps(d)
        sleep(3)
        for _ in range(2):
            if TYPE == 'p':
                open_vpn(d)
            logging.info(f"Running script on device with IP: {device_ip}")
            start_random_function([twi.main,twi.extraFunctions],d)
            close_apps(d)
            sleep(3)
        logging.info(f"Device with IP {device_ip} completed its tasks.")
    except Exception as e:
        logging.error(f"Error while processing device with IP {device_ip}: {e}")
        sleep(60)

    logging.info(f"Device with IP {device_ip} is sleeping for 1 hours before restarting tasks...")
    close_apps(d)
    # if TYPE=='v':
    sleep(0.5 * 3600)
    worker_queue.put(d)


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




def main():
    clean_log_files(".")
    clear_screenshots()
    global worker_queue
    start_and_connect_all_servers()

    max_threads = 15
    worker_queue = Queue()

    random.shuffle(device_ips)  # Shuffle the devices list
    for device in device_ips:
        worker_queue.put(device)

    threads = []
    for _ in range(max_threads):
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
                logging.error(traceback.format_exc())


try:
    main()
except KeyboardInterrupt:
    logging.info("\nMain thread: Stopping all workers.")
    stop_event.set()
