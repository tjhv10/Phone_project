from time import sleep
import random
from common_area_items import *
from common_area_functions import *

def search_youtube(d, video_name):
    try:
        x,y = find_best_match(take_screenshot(d,app="youtube"), "icons/youtube_icons/search.png",d)
    except:
        x,y = find_best_match(take_screenshot(d,app="youtube"), "icons/youtube_icons/xButton.png",d)
    d.click(int(x),int(y))
    sleep(2)
    type_keyboard(d, video_name)
    sleep(2)
    d.press("enter")
    sleep(5)
    result = search_sentence(d, video_name, plat="youtube", y_min=150)
    while result == None:
        d.swipe(500, 1000, 500, 500, duration = 0.1)
        sleep(3)
        result = search_sentence(d, video_name, plat="youtube", y_min=150)
    duration = extract_number_pairs(enhanced_image_to_string(take_screenshot(d,app="youtube",crop_area=(result[0],result[1]-200,result[0]+1000,result[1]))))
    while len(duration)==0 or duration == None:
        if result[1] > 350:
            d.swipe(500, 1000, 500, 500, duration = 0.5)
        elif result[1] < 350:
            d.swipe(500, 500, 500, 1000, duration = 0.5)
        sleep(5)
        result = search_sentence(d, video_name, plat="youtube", y_min=150)
        duration = extract_number_pairs(enhanced_image_to_string(take_screenshot(d,app="youtube",crop_area=(result[0],result[1]-200,result[0]+1000,result[1]))))
    d.click(*result)
    sleep(10)
    skip_button = search_sentence(d, "Skip", plat="youtube")
    while skip_button != None:
        d.click(int(skip_button[0]), int(skip_button[1]))
        sleep(10)
        skip_button = search_sentence(d, "Skip", plat="youtube")
    if search_sentence(d, "views", plat="youtube") == None:
        d.swipe(700,100,700,500,duration=0.1)

    return duration

def like(d):
    logging.info(d.serial + ": Liking video")
    try:
        x,y = find_best_match(take_screenshot(d,app="youtube"), "icons/youtube_icons/like.png",d)
        d.click(int(x),int(y))
        logging.info(d.serial + ": Video liked")
    except:
        logging.error(d.serial + ": No like button found")

def comment(d):
    logging.info(d.serial + ": Commenting video")
    if search_sentence(d, "Comments are turned off. Learn more", plat="youtube") != None:
        logging.info(d.serial + ": Comments are turned off")
        return
    try:
        x,y = search_sentence(d, "Comments", plat="youtube")
        d.click(int(x),int(y))
        logging.info(d.serial + ": Video Comments")
        sleep(2)
        d.click(rnd_value(375),rnd_value(1509)) # Click on comment box
        sleep(3)
        type_keyboard(d,random.choice(israel_support_comments)) 
        sleep(2)
        x,y = find_best_match(take_screenshot(d,app="youtube"), "icons/youtube_icons/send.png",d)
        d.click(rnd_value(int(x)),rnd_value(int(y)))
        logging.info(d.serial + ": Commented video")
    except:
        logging.error(d.serial + ": No Comments button found")

def subscribe(d):
    logging.info(d.serial + ": Subscribing to channel")
    try:
        x,y = find_best_match(take_screenshot(d,app="youtube"), "icons/youtube_icons/subscribe.png",d)
        d.click(int(x),int(y))
        logging.info(d.serial + ": Subscribed to channel")
    except:
        logging.error(d.serial + ": No subscribe button found")
    

def video_actions(d):
    like(d)
    comment(d)
    subscribe(d)


d = u2.connect("127.0.0.1:6555")
# video_actions(d)
# take_screenshot(d,app="youtube",crop_area=(540,639,696,703))
# search_youtube(d, "")
# subscribe(d)
# d.click(100,200)
