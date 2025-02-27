import logging
from time import sleep
import tiktokScript as tik
import twitterScript as twi
import instegramScript as inst
import uiautomator2 as u2
from start_adb import *
from common_area_items import *
from queue import Queue
import time
import threading
from queue import Empty
from common_area_functions import *

def like_comment_follow(d):
    """
    Function to run Twitter and TikTok scripts on a specific phone.
    """
    try:
        logging.info(f"Running tasks on device with thread: {threading.current_thread().name}:{d.serial}")
        close_apps(d)
        sleep(3)
        if TYPE == 'p':
            open_vpn(d)
        logging.info(f"Running script on device with thread: {threading.current_thread().name}:{d.serial}")
        start_random_function([twi.main,tik.main],d)
        logging.info(f"Device with thread {threading.current_thread().name}:{d.serial} completed its tasks.")
    except Exception as e:
        logging.error(f"Error while processing device with thread {threading.current_thread().name}:{d.serial}: {e}")
        sleep(60)
    logging.info(f"Device with thread {threading.current_thread().name} is sleeping for 1 hours before restarting tasks...")
    logging.info(f"Restarting: {threading.current_thread().name}:{d.serial}")
    if TYPE=='v':
        restart_device(d)
    sleep(0.5 * 3600)
    worker_queue.put(d)


def main():
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

stop_event = threading.Event()


devices_in_use = set()
devices_in_use_lock = threading.Lock()

def worker_task():
    while not stop_event.is_set():
        try:
            device = worker_queue.get(timeout=1)
            if device is None:
                break

            # Ensure device is not already in use
            with devices_in_use_lock:
                if device in devices_in_use:
                    worker_queue.put(device)  # Put it back in the queue
                    continue
                devices_in_use.add(device)

            try:
                # Perform the task
                like_comment_follow(device)
                close_apps(device)
            finally:
                # Mark device as no longer in use
                with devices_in_use_lock:
                    devices_in_use.remove(device)

            worker_queue.task_done()
            time.sleep(5)
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
