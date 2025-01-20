import uiautomator2 as u2
from time import sleep
from common_area_items import *
from common_area_functions import *

def scroll_once(d):
    """
    Scrolls down once on a scrollable view in the app if it exists.

    Parameters:
    d (uiautomator2.Device): The connected device object from uiautomator2.
    """
    logging.info(f"{threading.current_thread().name}:{d.wlan_ip} Starting scroll_once function")
    """
    Scrolls down once on a scrollable view in the app if it exists.

    Parameters:
    d (uiautomator2.Device): The connected device object from uiautomator2.
    """
    logging.info("Starting scroll_once function")
    if d(scrollable=True).exists:
        arch_swipe(d, *swipe_function_param)
        random_time = random.randint(1, 6)
        update_results_file("Scroll")
        logging.info(f"Swiped once. Waiting {random_time} seconds.")
        sleep(random_time)
    else:
        logging.warning("No scrollable view found!")

def scroll_random_number(d):
    """
    Scrolls down a random number of times between 3 and 8.

    Parameters:
    d (uiautomator2.Device): The connected device object from uiautomator2.
    """
    logging.info(f"{threading.current_thread().name}:{d.wlan_ip} Starting scroll_random_number function")
    """
    Scrolls down a random number of times between 3 and 8.

    Parameters:
    d (uiautomator2.Device): The connected device object from uiautomator2.
    """
    logging.info("Starting scroll_random_number function")
    if d(scrollable=True).exists:
        num_swipes = random.randint(3, 8)
        logging.info(f"Number of swipes: {num_swipes}")
        update_results_file("Scroll", num_swipes)

        for i in range(num_swipes):
            arch_swipe(d, *swipe_function_param)
            random_time = random.randint(2, 15)
            logging.info(f"Swipe {i + 1}/{num_swipes}. Waiting {random_time} seconds.")
            sleep(random_time)
    else:
        logging.warning("No scrollable view found!")
    logging.info(f"{threading.current_thread().name}:{d.wlan_ip} Finished scroll_random_number function")


def search_and_go_to_account(d, name):
    """
    Searches for a specific user on TikTok by simulating clicks and typing.

    Parameters:
    d (uiautomator2.Device): The connected device object from uiautomator2.
    text (str): The text to search for.
    """
    logging.info(f"{threading.current_thread().name}:{d.wlan_ip} Starting search_and_go_to_account function")
    # Calculate the coordinates as percentages of the screen resolution
    d.click(215, 1515)  # Click on the search button
    sleep(1)
    d.click(215, 1515)  # Click on the search button
    sleep(3)    
    d.click(352,100)  # Click on the search bar
    sleep(3)
    d.click(661,109)
    sleep(1)
    tap_keyboard(d,name)
    sleep(10)
    # d.click(357,221) # Press the search button
    try:
        d.click(*tap_search_icon(d))
    except:
        logging.info(f"{threading.current_thread().name}:{d.wlan_ip} somthing wrong happend")
        take_screenshot(d,threading.current_thread(),"insterr")
        
        
    sleep(5)
    d.click(*search_sentence(d,"Accounts","inst")) # Press the accounts button
    sleep(5)
    try:
        x,y = search_sentence(d,name,"inst",y_min=180) 
        print("Found account!")
    except:
        search_and_go_to_account(d,random.choice(instagram_accounts))
        return
    d.click(int(x),int(y))
    sleep(5)
    num = random.choice([1,2,3])
    if num >=2:
        follow_page(d)
    sleep(4)
    arch_swipe(d, *swipe_function_param)
    sleep(4)
    d.click(120,1000)
    logging.info(f"{threading.current_thread().name}:{d.wlan_ip} Finished search_and_go_to_account function")


def tap_like_button(d, like_button_template_path="icons/instagram_icons/like.png"):
    """
    Takes a screenshot and tries to tap on the like button if found.

    Parameters:
    d (uiautomator2.Device): The connected device object from uiautomator2.
    like_button_template_path (str): Path to the like button template image.
    """
    logging.info(f"{threading.current_thread().name}:{d.wlan_ip} Starting tap_like_button function")
    screenshot_path = take_screenshot(d,threading.current_thread().name,'inst')
    best_match = find_best_match(screenshot_path, like_button_template_path,d)

    # If the like button was found, tap on it
    if best_match and best_match[0] < 170:
        print(f"Like button found at {best_match} with match value: {best_match}, tapping...")
        d.click(int(best_match[0]), int(best_match[1]))  # Tap the best match
        update_results_file("Likes")
    else:
        print("Like button not found on the screen.")
    logging.info(f"{threading.current_thread().name}:{d.wlan_ip} Finished tap_like_button function")


def tap_search_icon(d, search_icon_template_path="icons/instagram_icons/search_icon.png"):
    """
    Takes a screenshot and tries to tap on the like button if found.

    Parameters:
    d (uiautomator2.Device): The connected device object from uiautomator2.
    search_icon_template_path (str): Path to the like button template image.
    """
    logging.info(f"{threading.current_thread().name}:{d.wlan_ip} Starting tap_search_icon function")
    screenshot_path = take_screenshot(d,threading.current_thread().name,'inst')
    best_match = find_best_match(screenshot_path, search_icon_template_path,d)
    print(f"Serach icon found at {best_match} with match value: {best_match}, clicking...")
    logging.info(f"{threading.current_thread().name}:{d.wlan_ip} Finished tap_search_icon function")
    if best_match:
        return best_match[0],best_match[1]
    else:
        return None


def comment_text(d,text, comment_template_path="icons/instagram_icons/comment.png"):
    """
    Takes a screenshot and tries to tap on the comment icon if found.

    Parameters:
    d (uiautomator2.Device): The connected device object from uiautomator2.
    comment_template_path (str): Path to the comment icon template image.
    """
    logging.info(f"{threading.current_thread().name}:{d.wlan_ip} Starting comment_text function")
    # Take a screenshot of the current screen
    screenshot_path = take_screenshot(d,threading.current_thread().name,"inst")
    
    # Find the best match for the comment icon in the screenshot
    coordinates = find_best_match(screenshot_path, comment_template_path,d)
    sleep(2)
    # If the comment icon was found, tap on it
    if coordinates:
        d.click(int(coordinates[0]), int(coordinates[1]))  # Tap the comment button
    else:
        print("Comment not found on the screen.")
    sleep(2)
    screenshot_path = take_screenshot(d,threading.current_thread().name,"inst")
    
    # Find the best match for the comment icon in the screenshot
    num_coordinates = find_best_match(screenshot_path, "icons/instagram_icons/num.png",d)
    if num_coordinates != None:
        sleep(2)
        tap_keyboard(d,text)
        sleep(1)
        d.press(66)
        sleep(1)
        update_results_file("Comments")
        sleep(1)
        d.press("back")
        sleep(1)
    if coordinates !=  None:
        d.press("back")
        sleep(2)
    sleep(2)
    logging.info(f"{threading.current_thread().name}:{d.wlan_ip} Finished comment_text function")

def scroll_like_and_comment(d):
    """
    Scrolls the screen and tries to like a tweet after each scroll by tapping the like button.

    Parameters:
    d (uiautomator2.Device): The connected device object from uiautomator2.
    """
    logging.info(f"{threading.current_thread().name}:{d.wlan_ip} Starting scroll_like_and_comment function")
    for _ in range(rnd_value(10)):
        scroll_once(d)  # Scroll down once
        sleep(3)  # Wait 3 second between actions
        num = random.choice([1,2,3,4,5]) 
        if num<=4:
            tap_like_button(d)
            if num>2:
                sleep(3)
                comment_text(d,random.choice(israel_support_comments))  # Try to tap the like button to like the post
        sleep(1)  # Wait 2 seconds after tapping
    d.press("back")
    sleep(0.8)
    d.press("back")
    sleep(0.89)
    d.press("back")
    sleep(0.95)
    d.press("back")
    sleep(0.78)
    d.press("back")
    sleep(0.99)
    d.click(73,1508) # press home
    logging.info(f"{threading.current_thread().name}:{d.wlan_ip} Finished scroll_like_and_comment function")

def report_post(d, link,action = 0):
    logging.info(f"{threading.current_thread().name}:{d.wlan_ip} Starting report_post function")
    # Open Twitter app
    d.app_start("com.instagram.lite")
    print(f"{threading.current_thread().name}:{d.wlan_ip} :Opened Instagram!")
    # sleep(15)

    if "com.instagram.lite" in d.app_list_running():
        print(f"{threading.current_thread().name}:{d.wlan_ip} Instagram is running!")

        # Open the tweet in the Twitter app
        d.shell(f"am start -a android.intent.action.VIEW -d '{link}'")
        print(f"{threading.current_thread().name}:{d.wlan_ip} Opened: {link}")
        sleep(3)
        # Click on the 3 dots button
        d.click(650, 130)
        sleep(3)
        # # Click on the report button
        d.click(370, 1018)
        sleep(3)
        # # Click on the report button
        d.click(370, 712)
        sleep(8)
        if action == 0: 
            handle_user_selection(d,report_instagram_post_clicks)
        else:
            print(report_instagram_post_clicks[report_instagram_keys[action-1]])
            execute_action(d,report_instagram_keys[action-1],report_instagram_post_clicks)
        sleep(2)
        update_results_file("Posts reported")
        sleep(4)
        d.app_stop("com.twitter.android")
        logging.info(f"{threading.current_thread().name}:{d.wlan_ip} Finished report_post function")


# TODO fix function
# def report_account(d, link): 
#     logging.info(f"{threading.current_thread().name}:{d.wlan_ip} Starting report_account function")
#     # Open Twitter app
#     d.app_start("com.instagram.lite")
#     print(f"{threading.current_thread().name}:{d.wlan_ip} :Opened Instagram!")
#     # sleep(15)

#     if "com.instagram.lite" in d.app_list_running():
#         print(f"{threading.current_thread().name}:{d.wlan_ip} Instagram is running!")

#         # Open the tweet in the Twitter app
#         d.shell(f"am start -a android.intent.action.VIEW -d '{link}'")
#         print(f"{threading.current_thread().name}:{d.wlan_ip} Opened: {link}")
#         sleep(3)
#         # Click on the share button
#         d.click(660, 135)
#         sleep(3)
#         d.click(*search_sentence(d,"Report_","inst"))
#         sleep(3)
#         d.click(*search_sentence(d,"Report Account","inst"))
#         sleep(3)
#         d.click(*search_sentence(d,"it's posting content that shoulden't be on","inst"))
#         sleep(8)
#         handle_user_selection(d,report_instagram_account_clicks)
#         sleep(2)
#         update_results_file("Accounts reported")
#         sleep(4)
#         d.app_stop("com.twitter.android")
#     logging.info(f"{threading.current_thread().name}:{d.wlan_ip} Finished report_account function")



def comment_text(d,text, comment_template_path="icons/instagram_icons/comment.png"):
    """
    Takes a screenshot and tries to tap on the comment icon if found.

    Parameters:
    d (uiautomator2.Device): The connected device object from uiautomator2.
    comment_template_path (str): Path to the comment icon template image.
    """
    logging.info(f"{threading.current_thread().name}:{d.wlan_ip} Starting comment_text function")
    # Take a screenshot of the current screen
    screenshot_path = take_screenshot(d,threading.current_thread().name,"inst")
    
    # Find the best match for the comment icon in the screenshot
    coordinates = find_best_match(screenshot_path, comment_template_path,d)
    sleep(2)
    # If the comment icon was found, tap on it
    if coordinates:
        d.click(int(coordinates[0]), int(coordinates[1]))  # Tap the comment button
    else:
        print("Comment not found on the screen.")
    sleep(2)
    screenshot_path = take_screenshot(d,threading.current_thread().name,"inst")
    
    # Find the best match for the comment icon in the screenshot
    num_coordinates = find_best_match(screenshot_path, "icons/instagram_icons/num.png",d)
    if num_coordinates != None:
        sleep(2)
        tap_keyboard(d,text)
        sleep(1)
        d.press(66)
        sleep(1)
        update_results_file("Comments")
        sleep(1)
        d.press("back")
        sleep(1)
    if coordinates !=  None:
        d.press("back")
        sleep(2)
    sleep(2)
    logging.info(f"{threading.current_thread().name}:{d.wlan_ip} Starting comment_text function")

def follow_page(d, follow_template_path="icons/instagram_icons/follow.png"):
    print(f"{threading.current_thread().name}:{d.wlan_ip} Starting follow_page function")
    screenshot_path = take_screenshot(d,threading.current_thread().name,"inst")
    best_match = find_best_match(screenshot_path, follow_template_path,d)
    if not best_match:
        best_match = find_best_match(screenshot_path, "icons/instagram_icons/follow_small.png",d)
    if best_match:
        d.click(int(best_match[0]), int(best_match[1]))
        print(f"{threading.current_thread().name}:{d.wlan_ip} Followed account!")
        sleep(2)
        update_results_file("Follows")
    else:
        print(f"{threading.current_thread().name}:{d.wlan_ip} Follow icon not found on the screen.")
    print(f"{threading.current_thread().name}:{d.wlan_ip} Finished follow_page function")

def support_accounts(d,accounts):
    logging.info(f"{threading.current_thread().name}:{d.wlan_ip} Starting support_accounts function")
    random.shuffle(accounts)
    for account in accounts:
        search_and_go_to_account(d,account)
        sleep(2)
        scroll_like_and_comment(d)
    logging.info(f"{threading.current_thread().name}:{d.wlan_ip} Starting support_accounts function")
        
def main(d):
    """
    The main function connects to the Android device and performs various Instagram actions.

    Args:
        d: The connected Android device object.

    Returns:
        None
    """
    start_time = time.time()
    logging.info(f"Starting main with duration limit: {MAX_DURATION}")

    try:
        d.app_start("com.instagram.lite")
        logging.info("Opened Instagram!")
        time.sleep(10)

        for _ in range(5):
            if time.time() - start_time > MAX_DURATION:
                logging.info("Exceeded max duration. Exiting main.")
                break

            scroll_random_number(d)
            time.sleep(2)
            tap_like_button(d)
            time.sleep(7)
            search_and_go_to_account(d, random.choice(instagram_accounts))
            time.sleep(3)
            scroll_like_and_comment(d)
            time.sleep(3)
            scroll_random_number(d)
            tap_like_button(d)
            scroll_random_number(d)
            time.sleep(2)

        support_accounts(d, instagram_handles_special)
        time.sleep(3)
        d.app_stop("com.instagram.lite")

    except Exception as e:
        logging.error("An error occurred", exc_info=True)
        d.app_stop("com.instagram.lite")

d = u2.connect("127.0.0.1:6555")
# main(d)
# report_account(d,"https://www.instagram.com/freepalestineland?igsh=YzljYTk1ODg3Zg==") #TODO fix  func
# report_post(d,"https://www.instagram.com/p/DEXwklSKeW5/?igsh=YzljYTk1ODg3Zg==")
search_and_go_to_account(d,"idf")