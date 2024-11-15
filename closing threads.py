import threading
import time

# A simple worker function
def worker(stop_event):
    while not stop_event.is_set():
        print("Thread is working...")
        time.sleep(1)
    print("Thread is stopping...")

# Create a list to hold threads and an event for stopping them
threads = []
stop_events = []

# Start multiple threads
for i in range(1000):  # Adjust the range for more threads
    stop_event = threading.Event()
    thread = threading.Thread(target=worker, args=(stop_event,))
    threads.append(thread)
    stop_events.append(stop_event)
    thread.start()

# Allow threads to run for a while
time.sleep(5)

# Signal all threads to stop
for event in stop_events:
    event.set()

# Wait for all threads to finish
for thread in threads:
    thread.join()

print("All threads have been closed.")
