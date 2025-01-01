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




def insert_date(d, date: str):
    """
    Adjusts the date (day, month, year) on the device.

    Args:
        d: Device object.
        date (str): Target date in the format "DD/MM/YYYY".
    """
    def adjust_date_component(d, current_value, target_value, crop_area, x, tolerance=2,swipe_distance = 100,y = 1340):
        """
        Adjusts a date component (day, month, year) to match the target value.

        Args:
            d: Device object.
            current_value (int): Current value of the date component.
            target_value (int): Target value of the date component.
            crop_area: Area to crop for OCR detection.
            x (int): X-coordinate for swiping.
            y (int): Y-coordinate for swiping.
            swipe_distance (int): Threshold to determine fast or slow swiping.
        """
        print(current_value)
        while current_value != target_value:
            if current_value > target_value:
                duration = 0.1 if current_value < target_value + tolerance else 0.005
                d.swipe(rnd_value(x), rnd_value(y)+5, rnd_value(x), rnd_value(y + swipe_distance), duration=duration)
            else:
                duration = 0.1 if current_value > target_value - tolerance else 0.005
                d.swipe(rnd_value(x), rnd_value(y)-5, rnd_value(x), rnd_value(y - swipe_distance), duration=duration)
            sleep(1)
            if x!=355 and x!=160:
                current_value = int(image_to_string(take_screenshot(d, crop_area=crop_area)))
            else:
                current_value = int(month_dict_month_to_number[image_to_string(take_screenshot(d, crop_area=crop_area),number=False).lower()])

        return current_value
    def adjust_date_component_with_list(d, current_values, target_value, crop_area, x, swipe_distance=100):
        """
        Adjusts a date component (day, month, year) to match a target value by comparing with a list of current values.

        Args:
            d: Device object.
            current_values (list): List of current values for the date component.
            target_value (int): The target value to match.
            crop_area: Area to crop for OCR detection.
            x (int): X-coordinate for swiping.
            y (int): Y-coordinate for swiping.
            tolerance (int): Acceptable range for close values (default is 2).
            swipe_distance (int): Threshold to determine fast or slow swiping (default is 100).

        Returns:
            int: The matched target value or -1 if not matched.
        """
        if not current_values:
            raise ValueError("Current values list cannot be empty.")        

        while target_value not in current_values:
            min_value = min(current_values)
            max_value = max(current_values)
            if (target_value > max_value and crop_area == YEAR_CROP_INST ) or (target_value < min_value and (crop_area == DAY_CROP_INST or crop_area == MONTH_CROP_INST)):
                # Swipe down if target is smaller than all current values
                d.swipe(rnd_value(x), rnd_value(y), rnd_value(x), rnd_value(y + swipe_distance), duration=0.02)
            elif (target_value > max_value and (crop_area == DAY_CROP_INST or crop_area == MONTH_CROP_INST)) or (target_value < min_value and crop_area == YEAR_CROP_INST):
                # Swipe up if target is larger than all current values
                d.swipe(rnd_value(x), rnd_value(y), rnd_value(x), rnd_value(y - swipe_distance), duration=0.02)
            else:
                # Swipe to adjust towards the closest current value
                closest_value = min(current_values, key=lambda v: abs(v - target_value))
                if target_value < closest_value:
                    d.swipe(rnd_value(x), rnd_value(y), rnd_value(x), rnd_value(y - swipe_distance), duration=0.1)
                else:
                    d.swipe(rnd_value(x), rnd_value(y), rnd_value(x), rnd_value(y + swipe_distance), duration=0.1)

            sleep(1)

            # Update current_values
            if x != 355:
                current_values = convert_strings_to_ints(strip_newlines_and_spaces(image_to_string(take_screenshot(d, crop_area=crop_area))).split("/"))
                
            else:
                current_values = transform_list(strip_newlines_and_spaces(image_to_string(take_screenshot(d, crop_area=crop_area))).split("/"),month_dict_month_to_number)
            sleep(1)
                

        return target_value


    

    day, month, year = map(int, date.split('/'))
    if d.app_current()["package"] == "com.instagram.lite": 
        # Adjust day
        adjust_date_component_with_list(d, convert_strings_to_ints(strip_newlines_and_spaces(image_to_string(take_screenshot(d, crop_area=DAY_CROP_INST))).split("/")), day, DAY_CROP_INST, x=150)
        sleep(2)
        x,y = search_sentence(d,str(format_with_leading_zero(day)),"inst")
        d.click(x,y)
        sleep(1)
        # Adjust month
        adjust_date_component_with_list(d, transform_list(strip_newlines_and_spaces(image_to_string(take_screenshot(d, crop_area=MONTH_CROP_INST),number=False)).split("/"),month_dict_month_to_number), month, MONTH_CROP_INST, x=355)
        x,y = search_sentence(d,month_dict_number_to_month[str(month)],"inst")
        d.click(x,y)
        sleep(1)
        # Adjust year
        adjust_date_component_with_list(d, convert_strings_to_ints(strip_newlines_and_spaces(image_to_string(take_screenshot(d, crop_area=YEAR_CROP_INST))).split("/")), year, YEAR_CROP_INST, x=600)
        sleep(2)
        x,y = search_sentence(d,str(year),"inst")
        d.click(x,y)
    elif d.app_current()["package"] == "com.twitter.android":
        # Adjust day
        adjust_date_component(d, int(image_to_string(take_screenshot(d, crop_area=DAY_CROP_TWI))), day, DAY_CROP_TWI, x=200)
        # Adjust month
        adjust_date_component(d, int(month_dict_month_to_number[image_to_string(take_screenshot(d, crop_area=MONTH_CROP_TWI),number=False).lower()]), month, MONTH_CROP_TWI, x=355)
        # Adjust year
        adjust_date_component(d, int(image_to_string(take_screenshot(d, crop_area=YEAR_CROP_TWI))), year, YEAR_CROP_TWI, x=514)
    elif d.app_current()["package"] == "com.zhiliaoapp.musically":
        y = 1167
        # Adjust day
        adjust_date_component(d, int(image_to_string(take_screenshot(d, crop_area=DAY_CROP_TIK))), day, DAY_CROP_TIK, x=350,y = y)
        # Adjust month
        adjust_date_component(d, int(month_dict_month_to_number[image_to_string(take_screenshot(d, crop_area=MONTH_CROP_TIK),number=False).lower()]), month, MONTH_CROP_TIK, x=160,y = y)
        # Adjust year
        adjust_date_component(d, int(image_to_string(take_screenshot(d, crop_area=YEAR_CROP_TIK))), year, YEAR_CROP_TIK, x=550,y = y)


def setup_tiktok(d,gmail,date):
    d.app_start("com.zhiliaoapp.musically")
    sleep(10)
    d.click(314,199) # go to sign up google
    sleep(1)
    d.click(314,669) #sign up google
    sleep(1)
    try:
        x,y = search_sentence(d,gmail,"twi")
        d.click(x,y)
    except:
        print("Didnt find mail")
        return
    insert_date(d,date)
    sleep(2)
    d.click(356,584) # next
    sleep(5)
    x,y = search_sentence(d,"Continue","twi",30)
    d.click(x,y)
    sleep(10)
    d.app_stop("com.zhiliaoapp.musically")


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
    sleep(5)
    d.app_stop("com.twitter.android")


def setup_instagram(d,gmail,full_name,password,date,username):
    d.app_start("com.instagram.lite")
    sleep(5)
    d.click(360,934) # create account button
    sleep(3)
    x,y = search_sentence(d,"Sign up with email","inst")
    d.click(x,y)
    sleep(3)
    d.click(360,380)
    sleep(2)
    tap_keyboard(d,gmail)
    sleep(2)
    d.click(360,500) # next
    sleep(5)
    d.app_start("com.google.android.gm")
    sleep(1)
    d.click(90,120)
    sleep(1)
    x,y = search_sentence(d,"Social","inst")
    d.click(x,y)
    sleep(3)
    d.swipe(500, 1000, 500, 1000 + 500, duration = 0.1)
    sleep(20)
    code = None
    while code is None:
        code = return_code_inst(image_to_string(take_screenshot(d,app="inst")),"Instagram")
        d.swipe(500, 1000, 500, 1000 + 500, duration = 0.1)
        print("searching code again...")
        sleep(20)
        
    d.app_stop("com.google.android.gm")
    sleep(2)
    d.app_start("com.instagram.lite")
    sleep(5)
    tap_keyboard(d,code,keyboard_dic_only_nums)
    sleep(2)
    d.click(360,460)
    sleep(5)
    tap_keyboard(d,full_name)
    sleep(1)
    d.click(360,400)
    sleep(2)
    tap_keyboard(d,password)
    sleep(5)
    d.click(360,640)
    sleep(5)
    insert_date(d,date)
    sleep(2)
    d.click(360,1480)
    sleep(5)
    d.click(360,1501)
    sleep(3)
    d.click(660,360)
    sleep(1)
    d.click(360,360)
    sleep(1)
    tap_keyboard(d,username)
    sleep(2)
    d.click(360,600)
    sleep(20)
    d.click(363,1521)
    sleep(3)
    d.click(363,1120)
    sleep(3)
    d.click(363,1120)
    sleep(2)
    x,y = search_sentence(d,"Not Now","inst")
    d.click(x,y)
    sleep(3)
    d.app_stop("com.instagram.lite")

gmail = "riley.jackson1010@gmail.com"
password = "Whatthehe12"
date = "06/12/1988"
d = u2.connect("127.0.0.1:6555")
# setup_google(d,gmail,password)
# print_running_apps(d)
# sleep(5)
# setup_twitter(d,gmail,"17/9/1998","alexanderson_fit")
# setup_instagram(d,gmail,"Riley Jackson",password,date,"rileyj_foodiesss")
# print(d.app_current()["package"])
# setup_twitter(d,gmail,date,"riley_foodyyyy")
# setup_tiktok(d,gmail,date,"riley_foodyyyy")
insert_date(d,date)
