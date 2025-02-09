from time import sleep
import random
import threading
from common_area_items import *
from common_area_functions import *
import uiautomator2 as u2

def tap_users(d, users_template_path="icons/tiktok_icons/users.png"):
    logging.info(f"{threading.current_thread().name}:{d.serial} Starting tap_users function")
    screenshot_path = take_screenshot(d, threading.current_thread().name, "tik")
    best_coordinates = find_best_match(screenshot_path, users_template_path, d)
    if best_coordinates:
        d.click(int(best_coordinates[0]), int(best_coordinates[1]))
        update_results_file("Actions")
    else:
        d.click(196, 213)
        update_results_file("Actions")
        logging.info(f"{threading.current_thread().name}:{d.serial} Users button not found on the screen.")

def search(d, text):
    logging.info(f"{threading.current_thread().name}:{d.serial} Starting search function")
    screen_width = d.info['displayWidth']
    screen_height = d.info['displayHeight']
    x = screen_width * (650 / 720)
    y = screen_height * (100 / 1560)
    d.click(x, y)  # Click on the search bar
    update_results_file("Actions")
    sleep(10)
    tap_keyboard(d, text)
    sleep(15)
    d.press(66)  # Press the search button
    update_results_file("Actions")
    sleep(20)
    tap_users(d)  # Click to go to users
    sleep(10)
    d.click(350, 300)  # Click to go into the first result
    update_results_file("Actions")
    sleep(10)

def tap_like_button(d, like_button_template_path="icons/tiktok_icons/like.png"):
    logging.info(f"{threading.current_thread().name}:{d.serial} Starting tap_like_button function")
    screenshot_path = take_screenshot(d, threading.current_thread().name, "tik")
    sleep(2)
    best_coordinates = find_best_match(screenshot_path, like_button_template_path, d)
    sleep(2)
    if best_coordinates:
        logging.info(f"{threading.current_thread().name}:{d.serial} Like button found at {best_coordinates}, tapping...")
        d.click(int(best_coordinates[0]), int(best_coordinates[1]))
        update_results_file("Actions")
        logging.info(f"{threading.current_thread().name}:{d.serial} Tapped best match at {best_coordinates}.")
        update_results_file("Likes")
        sleep(1)
    else:
        logging.info(f"{threading.current_thread().name}:{d.serial} Like button not found on the screen.")
    logging.info(f"{threading.current_thread().name}:{d.serial} Finished tap_like_button function")

def comment_text(d, text, send_button_template_path="icons/tiktok_icons/send.png"):
    logging.info(f"{threading.current_thread().name}:{d.serial} Starting comment_text function")
    d.click(670, 1000)  # Click on the comment button
    update_results_file("Actions")
    logging.info(f"{threading.current_thread().name}:{d.serial} Clicked on the comment button.")
    sleep(3)
    d.click(310, 1500)  # Click on the comment input field
    update_results_file("Actions")
    logging.info(f"{threading.current_thread().name}:{d.serial} Commenting: {text}")
    sleep(4)
    tap_keyboard(d, text)
    sleep(2)
    screenshot_path = take_screenshot(d, threading.current_thread().name, "tik")
    sleep(2)
    best_coordinates = find_best_match(screenshot_path, send_button_template_path, d)
    sleep(2)
    if best_coordinates:
        logging.info(f"{threading.current_thread().name}:{d.serial} Send button found at {best_coordinates}, tapping...")
        d.click(int(best_coordinates[0]), int(best_coordinates[1]))
        update_results_file("Actions")
        logging.info(f"{threading.current_thread().name}:{d.serial} Tapped best match at {best_coordinates}.")
        sleep(1)
        update_results_file("Comments")
        sleep(1)
    else:
        logging.info(f"{threading.current_thread().name}:{d.serial} Send button not found on the screen.")
    logging.info(f"{threading.current_thread().name}:{d.serial} Comment submitted.")
    sleep(3)
    d.press("back")
    update_results_file("Actions")

def scroll_random_number(d):
    logging.info(f"{threading.current_thread().name}:{d.serial} Starting scroll_random_number function")
    
    if d(scrollable=True).exists:
        logging.info(f"{threading.current_thread().name}:{d.serial} Found a scrollable view! Swiping down...")
        num_swipes = random.randint(1, 2)
        logging.info(f"{threading.current_thread().name}:{d.serial} Number of swipes: {num_swipes}")
        for i in range(num_swipes):
            arch_swipe(d, *swipe_function_param)
            update_results_file("Actions")
            random_time = random.randint(2, 15)
            sleep(random_time)
            logging.info(f"{threading.current_thread().name}:{d.serial} Swiped down {i + 1} time(s).")
    else:
        logging.info(f"{threading.current_thread().name}:{d.serial} No scrollable view found!")
        main(d)


def scroll_like_and_comment(d,postsToLike):
    """
    Scrolls the view and likes posts.
    """

    tap_like_button(d)

    for i in range(postsToLike):
        if d(scrollable=True).exists:
            arch_swipe(d, *swipe_function_param)
            update_results_file("Actions")
            random_time = random.randint(2, 15)
            sleep(random_time)
            logging.info(f"{threading.current_thread().name}:{d.serial} Swiped down {i + 1} time(s).")
        else:
            logging.info(f"{threading.current_thread().name}:{d.serial} No scrollable view found!")
            main(d)
        num = random.choice([1, 2, 3, 4, 5])
        if  num <= 2:
            logging.info(f"{threading.current_thread().name}:{d.serial} like")
            tap_like_button(d)
            sleep(1)
        elif num>2 and num<=4:
            logging.info(f"{threading.current_thread().name}:{d.serial} like and comment")
            tap_like_button(d)
            sleep(2)
            comment_text(d,random.choice(israel_support_comments))
            sleep(1)
        else:
            logging.info(f"{threading.current_thread().name}:{d.serial} none")
    d.press("back")
    d.press("back")
    sleep(2)
    d.press("back")
    sleep(2)
    d.press("back")
    sleep(4)
    d.press("back")


def like_a_page(d, page):
    # Open TikTok app
    if "com.zhiliaoapp.musically" in d.app_list_running():
        # Stop Tiktok app
        d.app_stop("com.zhiliaoapp.musically")
        sleep(8)

    # Start the Twitter app 
    d.app_start("com.zhiliaoapp.musically")
    sleep(12)
    search(d, page)
    sleep(5)
    try:
        x,y = search_sentence(d,"Follow")
        d.click(x,y)
    except:
        logging.info(f"{threading.current_thread().name}:{d.serial} : Allready following!")
    sleep(10)
    d.click(120, 1450) # Get in the first page
    update_results_file("Actions")
    sleep(5)
    scroll_like_and_comment(d,10)


def report_tiktok_posts(d):
    choice = random.choice([1, 2])

    if choice == 1:
        post = random.choice(tiktok_posts_to_report)
        report_post(d, post[0], post[1])


def report_post(d, link, action=0):
    # Open TikTok app
    if "com.zhiliaoapp.musically" in d.app_list_running():
        # Stop Tiktok app
        d.app_stop("com.zhiliaoapp.musically")
        sleep(4)

    # Start the Twitter app 
    d.app_start("com.zhiliaoapp.musically")
    logging.info(f"{threading.current_thread().name}:{d.serial} : Opened TikTok!")
    sleep(15)

    if "com.zhiliaoapp.musically" in d.app_list_running():
        logging.info(f"{threading.current_thread().name}:{d.serial} TikTok is running!")
        d.shell(f"am start -a android.intent.action.VIEW -d {link}")
        logging.info(f"{threading.current_thread().name}:{d.serial} Opened link: {link}")
        sleep(10)
            
        try:   
            # Find and click the "Watch only" button
            x, y = search_sentence(d, "Watch only","tik")
            d.click(int(x), int(y))
            update_results_file("Actions")
            sleep(7)
        except:
           pass
        
            
        # Click on the share button
        d.click(660, 1240)
        update_results_file("Actions")
        sleep(3)

        # Click on the report button
        d.click(90, 1400)
        update_results_file("Actions")
        sleep(5)
    
        if action == 0: 
            handle_user_selection(d, report_tiktok_clicks)
        else:
            logging.info(report_tiktok_clicks[report_tiktok_keys[action - 1]])
            execute_action(d, report_tiktok_keys[action - 1], report_tiktok_clicks)
        
        sleep(4)
        update_results_file("Posts reported")
    
        # Stop TikTok app
        d.app_stop("com.zhiliaoapp.musically")


def report_account(d, link):
    # Open TikTok app
    if "com.zhiliaoapp.musically" in d.app_list_running():
        # Stop Tiktok app
        d.app_stop("com.zhiliaoapp.musically")
        sleep(4)

    # Start the Twitter app 
    d.app_start("com.zhiliaoapp.musically")
    logging.info(f"{threading.current_thread().name}:{d.serial} : Opened TikTok!")

    # Wait to make sure TikTok fully loads
    sleep(15)

    # Check if TikTok is running
    if "com.zhiliaoapp.musically" in d.app_list_running():
        logging.info(f"{threading.current_thread().name}:{d.serial} TikTok is running!")

        # Open link with TikTok
        d.shell(f"am start -a android.intent.action.VIEW -d {link}")
        logging.info(f"{threading.current_thread().name}:{d.serial} Opened link: {link}")

        # Give some time to load the page within TikTok
        sleep(15)

        # Continue with the reporting steps
        try:
            d.click(660, 120)  # Click on the share button
            update_results_file("Actions")
            sleep(3)
            d.click(90, 1400)  # Click on the report button
            update_results_file("Actions")
            sleep(5)
            d.click(336, 370)  # Reporting account
            update_results_file("Actions")
            sleep(2)
            d.click(336, 370)  # Click on "posts inappropriate content"
            update_results_file("Actions")
            sleep(2)
            d.click(336, 974)  # Click on "other"
            update_results_file("Actions")
            sleep(2)
            d.click(336, 1480)  # Click on "submit"
            update_results_file("Actions")
            sleep(2)
            update_results_file("Accounts reported")
        finally:
            d.app_stop("com.zhiliaoapp.musically")
            logging.info(f"{threading.current_thread().name}:{d.serial} : Stopped TikTok.")


def support_accounts(d,accounts):
    random.shuffle(accounts)
    for account in accounts:
        if "com.zhiliaoapp.musically" in d.app_list_running():
            # Stop Tiktok app
            d.app_stop("com.zhiliaoapp.musically")
            sleep(4)

        # Start the Twitter app 
        d.app_start("com.zhiliaoapp.musically")  # Open TikTok app
        logging.info(f"{threading.current_thread().name}:{d.serial} :Opened TikTok!")
        sleep(15)
        search(d,account)
        sleep(2)
        d.click(100,1000)
        sleep(2)
        scroll_like_and_comment(d,5)
        d.app_stop("com.zhiliaoapp.musically")
        sleep(4)


def main(d):
    """
    The main function connects to the Android device and performs various TikTok actions.

    Args:
        d: The connected Android device object.

    Returns:
        None
    """
    start_time = time.time()
    try:
        for _ in range(5):
            if "com.zhiliaoapp.musically" in d.app_list_running():
                d.app_stop("com.zhiliaoapp.musically")
                time.sleep(4)

            d.app_start("com.zhiliaoapp.musically")  # Open TikTok app
            logging.info("Opened TikTok!")
            time.sleep(15)

            if time.time() - start_time > MAX_DURATION:
                logging.info("Exceeded max duration. Exiting main.")
                break

            scroll_random_number(d)
            time.sleep(4)
            like_a_page(d, random.choice(tiktok_accounts))
            scroll_random_number(d)
            time.sleep(10)

        support_accounts(d, tiktok_handles_specials)
        report_tiktok_posts(d)
        time.sleep(3)
        d.app_stop("com.zhiliaoapp.musically")
        logging.info("Done with TikTok!")


    except Exception as e:
        logging.error("An error occurred", exc_info=True)
        d.app_stop("com.zhiliaoapp.musically")

# d = u2.connect("127.0.0.1:6555")
# main(d)
# x,y = search_sentence(d,"Follow","tik")
# d.click(x,y)
# report_post(d,random.choice(tiktok_posts_to_report)[0])
# report_account(d,"https://www.tiktok.com/@healwithtati")
