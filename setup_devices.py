import uiautomator2 as u2
import logging
from time import sleep
from common_area_items import *
from common_area_functions import *


# Configure logging
log_file = "logs.log"  # Log file to capture output
logging.basicConfig(
    level=logging.INFO,  # Log all messages of level DEBUG and above
    format="%(asctime)s - %(levelname)s - %(message)s",  # Include timestamp, level, and message
    handlers=[
        logging.FileHandler(log_file, mode='w'),  # Write logs to a file
        logging.StreamHandler()  # Also print logs to the console
    ]
)

# Replace all `print` statements with `logging.info` or appropriate log levels
print = logging.info  # Redirect print to info-level logging


def setup_google(d,gmail:str,password):
    d.app_stop("com.android.vending")
    sleep(2)
    d.app_start("com.android.vending")
    sleep(5)
    d.click(300,1090) #sign in button
    sleep(10)
    d.click(300,630) #insert email press 
    sleep(3)
    tap_keyboard(d,gmail.split("@")[0])
    sleep(1)
    d.click(592,1030) #press next
    sleep(7)
    d.click(300,570) #insert password press 
    tap_keyboard(d,password)
    sleep(1)
    d.click(592,1030) #press next
    sleep(5)
    x,y = search_sentence(d,"Tagree","goo")
    d.click(x,y)
    sleep(20)
    d.app_stop("com.android.vending")
    sleep(2)
    
def setup_twitter(d,gmail,password=""):
    d.app_start("com.twitter.android")
    sleep(10)
    try:
        x,y = search_sentence(d,gmail,"twi")
        d.click(x,y)
    except:
        d.click(300,500)
        sleep(2)
        d.click(360,1057) # Tap create account with google
        sleep(5)
        x,y = search_sentence(d,gmail,"twi")
        d.click(x,y)
    d.click(632,1481) # Tap Next
    sleep(2)
    d.click(347,532) #Tap date of birth 
d = u2.connect("127.0.0.1:6555")
# setup_twitter(d,"alex.thomas126001@gmail.com","17/Sep/1998")
d.swipe(200, 1340, 200, 1340 + 90, duration = 0.005)
sleep(1)
d.swipe(207, 1340, 200, 1340 + 90, duration = 0.1)
sleep(1)
d.swipe(210, 1340, 200, 1340 + 90, duration = 0.005)