import threading
from time import sleep
import random
from common_area import *
import uiautomator2 as u2
import logging

# Configure logging
log_file = "logs.log" # Log file to capture output
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


#TODO add pic equlaizer to save from unexpected behavior


def tap_like_button(d, like_button_template_path="icons/twitter_icons/like.png"):
    logging.info(f"{threading.current_thread().name}:{d.wlan_ip} Starting tap_like_button function")
    
    screenshot_path = take_screenshot(d,threading.current_thread().name,"twi")
    
    best_cordinates = find_best_match(screenshot_path, like_button_template_path,d)    
    
    if best_cordinates:
        logging.info(f"{threading.current_thread().name}:{d.wlan_ip} Like button found at {best_cordinates}, tapping...")
        d.click(int(best_cordinates[0]), int(best_cordinates[1]))
        update_results_file("Actions")
        logging.info(f"{threading.current_thread().name}:{d.wlan_ip} Tapped best match at {best_cordinates}.")
        update_results_file("Likes")
    else:
        logging.info(f"{threading.current_thread().name}:{d.wlan_ip} Like button not found on the screen.")
    
    logging.info(f"{threading.current_thread().name}:{d.wlan_ip} Finished tap_like_button function")
    

def comment_text(d, text, comment_template_path="icons/twitter_icons/comment.png"):
    logging.info(f"{threading.current_thread().name}:{d.wlan_ip} Starting comment_text function")
    screenshot_path = take_screenshot(d,threading.current_thread().name,"twi")
    best_match = find_best_match(screenshot_path, comment_template_path,d)
    if best_match:
        d.click(int(best_match[0]), int(best_match[1]))  # Unpack directly
        update_results_file("Actions")
        sleep(10)
        result = search_sentence(d,"posts.","twi", tolerance=0) # For post location message
        if result:
            d.click(430,910)
            sleep(5)
            x,y = search_sentence(d,"Post your replay","twi", tolerance=20) # For post location message
            d.click(int(x),int(y))
            sleep(5)
        result = search_sentence(d,"2123","twi", tolerance=20) # For post location message
        if not result:
            d.click(int(350),int(350))
            sleep(5)
        tap_keyboard(d,text) 
        sleep(1)
        logging.info(f"{threading.current_thread().name}:{d.wlan_ip} Searching for: {text}")
        if search_sentence(d,text[:29],"twi"):
            update_results_file("Comments")
            sleep(1)
            d.click(600, 125)  # Click the post button
            update_results_file("Actions")
            logging.info(f"{threading.current_thread().name}:{d.wlan_ip} Commented: {text}")
        else:
            logging.info(f"{threading.current_thread().name}:{d.wlan_ip} Comment is deprecated, canceling.")
            d.click(60,130)
            update_results_file("Actions")
            sleep(3)
            d.click(430,920)
            update_results_file("Actions")
            logging.info(f"{threading.current_thread().name}:{d.wlan_ip} Got out of deprecated comment.")
    else:
        logging.info(f"{threading.current_thread().name}:{d.wlan_ip} Comment icon not found on the screen.")
        
    logging.info(f"{threading.current_thread().name}:{d.wlan_ip} Finished comment_text function")
        

def tap_repost_button(d, repost_button_template_path="icons/twitter_icons/repost.png"):
    logging.info(f"{threading.current_thread().name}:{d.wlan_ip} Starting tap_repost_button function")
    
    screenshot_path = take_screenshot(d,threading.current_thread().name,"twi")
    
    best_cordinates = find_best_match(screenshot_path, repost_button_template_path,d)    
    
    if best_cordinates:
        logging.info(f"{threading.current_thread().name}:{d.wlan_ip} repost button found at {best_cordinates}, tapping...")
        d.click(int(best_cordinates[0]), int(best_cordinates[1]))
        update_results_file("Actions")
        logging.info(f"{threading.current_thread().name}:{d.wlan_ip} Tapped best match at {best_cordinates}.")
        sleep(2)
        d.click(360,1370) # Tap repost button
        update_results_file("Actions")
        update_results_file("Reposts")
    else:
        logging.info(f"{threading.current_thread().name}:{d.wlan_ip} reposts button not found on the screen.")
    
    logging.info(f"{threading.current_thread().name}:{d.wlan_ip} Finished tap_reposts_button function")

def scroll_like_and_comment(d,posts):
    logging.info(f"{threading.current_thread().name}:{d.wlan_ip} Starting scroll_like_and_comment function")
    actions = ['like', 'comment', 'both', 'none']
    for _ in range(posts):
        if d(scrollable=True).exists:
            start_x = random.randint(400, 600)
            start_y = random.randint(900, 1200)
            end_y = start_y - random.randint(400, 600)
            swipe_duration = random.uniform(0.04, 0.06)
            d.swipe(start_x, start_y, start_x, end_y, duration=swipe_duration)
            update_results_file("Actions")
            logging.info(f"{threading.current_thread().name}:{d.wlan_ip} Scrolled from ({start_x}, {start_y}) to ({start_x}, {end_y}) in {swipe_duration:.2f} seconds.")
        else:
            logging.info(f"{threading.current_thread().name}:{d.wlan_ip} No scrollable view found!")
            main(d)

            
        sleep(random.uniform(2, 14))
        action = random.choice(actions)
        logging.info(f"{threading.current_thread().name}:{d.wlan_ip} Action chosen: {action}")
        text = random.choice(israel_support_comments)
        if action == 'like':
            tap_like_button(d)
            logging.info(f"{threading.current_thread().name}:{d.wlan_ip} Liked the post.")

        elif action == 'both':
            tap_like_button(d)
            logging.info(f"{threading.current_thread().name}:{d.wlan_ip} Liked the post.")
            sleep(2)
            sleep(2)
            num = random.choice([1,2,3,4,5])
            if num==3:
                comment_text(d, text)
                logging.info(f"{threading.current_thread().name}:{d.wlan_ip} Commented: {text}")
                tap_repost_button(d)
                logging.info(f"{threading.current_thread().name}:{d.wlan_ip} Reposted.")
            elif num<=2:
                comment_text(d, text)
                logging.info(f"{threading.current_thread().name}:{d.wlan_ip} Commented: {text}")
        
        sleep(3)
    sleep(2)
    d.press("back")
    sleep(0.5)
    d.press("back")
    sleep(2)
    logging.info(f"{threading.current_thread().name}:{d.wlan_ip} Finished scroll_like_and_comment function")


def scroll_random_number(d):
    """
    Scrolls down a random number of times between 1 and 3 and then scrolls up.

    Parameters:
    d (uiautomator2.Device): The connected device object from uiautomator2.
    """
    if d(scrollable=True).exists:
        logging.info(f"{threading.current_thread().name}:{d.wlan_ip} Found a scrollable view! Swiping down...")

        # Randomly choose how many times to swipe (between 1 and 6)
        num_swipes = random.randint(1, 6)
        logging.info(f"{threading.current_thread().name}:{d.wlan_ip} Number of swipes: {num_swipes}")



        # Perform the swipe action for the chosen number of times
        for _ in range(num_swipes):
            if d(scrollable=True).exists:
                start_x = random.randint(400, 600)
                start_y = random.randint(900, 1200)
                end_y = start_y - random.randint(400, 600)
                swipe_duration = random.uniform(0.04, 0.06)
                d.swipe(start_x, start_y, start_x, end_y, duration=swipe_duration)
                update_results_file("Actions")
                logging.info(f"{threading.current_thread().name}:{d.wlan_ip} Scrolled from ({start_x}, {start_y}) to ({start_x}, {end_y}) in {swipe_duration:.2f} seconds.")
            else:
                logging.info(f"{threading.current_thread().name}:{d.wlan_ip} No scrollable view found!")
                d.click(40,1340)
                update_results_file("Actions")
                main(d)
            sleep(random.randint(2, 10))
    else:
        logging.info(f"{threading.current_thread().name}:{d.wlan_ip} No scrollable view found!")
        main(d)
        


def search_and_go_to_page(d, page_name):
    """ 
    Searches for the specified text in Twitter and navigates to the desired page.

    Parameters:
    d (uiautomator2.Device): The connected device object from uiautomator2.
    text (str): The text to search for.
    """
    # Start the Twitter app 

    if "com.twitter.android" in d.app_list_running():
        # Stop Twitter app
        d.app_stop("com.twitter.android")
        sleep(2)

    # Start the Twitter app 
    d.app_start("com.twitter.android")
    logging.info(f"{threading.current_thread().name}:{d.wlan_ip} : Opened Twitter!")
    sleep(10)

    # Swipe up to return to the previous content
    d.swipe(500, 300, 500, 1000, duration = 0.05)
    update_results_file("Actions")
    sleep(3)
    # Perform the search
    d.click(180, 1500)
    update_results_file("Actions")
    file_name = "bug.txt"
    logging.info(page_name+" ohhhh")
    if page_name.strip() == "israel":
        with open(file_name, "w") as file:
            file.write(f"Account: {page_name}\n")
            file.write(f"Memory address: {hex(id(page_name))}\n")
            file.write("\n")  # Add a newline for better readability


    logging.info(f"{threading.current_thread().name}:{d.wlan_ip} Clicked on the search button.")
    logging.info(f"{threading.current_thread().name}:{d.wlan_ip} serching for {page_name}.")
    sleep(3)
    # Click on the search input field
    d.click(360, 140)
    update_results_file("Actions")
    sleep(5)
     # Type each character of the search term with a random delay to simulate human typing
    tap_keyboard(d,page_name)
    sleep(15)
    logging.info(f"{threading.current_thread().name}:{d.wlan_ip} Typed '{page_name}' in the search bar naturally.")
    try:
        x,y = search_sentence(d,"@"+page_name,"twi")
        d.click(int(x),int(y))
        update_results_file("Actions")
    except:
        try:
            x,y = search_sentence(d,"@"+page_name.lower(),"twi")
            d.click(int(x),int(y))
            update_results_file("Actions")
        except:
            logging.info("Didnt find page!")
    
    logging.info(f"{threading.current_thread().name}:{d.wlan_ip} Got into the page!")
    sleep(5)

def follow_page(d, follow_template_path="icons/twitter_icons/follow.png"):
    logging.info(f"{threading.current_thread().name}:{d.wlan_ip} Starting follow_page function")
    screenshot_path = take_screenshot(d,threading.current_thread().name,"twi")
    best_match = find_best_match(screenshot_path, follow_template_path,d)
    if best_match:
        num = random.choice([1, 2]) #TODO change to 4,20
        if  num == 1:
            d.click(int(best_match[0]), int(best_match[1]))
            update_results_file("Actions")
            logging.info(f"{threading.current_thread().name}:{d.wlan_ip} Followed account!")
            update_results_file("Follows")
            sleep(1)
        else:
            logging.info(f"{threading.current_thread().name}:{d.wlan_ip} didn't followed account!")
            
        sleep(2)
    else:
        logging.info(f"{threading.current_thread().name}:{d.wlan_ip} Follow icon not found on the screen.")
    logging.info(f"{threading.current_thread().name}:{d.wlan_ip} Finished follow_page function")
        

def report_twitter_posts(d):
    choice = random.choice([1, 2])

    if choice == 1:
        post = random.choice(twitter_posts_to_report)
        report_post(d, post[0], post[1])

def report_twitter_accounts(d):
    choice = random.choice([1, 2])

    if choice == 1:
        account = random.choice(anti_israel_twitter)
        report_account(d, account)


def report_post(d, link, action=0):
    # Open Twitter app
    
    if "com.twitter.android" in d.app_list_running():
        # Stop Twitter app
        d.app_stop("com.twitter.android")
        sleep(2)
        

    # Start the Twitter app 
    d.app_start("com.twitter.android")
    logging.info(f"{threading.current_thread().name}:{d.wlan_ip} : Opened Twitter!")
    sleep(10)

    if "com.twitter.android" in d.app_list_running():
        logging.info(f"{threading.current_thread().name}:{d.wlan_ip} Twitter is running!")
        # Open the tweet in the Twitter app
        d.shell(f"am start -a android.intent.action.VIEW -d '{link}'")
        logging.info(f"{threading.current_thread().name}:{d.wlan_ip} Opened tweet: {link}")
        sleep(10)
            
        try:
            # Click on the share button
            d.click(685, 210)
            update_results_file("Actions")
            sleep(3)
            if search_sentence(d, "you reported this post.","twi"):
                logging.info(f"{threading.current_thread().name}:{d.wlan_ip} already reported this tweet.")
                return 
            # Click on the report button
            # x, y = search_sentence(d, "Report post","twi")
            # sleep(3)
            d.click(int(515), int(815))
            update_results_file("Actions")
            sleep(15)
            while not search_sentence(d,"What type of issue are","twi"):
                logging.info(f"{threading.current_thread().name}:{d.wlan_ip} Waiting for report page to load...")
                sleep(10)

            if action == 0: 
                handle_user_selection(d, report_twitter_clicks)
            else:
                execute_action(d, twitter_report_keys[action-1], report_twitter_clicks)
            
            update_results_file("Posts reported")
        
            # Stop Twitter app
            d.app_stop("com.twitter.android")

        except Exception as e:
            logging.info(f"{threading.current_thread().name}:{d.wlan_ip} already reported that post.")
            # Stop Twitter app
            d.app_stop("com.twitter.android")



def report_account(d, account,action=0):
    # Open Twitter app
    if "com.twitter.android" in d.app_list_running():
        # Stop Twitter app
        d.app_stop("com.twitter.android")
        sleep(2)

    # Start the Twitter app 
    d.app_start("com.twitter.android")
    logging.info(f"{threading.current_thread().name}:{d.wlan_ip} :Opened Twitter!")
    sleep(15)

    if "com.twitter.android" in d.app_list_running():
        logging.info(f"{threading.current_thread().name}:{d.wlan_ip} Twitter is running!")

        
        if account != '':
            search_and_go_to_page(d, account)
        else:
            logging.info(f"{threading.current_thread().name}:{d.wlan_ip} didn't get link nor an account name. exiting the function..")
            return
        sleep(5)
        # Click on the share button
        d.click(667, 120)
        update_results_file("Actions")
        sleep(3)
        # Click on the report button
        x,y = search_sentence(d,"Report","twi")
        sleep(3)
        d.click(int(x), int(y))
        update_results_file("Actions")
        sleep(8)
        if action == 0: 
                handle_user_selection(d, report_twitter_clicks)
        else:
            execute_action(d,report_tiktok_account_keys[action-1], report_tiktok_account)
        sleep(20)
        update_results_file("Accounts reported")
        d.app_stop("com.twitter.android")



def support_accounts(d,accounts):
    random.shuffle(accounts)
    for account in accounts:
        # Start the Twitter app 
        if "com.twitter.android" in d.app_list_running():
            # Stop Twitter app
            d.app_stop("com.twitter.android")
            sleep(2)

        # Start the Twitter app 
        d.app_start("com.twitter.android")
        
        search_and_go_to_page(d,account)
        sleep(2)
        scroll_like_and_comment(d,5)
        # Stop Twitter app
        d.app_stop("com.twitter.android")
        sleep(2)


def main(d):
    """
    The main function connects to the Android device and performs various Twitter actions.
    """
    # Start the Twitter app 
    try:
        if "com.twitter.android" in d.app_list_running():
            # Stop Twitter app
            d.app_stop("com.twitter.android")
            sleep(2)

        # Start the Twitter app 
        d.app_start("com.twitter.android")
        logging.info(f"{threading.current_thread().name}:{d.wlan_ip} Opened Twitter!")
        sleep(12)  # Wait for Twitter to fully load
        d.click(75,1500) # Go to home
        update_results_file("Actions")
        for _ in range(random.randint(1,2)):
            scroll_random_number(d)
            sleep(4)
            # tap_like_button(d)   #don't use until fyp is pro israel
            sleep(2)

        # Stop Twitter app
        d.app_stop("com.twitter.android")
        sleep(2)

        for _ in range(5):
            account = random.choice(twitter_handles)
            while account.strip() == "israel" or account.strip() == "Israel":
                logging.ERROR(f"{threading.current_thread().name}:{d.wlan_ip} israel was choosen somehow!!")
                account = random.choice(twitter_handles)

            logging.info(f"{threading.current_thread().name}:{d.wlan_ip} The account is: {account}!")
            search_and_go_to_page(d, account)
            sleep(2)
            follow_page(d)
            sleep(2)
            scroll_like_and_comment(d,10)
            d.click(75,1500) # Go to home
            update_results_file("Actions")
            sleep(4)
            
            for _ in range(random.randint(1,2)):
                scroll_random_number(d)
                sleep(2)
                # tap_like_button(d)
                sleep(2)
                
            # Stop Twitter app
            d.app_stop("com.twitter.android")
            sleep(5)
        support_accounts(d,twitter_handles_specials)
        report_twitter_posts(d)
        # report_account(d,random.choice(anti_israel_twitter)) #TODO fix
        sleep(3)
        d.app_stop("com.twitter.android")
        sleep(4)
    except:
        logging.error("An error occurred", exc_info=True)  # Log error with stack trace
        d.app_stop("com.twitter.android")
# d = u2.connect("10.0.0.11")
# report_account(d,anti_israel_twitter[0],7)
