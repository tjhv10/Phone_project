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


def adjust_date_component(d, current_value, target_value, crop_area, x, y, tolerance=2):
    """
    Adjusts a date component (day, month, year) to match the target value.

    Args:
        d: Device object.
        current_value (int): Current value of the date component.
        target_value (int): Target value of the date component.
        crop_area: Area to crop for OCR detection.
        x (int): X-coordinate for swiping.
        y (int): Y-coordinate for swiping.
        tolerance (int): Threshold to determine fast or slow swiping.
    """
    swipe_distance = 100
    while current_value != target_value:
        if current_value > target_value:
            duration = 0.1 if current_value <= target_value + tolerance else 0.005
            d.swipe(rnd_value(x), rnd_value(y), rnd_value(x), rnd_value(y + swipe_distance), duration=duration)
        else:
            duration = 0.1 if current_value >= target_value - tolerance else 0.005
            d.swipe(rnd_value(x), rnd_value(y), rnd_value(x), rnd_value(y - swipe_distance), duration=duration)
        sleep(1)
        if x!=355:
            current_value = int(image_to_string(take_screenshot(d, crop_area=crop_area)))
        else:
            current_value = int(month_dict_month_to_number[image_to_string(take_screenshot(d, crop_area=crop_area))])

    return current_value

def insert_date(d, date: str):
    """
    Adjusts the date (day, month, year) on the device.

    Args:
        d: Device object.
        date (str): Target date in the format "DD/MM/YYYY".
    """
    day, month, year = map(int, date.split('/'))
    # Adjust day
    adjust_date_component(d, int(image_to_string(take_screenshot(d, crop_area=DAY_CROP))), day, DAY_CROP, x=200, y=1340)
    # Adjust month
    adjust_date_component(d, int(month_dict_month_to_number[image_to_string(take_screenshot(d, crop_area=MONTH_CROP))]), month, MONTH_CROP, x=355, y=1340)
    # Adjust year
    adjust_date_component(d, int(image_to_string(take_screenshot(d, crop_area=YEAR_CROP))), year, YEAR_CROP, x=514, y=1340)


def setup_twitter(d,gmail,date,username):
    d.app_start("com.twitter.android")
    sleep(5)
    try:
        x,y = search_sentence(d,gmail,"twi")
        d.click(x,y)
    except:
        d.click(300,500)
        sleep(2)
        d.click(360,1057) # Tap create account with google
        sleep(5)
        try:
            x,y = search_sentence(d,gmail,"twi")
            d.click(x,y)
        except:
            print("Didnt find mail")
            return
    try: 
        x,y = search_sentence(d,"Allow Google to sign you in","twi")
        x,y = search_sentence(d,"Agree","twi")
        d.click(x,y)
    except:
        pass
    sleep(5)
    d.click(632,1481) # Tap Next
    sleep(2)
    d.click(347,532) #Tap date of birth 
    sleep(2)
    insert_date(d,date)
    sleep(1)
    x,y = search_sentence(d,"Sign up","twi")
    d.click(x,y)
    sleep(5)
    d.click(347,460) #Tap usrname chagne
    for _ in range(16):
        d.click(674,1389) # delete
        sleep(0.05)
    tap_keyboard(d,username)
    d.click(639,956) # Tap next
    d.app_stop("com.twitter.android")
    
gmail = "alex.anderson32001@gmail.com"
password = "iZM@KdzU$$SX"
d = u2.connect("127.0.0.1:6562")
# setup_google(d,gmail,password)
# sleep(5)
setup_twitter(d,gmail,"17/9/1998","alexanderson_fit")
# d.swipe(200, 1340, 200, 1340 + 90, duration = 0.005)
# sleep(1)
# d.swipe(207, 1340, 200, 1340 + 90, duration = 0.1)
# sleep(1)
# d.swipe(210, 1340, 200, 1340 + 90, duration = 0.005)
# print(image_to_string(take_screenshot(d, crop_area=MONTH_CROP)))