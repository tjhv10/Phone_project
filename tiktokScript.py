from time import sleep
import random
import threading
from common_area import *
import uiautomator2 as u2
from twitterScript import search_sentence


def tap_users(d, users_template_path="icons/tiktok_icons/users.png"):
    """
    Takes a screenshot and tries to tap on the like button if found.
    """
    screenshot_path = take_screenshot(d,threading.current_thread().name,"tik")
    best_coordinates = find_best_match(screenshot_path, users_template_path,d)
    if best_coordinates:
        d.click(int(best_coordinates[0]), int(best_coordinates[1]))
        update_results_file("Actions")
    else:
        d.click(196,213)
        update_results_file("Actions")
        print(f"{threading.current_thread().name}:{d.wlan_ip} Users button not found on the screen.")
   

def search(d, text):
    """
    Searches for a specific user on TikTok by simulating clicks and typing.
    """
    screen_width = d.info['displayWidth']
    screen_height = d.info['displayHeight']
    
    x = screen_width * (650 / 720)
    y = screen_height * (100 / 1560)

    
    d.click(x, y)  # Click on the search bar
    update_results_file("Actions")
    sleep(4)
    tap_keyboard(d,text)
    sleep(5)
    d.press(66)  # Press the search button
    update_results_file("Actions")
    sleep(10)

    tap_users(d)  # Click to go to users
    sleep(8)

    d.click(350, 300)  # Click to go into the first result
    update_results_file("Actions")
    sleep(4)
    
        

def tap_like_button(d, like_button_template_path="icons/tiktok_icons/like.png"):
    print(f"{threading.current_thread().name}:{d.wlan_ip} Starting tap_like_button function")
    screenshot_path = take_screenshot(d,threading.current_thread().name,"tik")
    sleep(2)
    best_coordinates = find_best_match(screenshot_path, like_button_template_path,d)
    sleep(2)
    if best_coordinates:
        print(f"{threading.current_thread().name}:{d.wlan_ip} Like button found at {best_coordinates}, tapping...")
        d.click(int(best_coordinates[0]), int(best_coordinates[1]))
        update_results_file("Actions")
        print(f"{threading.current_thread().name}:{d.wlan_ip} Tapped best match at {best_coordinates}.")
        update_results_file("Likes")
        sleep(1)
    else:
        print(f"{threading.current_thread().name}:{d.wlan_ip} Like button not found on the screen.")
    print(f"{threading.current_thread().name}:{d.wlan_ip} Finished tap_like_button function")

def comment_text(d, text,send_button_template_path="icons/tiktok_icons/send.png"):
    """
    Comments on a post using the regular keyboard.
    """
    d.click(670, 1000)  # Click on the comment button
    update_results_file("Actions")
    print(f"{threading.current_thread().name}:{d.wlan_ip} Clicked on the comment button.")
    sleep(3)
    d.click(310, 1500)  # Click on the comment input field
    update_results_file("Actions")
    print(f"{threading.current_thread().name}:{d.wlan_ip} Commenting: {text}")
    
    sleep(4)  # Wait for the input field to be ready
    
    tap_keyboard(d,text)
    
    sleep(2)  # Give some time for the input to be registered
    screenshot_path = take_screenshot(d,threading.current_thread().name,"tik")
    sleep(2)
    best_coordinates = find_best_match(screenshot_path, send_button_template_path,d)
    sleep(2)
    if best_coordinates:
        print(f"{threading.current_thread().name}:{d.wlan_ip} Send button found at {best_coordinates}, tapping...")
        d.click(int(best_coordinates[0]), int(best_coordinates[1]))
        update_results_file("Actions")
        print(f"{threading.current_thread().name}:{d.wlan_ip} Tapped best match at {best_coordinates}.")
        sleep(1)
        update_results_file("Comments")
        sleep(1)
    else:
        print(f"{threading.current_thread().name}:{d.wlan_ip} Send button not found on the screen.")
      # Click the submit button for the comment
    print(f"{threading.current_thread().name}:{d.wlan_ip} Comment submitted.")
    sleep(3)
    d.press("back")
    update_results_file("Actions")

def scroll_random_number(d):
    """
    Scrolls down a random number of times in a scrollable view.
    """
    screen_width = d.info['displayWidth']
    screen_height = d.info['displayHeight']
    
    if d(scrollable=True).exists:
        print(f"{threading.current_thread().name}:{d.wlan_ip} Found a scrollable view! Swiping down...")
        num_swipes = random.randint(1, 2)
        print(f"{threading.current_thread().name}:{d.wlan_ip} Number of swipes: {num_swipes}")

        for i in range(num_swipes):
            x_start = screen_width * (500 / 720)
            y_start = screen_height * (1200 / 1560)
            x_end = screen_width * (500 / 720)
            y_end = screen_height * (300 / 1560)
            d.swipe(x_start, y_start, x_end, y_end, duration=0.05)
            update_results_file("Actions")
            random_time = random.randint(2, 15)
            sleep(random_time)
            print(f"{threading.current_thread().name}:{d.wlan_ip} Swiped down {i + 1} time(s).")
    else:
        print(f"{threading.current_thread().name}:{d.wlan_ip} No scrollable view found!")


def scroll_like_and_comment(d):
    """
    Scrolls the view and likes posts.
    """
    tap_like_button(d)
    screen_width = d.info['displayWidth']
    screen_height = d.info['displayHeight']

    for i in range(2):
        if d(scrollable=True).exists:
            x_start = screen_width * (500 / 720)
            y_start = screen_height * (1200 / 1560)
            x_end = screen_width * (500 / 720)
            y_end = screen_height * (300 / 1560)
            d.swipe(x_start, y_start, x_end, y_end, duration=0.05)
            update_results_file("Actions")
            random_time = random.randint(2, 15)
            sleep(random_time)
            print(f"{threading.current_thread().name}:{d.wlan_ip} Swiped down {i + 1} time(s).")
        else:
            print(f"{threading.current_thread().name}:{d.wlan_ip} No scrollable view found!")
        num = random.choice([1, 2, 3, 4, 5])
        if  num <= 2:
            print(f"{threading.current_thread().name}:{d.wlan_ip} like")
            tap_like_button(d)
            sleep(1)
        elif num>2 and num<=4:
            print(f"{threading.current_thread().name}:{d.wlan_ip} like and comment")
            tap_like_button(d)
            sleep(2)
            comment_text(d,random.choice(israel_support_comments))
            sleep(1)
        else:
            print(f"{threading.current_thread().name}:{d.wlan_ip} none")
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
    d.click(120, 1450) # Get in the first page
    update_results_file("Actions")
    sleep(5)
    scroll_like_and_comment(d)


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
    print(f"{threading.current_thread().name}:{d.wlan_ip} : Opened TikTok!")
    # sleep(15)

    if "com.zhiliaoapp.musically" in d.app_list_running():
        print(f"{threading.current_thread().name}:{d.wlan_ip} TikTok is running!")
        d.shell(f"am start -a android.intent.action.VIEW -d {link}")
        print(f"{threading.current_thread().name}:{d.wlan_ip} Opened link: {link}")
        sleep(2)
            
        try:   
            # Find and click the "Watch only" button
            x, y = search_sentence(d, "Watch only")
            d.click(int(x), int(y))
            update_results_file("Actions")
            sleep(7)
            
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
                print(report_tiktok_clicks[report_tiktok_keys[action - 1]])
                execute_action(d, report_tiktok_keys[action - 1], report_tiktok_clicks)
            
            sleep(4)
            update_results_file("Posts reported")
        
            # Stop TikTok app
            d.app_stop("com.zhiliaoapp.musically")

        except Exception as e:
            print(f"{threading.current_thread().name}:{d.wlan_ip} already reported that post.")

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
    print(f"{threading.current_thread().name}:{d.wlan_ip} : Opened TikTok!")

    # Wait to make sure TikTok fully loads
    sleep(15)

    # Check if TikTok is running
    if "com.zhiliaoapp.musically" in d.app_list_running():
        print(f"{threading.current_thread().name}:{d.wlan_ip} TikTok is running!")

        # Open link with TikTok
        d.shell(f"am start -n com.zhiliaoapp.musically/.MainActivity -a android.intent.action.VIEW -d {link}")
        print(f"{threading.current_thread().name}:{d.wlan_ip} Opened link: {link}")

        # Give some time to load the page within TikTok
        sleep(8)

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
            print(f"{threading.current_thread().name}:{d.wlan_ip} : Stopped TikTok.")


def support_accounts(d,accounts):
    accounts = random.shuffle(accounts)
    for account in accounts:
        if "com.zhiliaoapp.musically" in d.app_list_running():
            # Stop Tiktok app
            d.app_stop("com.zhiliaoapp.musically")
            sleep(4)

        # Start the Twitter app 
        d.app_start("com.zhiliaoapp.musically")  # Open TikTok app
        print(f"{threading.current_thread().name}:{d.wlan_ip} :Opened TikTok!")
        sleep(15)
        search(d,account)
        sleep(2)
        scroll_like_and_comment(d,5)
        d.app_stop("com.zhiliaoapp.musically")
        sleep(4)


def main(d):
    """
    Main function to connect to the device and perform actions on TikTok.
    # """
    # d.app_start("com.zhiliaoapp.musicallyy")  # Open TikTok app
    # print(f"{threading.current_thread().name}:{d.wlan_ip} :Opened TikTok!")
    # sleep(15)
    # if "com.zhiliaoapp.musically" in d.app_list_running():
    #     print(f"{threading.current_thread().name}:{d.wlan_ip} TikTok is running!")
    for _ in range(10):
        if "com.zhiliaoapp.musically" in d.app_list_running():
            # Stop Tiktok app
            d.app_stop("com.zhiliaoapp.musically")
            sleep(4)

        # Start the Twitter app 
        d.app_start("com.zhiliaoapp.musically")  # Open TikTok app
        print(f"{threading.current_thread().name}:{d.wlan_ip} :Opened TikTok!")
        sleep(15)
        scroll_random_number(d)
        # sleep(1)
        # tap_like_button(d)
        sleep(4)
        like_a_page(d,random.choice(tiktok_accounts))
        scroll_random_number(d)
        sleep(10)

    support_accounts(d,tiktok_handles_specials)
    report_tiktok_posts(d)
    sleep(3)
    d.app_stop("com.zhiliaoapp.musically")
    sleep(4)
    # else:
    #     print(f"{threading.current_thread().name}:{d.wlan_ip} TikTok is not running!")
    print(f"{threading.current_thread().name}:{d.wlan_ip} done")
    
        
    # Sleep for 0.5 hours before the next cycle
    print(f"{threading.current_thread().name}:{d.wlan_ip} completed its tasks. Sleeping for 0.5 hours...")
    sleep(.5 * 3600)  # 0.5 hours break for this worker


# d = u2.connect("10.0.0.21")
# for handle in tiktok_accounts:
#     like_a_page(d, handle)
# d = u2.connect("10.0.0.15")
# report_post(d,"https://vt.tiktok.com/ZSjFJUTw5/")
