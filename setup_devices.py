import uiautomator2 as u2
import logging
from time import sleep
import random
import threading
from common_area import *

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


def setup_google(d,gmail,password,name,date:str):
    d.app_start("com.android.vending")
    sleep(5)
    d.click(300,1090)
    sleep(10)
    d.click(140,900)
    sleep(2)
    d.click(190,1000)
    sleep(5)
    d.click(332,460)
    sleep(3)
    tap_keyboard(d,name)
    sleep(5)
    d.click(588,952)
    sleep(1)
    d.click(search_sentence(d,date.split("/")[1],"goo"))

def setup_twitter(d,gmail,password=""):
    d.app_start("com.twitter.android")
    sleep(10)
    d.click(300,500)
    sleep(2)
    d.click(360,1057) # Tap create account with google
    sleep(5)
    x,y = search_sentence(d,gmail,"twi")
    d.click(x,y)
setup_google(u2.connect("127.0.0.1:6555"),"exp53261456@gmail.com","02082003exp","expirimentman","2/August/2003")