import threading
from time import sleep
import random
from common_area_items import *
from common_area_functions import *



def tap_like_button(d, like_button_template_path="icons/twitter_icons/like.png"):
    logging.info(f"{threading.current_thread().name}:{d.serial} Starting tap_like_button function")
    
    screenshot_path = take_screenshot(d,threading.current_thread().name,"twi")
    
    best_cordinates = find_best_match(screenshot_path, like_button_template_path,d)    
    
    if best_cordinates:
        logging.info(f"{threading.current_thread().name}:{d.serial} Like button found at {best_cordinates}, tapping...")
        d.click(int(best_cordinates[0]), int(best_cordinates[1]))
        update_results_file("Actions")
        logging.info(f"{threading.current_thread().name}:{d.serial} Tapped best match at {best_cordinates}.")
        update_results_file("Likes")
    else:
        logging.info(f"{threading.current_thread().name}:{d.serial} Like button not found on the screen.")
    
    logging.info(f"{threading.current_thread().name}:{d.serial} Finished tap_like_button function")
    

def comment_text(d, text, comment_template_path="icons/twitter_icons/comment.png"):
    logging.info(f"{threading.current_thread().name}:{d.serial} Starting comment_text function")
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
        result = search_sentence(d,"2123","twi", tolerance=26) # For post location message
        if not result:
            d.click(int(350),int(350))
            sleep(5)
        type_keyboard(d,text) 
        sleep(1)
        logging.info(f"{threading.current_thread().name}:{d.serial} Searching for: {text}")
        if search_sentence(d,text[:29],"twi"):
            update_results_file("Comments")
            sleep(1)
            d.click(600, 125)  # Click the post button
            update_results_file("Actions")
            logging.info(f"{threading.current_thread().name}:{d.serial} Commented: {text}")
        else:
            logging.info(f"{threading.current_thread().name}:{d.serial} Comment is deprecated, canceling.")
            d.click(60,130)
            update_results_file("Actions")
            sleep(3)
            d.click(430,920)
            update_results_file("Actions")
            logging.info(f"{threading.current_thread().name}:{d.serial} Got out of deprecated comment.")
    else:
        logging.info(f"{threading.current_thread().name}:{d.serial} Comment icon not found on the screen.")
        
    logging.info(f"{threading.current_thread().name}:{d.serial} Finished comment_text function")
        

def tap_repost_button(d, repost_button_template_path="icons/twitter_icons/repost.png"):
    logging.info(f"{threading.current_thread().name}:{d.serial} Starting tap_repost_button function")
    
    screenshot_path = take_screenshot(d,threading.current_thread().name,"twi")
    
    best_cordinates = find_best_match(screenshot_path, repost_button_template_path,d)    
    
    if best_cordinates:
        logging.info(f"{threading.current_thread().name}:{d.serial} repost button found at {best_cordinates}, tapping...")
        d.click(int(best_cordinates[0]), int(best_cordinates[1]))
        update_results_file("Actions")
        logging.info(f"{threading.current_thread().name}:{d.serial} Tapped best match at {best_cordinates}.")
        sleep(2)
        d.click(360,1370) # Tap repost button
        update_results_file("Actions")
        update_results_file("Reposts")
    else:
        logging.info(f"{threading.current_thread().name}:{d.serial} reposts button not found on the screen.")
    
    logging.info(f"{threading.current_thread().name}:{d.serial} Finished tap_reposts_button function")

def scroll_like_and_comment(d,posts,duration):
    logging.info(f"{threading.current_thread().name}:{d.serial} Starting scroll_like_and_comment function")
    logging.info(f"{threading.current_thread().name}:{d.serial} duration in main :"+str(duration))
    start_time = time.time()
    actions = ['none', 'none', 'none','none','none','none']
    for _ in range(posts):
        if d(scrollable=True).exists:
            start_x = random.randint(400, 600)
            start_y = random.randint(900, 1200)
            end_y = start_y - random.randint(400, 600)
            swipe_duration = random.uniform(0.04, 0.06)
            arch_swipe(d, *swipe_function_param)
            update_results_file("Actions")
            logging.info(f"{threading.current_thread().name}:{d.serial} Scrolled from ({start_x}, {start_y}) to ({start_x}, {end_y}) in {swipe_duration:.2f} seconds.")
        else:
            logging.info(f"{threading.current_thread().name}:{d.serial} No scrollable view found!")
            try:
                d.click(*search_sentence(d,"Got it","twi"))
            except:
                if TYPE == 'v':
                    restart_device(d)
                    sleep(5)
                scroll_like_comment_main(d,duration+time.time()-start_time)
                return
        sleep(random.uniform(5, 30))
        action = random.choice(actions)
        logging.info(f"{threading.current_thread().name}:{d.serial} Action chosen: {action}")
        text = random.choice(israel_support_comments)
        if action == 'like':
            tap_like_button(d)
            logging.info(f"{threading.current_thread().name}:{d.serial} Liked the post.")

        elif action == 'both':
            tap_like_button(d)
            logging.info(f"{threading.current_thread().name}:{d.serial} Liked the post.")
            sleep(2)
            sleep(2)
            num = random.choice([1,2,3,4,5])
            if num==3:
                comment_text(d, text)
                logging.info(f"{threading.current_thread().name}:{d.serial} Commented: {text}")
                tap_repost_button(d)
                logging.info(f"{threading.current_thread().name}:{d.serial} Reposted.")
            elif num<=2:
                comment_text(d, text)
                logging.info(f"{threading.current_thread().name}:{d.serial} Commented: {text}")
        
        sleep(3)
    sleep(2)
    d.press("back")
    sleep(0.5)
    d.press("back")
    sleep(2)
    logging.info(f"{threading.current_thread().name}:{d.serial} Finished scroll_like_and_comment function")


def scroll_random_number(d,duration):
    """
    Scrolls down a random number of times between 1 and 3 and then scrolls up.

    Parameters:
    d (uiautomator2.Device): The connected device object from uiautomator2.
    """
    start_time = time.time()
    if d(scrollable=True).exists:
        logging.info(f"{threading.current_thread().name}:{d.serial} Found a scrollable view! Swiping down...")

        # Randomly choose how many times to swipe (between 1 and 6)
        num_swipes = random.randint(1, 6)
        logging.info(f"{threading.current_thread().name}:{d.serial} Number of swipes: {num_swipes}")



        # Perform the swipe action for the chosen number of times
        for _ in range(num_swipes):
            if d(scrollable=True).exists:
                start_x = random.randint(400, 600)
                start_y = random.randint(900, 1200)
                end_y = start_y - random.randint(400, 600)
                swipe_duration = random.uniform(0.04, 0.06)
                arch_swipe(d, *swipe_function_param)
                update_results_file("Actions")
                logging.info(f"{threading.current_thread().name}:{d.serial} Scrolled from ({start_x}, {start_y}) to ({start_x}, {end_y}) in {swipe_duration:.2f} seconds.")
            else:
                
                logging.info(f"{threading.current_thread().name}:{d.serial} No scrollable view found!")
                update_results_file("Actions")
                try:
                    d.click(*search_sentence(d,"Got it","twi"))
                except:
                    if TYPE == 'v':
                        restart_device(d)
                        sleep(5)
                    scroll_like_comment_main(d,duration+time.time()-start_time)
                    return
            sleep(random.randint(2, 30))
    else:
        logging.info(f"{threading.current_thread().name}:{d.serial} No scrollable view found!")
        try:
            d.click(*search_sentence(d,"Got it","twi"))
        except:
            if TYPE == 'v':
                restart_device(d)
                sleep(5)
            scroll_like_comment_main(d,duration+time.time()-start_time)
            return
        


def search_and_go_to_page(d, page_name,duration=0):
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
    logging.info(f"{threading.current_thread().name}:{d.serial} : Opened Twitter!")
    sleep(10)
    update_results_file("Actions")
    sleep(3)
    # Perform the search
    d.click(180, 1500)
    update_results_file("Actions")
    logging.info(f"{threading.current_thread().name}:{d.serial} Clicked on the search button.")
    logging.info(f"{threading.current_thread().name}:{d.serial} serching for {page_name}.")
    sleep(3)
    # Click on the search input field
    d.click(360, 140)
    update_results_file("Actions")
    sleep(10)
     # Type each character of the search term with a random delay to simulate human typing
    type_keyboard(d,page_name)
    sleep(15)
    logging.info(f"{threading.current_thread().name}:{d.serial} Typed '{page_name}' in the search bar naturally.")
    try:
        x,y = search_sentence(d,"@"+page_name,"twi",y_min=180)
        d.click(int(x),int(y))
        update_results_file("Actions")
    except:
        try:
            x,y = search_sentence(d,"@"+page_name.lower(),"twi",y_min=180)
            d.click(int(x),int(y))
            update_results_file("Actions")
        except:
            if duration > MAX_DURATION_TWITTER:  # Check duration
                return
            logging.warning(f"{threading.current_thread().name}:{d.serial} Didnt find '{page_name}' checking vpn and restarting.")
            close_apps(d)
            sleep(5)
            if TYPE=='p':
                open_vpn(d)
            else:
                logging.warning(f"{threading.current_thread().name}:{d.serial} restarting...")
                restart_device(d)
                sleep(15)
            sleep(5)
            search_and_go_to_page(d,page_name,duration)
    
    logging.info(f"{threading.current_thread().name}:{d.serial} Got into the page!")
    sleep(5)

def follow_page(d, follow_template_path="icons/twitter_icons/follow.png"):
    logging.info(f"{threading.current_thread().name}:{d.serial} Starting follow_page function")
    screenshot_path = take_screenshot(d,threading.current_thread().name,"twi")
    best_match = find_best_match(screenshot_path, follow_template_path,d)
    if best_match:
        num = random.choice([2, 2]) #TODO change to 4,20
        if  num == 1:
            d.click(int(best_match[0]), int(best_match[1]))
            update_results_file("Actions")
            logging.info(f"{threading.current_thread().name}:{d.serial} Followed account!")
            update_results_file("Follows")
            sleep(1)
        else:
            logging.info(f"{threading.current_thread().name}:{d.serial} didn't followed account!")
            
        sleep(2)
    else:
        logging.info(f"{threading.current_thread().name}:{d.serial} Follow icon not found on the screen.")
    logging.info(f"{threading.current_thread().name}:{d.serial} Finished follow_page function")
        
        
def report_post(d):
    return #TODO remove this line
    # Open Twitter app
    link,action = random.choice(get_links_and_reasons_from_non_red_cells("Posts to report _ ARISE.xlsx", "Sheet1", "C", "D"))
    if "com.twitter.android" in d.app_list_running():
        # Stop Twitter app
        d.app_stop("com.twitter.android")
        sleep(2)
        

    # Start the Twitter app 
    d.app_start("com.twitter.android")
    logging.info(f"{threading.current_thread().name}:{d.serial} : Opened Twitter!")
    sleep(10)

    if "com.twitter.android" in d.app_list_running():
        logging.info(f"{threading.current_thread().name}:{d.serial} Twitter is running!")
        logging.info(f"{threading.current_thread().name}:{d.serial} Going to link {link}")
        # Open the tweet in the Twitter app
        d.shell(f"am start -a android.intent.action.VIEW -d '{link}'")
        logging.info(f"{threading.current_thread().name}:{d.serial} Opened tweet: {link}")
        sleep(10)
            
        try:
            # Click on the share button
            d.click(685, 210)
            update_results_file("Actions")
            sleep(3)
            if search_sentence(d, "you reported this post.","twi"):
                logging.info(f"{threading.current_thread().name}:{d.serial} already reported this tweet.")
                return 
            d.click(*search_sentence(d, "Report post","twi"))
            update_results_file("Actions")
            sleep(15)
            retry_count = 0
            while not search_sentence(d,"What type of issue are","twi") and retry_count < 3:
                logging.info(f"{threading.current_thread().name}:{d.serial} Waiting for report page to load... Attempt {retry_count + 1}")
                sleep(10)
                retry_count += 1

            if retry_count == 3:
                logging.warning(f"{threading.current_thread().name}:{d.serial} Report page did not load after 3 attempts. Restarting VPN...")
                close_apps(d)
                sleep(5)
                if TYPE == 'p':
                    open_vpn(d)
                else:
                    restart_device(d)
                    sleep(15)
                sleep(5)
                report_post(d)

            if action == 0: 
                handle_user_selection(d, report_twitter_clicks)
            else:
                execute_action(d, twitter_report_keys[action-1], report_twitter_clicks)
            
            update_results_file("Posts reported")
        
            # Stop Twitter app
            d.app_stop("com.twitter.android")

        except Exception as e:
            logging.info(f"{threading.current_thread().name}:{d.serial} already reported that post.")
            # Stop Twitter app
            d.app_stop("com.twitter.android")



def report_account(d):
    return #TODO remove this line
    account = random.choice(anti_israel_twitter)
    action = 5
    # Open Twitter app
    if "com.twitter.android" in d.app_list_running():
        # Stop Twitter app
        d.app_stop("com.twitter.android")
        sleep(2)
    logging.info(f"{threading.current_thread().name}:{d.serial} Twitter is running!")
    search_and_go_to_page(d,account)
    sleep(5)
    # Click on the share button
    d.click(667, 120)
    update_results_file("Actions")
    sleep(3)
    # Click on the report button
    try:
        x,y = search_sentence(d,"Report","twi")
        sleep(3)
        d.click(int(x), int(y))
        update_results_file("Actions")
        retry_count = 0
        sleep(10)
        while not search_sentence(d,"What type of issue are","twi") and retry_count < 3:
            logging.info(f"{threading.current_thread().name}:{d.serial} Waiting for report page to load... Attempt {retry_count + 1}")
            sleep(10)
            retry_count += 1

            if retry_count == 3:
                logging.warning(f"{threading.current_thread().name}:{d.serial} Report page did not load after 3 attempts. Restarting VPN...")
                close_apps(d)
                sleep(5)
                if TYPE == 'p':
                    open_vpn(d)
                else:
                    restart_device(d)
                    sleep(15)
                sleep(5)
                report_account(d)        
        if action == 0: 
            handle_user_selection(d, report_twitter_clicks)
        else:
            execute_action(d,twitter_report_keys[action-1], report_twitter_clicks)
        sleep(10)
        update_results_file("Accounts reported")
        d.app_stop("com.twitter.android")
    except:
        logging.error(f"{threading.current_thread().name}:{d.serial} Report button not found!!")
        return


def support_accounts(d):
    random.shuffle(twitter_handles_specials)
    for account in twitter_handles_specials:
        # Start the Twitter app 
        if "com.twitter.android" in d.app_list_running():
            # Stop Twitter app
            d.app_stop("com.twitter.android")
            sleep(2)

        # Start the Twitter app 
        d.app_start("com.twitter.android")
        
        search_and_go_to_page(d,account)
        sleep(2)
        scroll_like_and_comment(d,5,0)
        # Stop Twitter app
        d.app_stop("com.twitter.android")
        sleep(2)

def scroll_like_comment_main(d,duration=0):    
    logging.info(f"{threading.current_thread().name}:{d.serial} duration in main: "+str(duration))
    start_time = time.time()
    duration = duration+time.time()-start_time
    if duration > MAX_DURATION_TWITTER:  # Check duration
        logging.info(f"{threading.current_thread().name}:{d.serial} Exceeded max duration {duration}. Exiting...")
        return  
    # Check if Twitter is running and stop it
    if "com.twitter.android" in d.app_list_running():
        d.app_stop("com.twitter.android")
        sleep(2)

    # Start Twitter
    d.app_start("com.twitter.android")
    logging.info(f"{threading.current_thread().name}:{d.serial} Opened Twitter!")
    sleep(12)  # Wait for Twitter to fully load
    d.click(75, 1500)  # Go to home
    update_results_file("Actions")
    sleep(2)
    duration = duration+time.time()-start_time
    logging.info(f"{threading.current_thread().name}:{d.serial} duration in main:" +str(duration))
    # Perform random scrolling actions
    for _ in range(random.randint(1,5)):
        duration = duration+time.time()-start_time
        if duration > MAX_DURATION_TWITTER:  # Check duration
            logging.info(f"{threading.current_thread().name}:{d.serial} Exceeded max duration {duration}. Exiting...")
            return
        scroll_random_number(d,duration+time.time()-start_time)
        sleep(4)

    # Stop Twitter
    d.app_stop("com.twitter.android")
    sleep(2)
    
    # Interact with accounts
    for _ in range(5):
        if search_sentence(d,"X isn't responding","twi", tolerance=30):
            d.click(search_sentence(d,"Close app","twi", tolerance=30))
            sleep(5)
        duration = duration+time.time()-start_time
        logging.info(f"{threading.current_thread().name}:{d.serial} duration in main:"+str(duration))
        if duration > MAX_DURATION_TWITTER:  # Check duration
            logging.info(f"{threading.current_thread().name}:{d.serial} Exceeded max duration {duration}. Exiting...")
            d.app_stop("com.twitter.android")
            return

        account = random.choice(twitter_handles)
        while account.strip().lower() == "israel":
            logging.error(f"{threading.current_thread().name}:{d.serial} 'israel' was chosen somehow!")
            account = random.choice(twitter_handles)

        logging.info(f"{threading.current_thread().name}:{d.serial} The account is: {account}!")
        search_and_go_to_page(d, account,duration)
        duration = duration+time.time()-start_time
        if duration > MAX_DURATION_TWITTER:  # Check duration
            logging.info(f"{threading.current_thread().name}:{d.serial} Exceeded max duration {duration}. Exiting...")
            d.app_stop("com.twitter.android")
            return
        sleep(2)
        follow_page(d)
        duration = duration+time.time()-start_time
        if duration > MAX_DURATION_TWITTER:  # Check duration
            logging.info(f"{threading.current_thread().name}:{d.serial} Exceeded max duration {duration}. Exiting...")
            d.app_stop("com.twitter.android")
            return
        sleep(2)
        scroll_like_and_comment(d, 15,duration=duration+time.time()-start_time)
        duration = duration+time.time()-start_time
        if duration > MAX_DURATION_TWITTER:  # Check duration
            logging.info(f"{threading.current_thread().name}:{d.serial} Exceeded max duration {duration}. Exiting...")
            d.app_stop("com.twitter.android")
            return
        d.click(75, 1500)  # Go to home
        update_results_file("Actions")
        sleep(4)

        for _ in range(random.randint(5, 15)):
            scroll_random_number(d,duration+time.time()-start_time)
            sleep(2)

def main(d):
    """
    The main function connects to the Android device and performs various Twitter actions.
    
    Parameters:
    d (uiautomator2.Device): The connected Android device object.
    """
    try:
        functions = [scroll_like_comment_main, support_accounts, report_post, report_account]
        random.shuffle(functions)
        for action in functions:
            action(d)
            sleep(3)
    except Exception:
        logging.error("An error occurred", exc_info=True)
        d.app_stop("com.twitter.android")



# d = u2.connect("127.0.0.1:6555")
# main(d)
# report_account(d)
# report_post(d)
# restart_device(d)