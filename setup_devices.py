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


def setup_google(d,gmail:str,password,name,date:str,gender):
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
    sleep(2)
    d.click(588,952)
    sleep(5)
    d.click(130,500)
    sleep(1)
    x,y = search_sentence(d,date.split("/")[1],"goo")
    d.click(x,y)
    sleep(5)
    d.click(347,500)
    sleep(1)
    tap_keyboard(d,date.split("/")[0],keyboard_dic_only_nums)
    sleep(1)
    d.click(575,500)
    sleep(1)
    tap_keyboard(d,date.split("/")[2],keyboard_dic_only_nums)
    sleep(1)
    d.click(575,620)
    try:
        x,y = search_sentence(d,gender,"goo")
        d.click(x,y)
    except:
        d.click(323,730) #male is defult
    sleep(3)
    d.click(590,1480)
    sleep(3)
    d.click(360,700)
    sleep(3)
    tap_keyboard(d,gmail.split("@")[0])
    sleep(3)
    d.click(590,950)
    sleep(3)
    tap_keyboard(d,password)
    sleep(3)
    d.click(590,950)


def setup_twitter(d,gmail,password=""):
    d.app_start("com.twitter.android")
    sleep(10)
    d.click(300,500)
    sleep(2)
    d.click(360,1057) # Tap create account with google
    sleep(5)
    x,y = search_sentence(d,gmail,"twi")
    d.click(x,y)
setup_google(u2.connect("127.0.0.1:6555"),"exp53261456@gmail.com","02082003exp","expirimentman","2/August/2003","Male")