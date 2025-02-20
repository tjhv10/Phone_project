import threading
from time import sleep
import random
from common_area_items import *
from common_area_functions import *
import re

def search_youtube(d, video_name):
    try:
        x,y = find_best_match(take_screenshot(d,app="youtube"), "icons/youtube_icons/search.png",d)
    except:
        x,y = find_best_match(take_screenshot(d,app="youtube"), "icons/youtube_icons/xButton.png",d)
    d.click(int(x),int(y))
    sleep(2)
    tap_keyboard(d, video_name)
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
    return duration

d = u2.connect("127.0.0.1:6555")
search_youtube(d, "the best of israel")