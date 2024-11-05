import threading
from time import sleep
import random
from common_area import *
import easyocr
from fuzzywuzzy import fuzz
import uiautomator2 as u2



def tap_like_button(d, like_button_template_path="icons/twitter_icons/like.png"):
    print(f"{threading.current_thread().name}:{d.wlan_ip} Starting tap_like_button function")
    
    screenshot_path = take_screenshot(d,threading.current_thread().name,"twi")
    
    best_cordinates = find_best_match(screenshot_path, like_button_template_path,d)    
    
    if best_cordinates:
        print(f"{threading.current_thread().name}:{d.wlan_ip} Like button found at {best_cordinates}, tapping...")
        d.click(int(best_cordinates[0]), int(best_cordinates[1]))
        print(f"{threading.current_thread().name}:{d.wlan_ip} Tapped best match at {best_cordinates}.")
        update_results_file("Likes")
    else:
        print(f"{threading.current_thread().name}:{d.wlan_ip} Like button not found on the screen.")
    
    print(f"{threading.current_thread().name}:{d.wlan_ip} Finished tap_like_button function")
    

def comment_text(d, text, comment_template_path="icons/twitter_icons/comment.png"):
    print(f"{threading.current_thread().name}:{d.wlan_ip} Starting comment_text function")
    screenshot_path = take_screenshot(d,threading.current_thread().name,"twi")
    best_match = find_best_match(screenshot_path, comment_template_path,d)
    if best_match:
        d.click(int(best_match[0]), int(best_match[1]))  # Unpack directly
        sleep(2)
        tap_keyboard(d,text) 
        sleep(1)
        update_results_file("Comments")
        sleep(1)
        d.click(600, 125)  # Click the post button
    else:
        print(f"{threading.current_thread().name}:{d.wlan_ip} Comment icon not found on the screen.")
    print(f"{threading.current_thread().name}:{d.wlan_ip} Finished comment_text function")

def tap_repost_button(d, repost_button_template_path="icons/twitter_icons/repost.png"):
    print(f"{threading.current_thread().name}:{d.wlan_ip} Starting tap_repost_button function")
    
    screenshot_path = take_screenshot(d,threading.current_thread().name,"twi")
    
    best_cordinates = find_best_match(screenshot_path, repost_button_template_path,d)    
    
    if best_cordinates:
        print(f"{threading.current_thread().name}:{d.wlan_ip} repost button found at {best_cordinates}, tapping...")
        d.click(int(best_cordinates[0]), int(best_cordinates[1]))
        print(f"{threading.current_thread().name}:{d.wlan_ip} Tapped best match at {best_cordinates}.")
        sleep(2)
        d.click(360,1370) # Tap repost button
        update_results_file("Reposts")
    else:
        print(f"{threading.current_thread().name}:{d.wlan_ip} reposts button not found on the screen.")
    
    print(f"{threading.current_thread().name}:{d.wlan_ip} Finished tap_reposts_button function")

def scroll_like_and_comment(d,posts):
    print(f"{threading.current_thread().name}:{d.wlan_ip} Starting scroll_like_and_comment function")
    actions = ['like', 'comment', 'both', 'none']
    for _ in range(posts):
        if d(scrollable=True).exists:
            start_x = random.randint(400, 600)
            start_y = random.randint(900, 1200)
            end_y = start_y - random.randint(400, 600)
            swipe_duration = random.uniform(0.04, 0.06)
            d.swipe(start_x, start_y, start_x, end_y, duration=swipe_duration)
            print(f"{threading.current_thread().name}:{d.wlan_ip} Scrolled from ({start_x}, {start_y}) to ({start_x}, {end_y}) in {swipe_duration:.2f} seconds.")
        else:
            print(f"{threading.current_thread().name}:{d.wlan_ip} No scrollable view found!")
        sleep(random.uniform(2, 14))
        action = random.choice(actions)
        print(f"{threading.current_thread().name}:{d.wlan_ip} Action chosen: {action}")
        text = random.choice(israel_support_comments)
        if action == 'like':
            tap_like_button(d)
            print(f"{threading.current_thread().name}:{d.wlan_ip} Liked the post.")

        elif action == 'comment':
            comment_text(d, text)
            print(f"{threading.current_thread().name}:{d.wlan_ip} Commented: {text}")

        elif action == 'both':
            tap_like_button(d)
            print(f"{threading.current_thread().name}:{d.wlan_ip} Liked the post.")
            sleep(2)
            comment_text(d, text)
            print(f"{threading.current_thread().name}:{d.wlan_ip} Commented: {text}")
            sleep(2)
            num = random.choice([1,2,3,4,5])
            if num==1:
                tap_repost_button(d)
        sleep(3)
    sleep(2)
    d.press("back")
    sleep(0.5)
    d.press("back")
    sleep(2)
    print(f"{threading.current_thread().name}:{d.wlan_ip} Finished scroll_like_and_comment function")


def scroll_random_number(d):
    """
    Scrolls down a random number of times between 1 and 3 and then scrolls up.

    Parameters:
    d (uiautomator2.Device): The connected device object from uiautomator2.
    """
    if d(scrollable=True).exists:
        print(f"{threading.current_thread().name}:{d.wlan_ip} Found a scrollable view! Swiping down...")

        # Randomly choose how many times to swipe (between 1 and 6)
        num_swipes = random.randint(1, 6)
        print(f"{threading.current_thread().name}:{d.wlan_ip} Number of swipes: {num_swipes}")

        # Perform the swipe action for the chosen number of times
        for _ in range(num_swipes):
            if d(scrollable=True).exists:
                start_x = random.randint(400, 600)
                start_y = random.randint(900, 1200)
                end_y = start_y - random.randint(400, 600)
                swipe_duration = random.uniform(0.04, 0.06)
                d.swipe(start_x, start_y, start_x, end_y, duration=swipe_duration)
                print(f"{threading.current_thread().name}:{d.wlan_ip} Scrolled from ({start_x}, {start_y}) to ({start_x}, {end_y}) in {swipe_duration:.2f} seconds.")
            else:
                print(f"{threading.current_thread().name}: No scrollable view found!")
                d.click(40,1340)
            sleep(random.randint(2, 10))
    else:
        print(f"{threading.current_thread().name}:{d.wlan_ip} No scrollable view found!")


def search_and_go_to_page(d, page_name):
    """
    Searches for the specified text in Twitter and navigates to the desired page.

    Parameters:
    d (uiautomator2.Device): The connected device object from uiautomator2.
    text (str): The text to search for.
    """
    # Swipe up to return to the previous content
    d.swipe(500, 300, 500, 1000, duration = 0.05)
    sleep(3)
    # Perform the search
    d.click(180, 1500)
    print(f"{threading.current_thread().name}:{d.wlan_ip} Clicked on the search button.")
    sleep(3)
    # Click on the search input field
    d.click(360, 140)
    sleep(3)
     # Type each character of the search term with a random delay to simulate human typing
    tap_keyboard(d,page_name)
    sleep(4)
    print(f"{threading.current_thread().name}:{d.wlan_ip} Typed '{page_name}' in the search bar naturally.")
    try:
        x,y = search_sentence(d,"@"+page_name)
        d.click(int(x),int(y))
    except:
        print("Didnt find page!")
    
    print(f"{threading.current_thread().name}:{d.wlan_ip} Got into the page!")
    sleep(5)

def follow_page(d, follow_template_path="icons/twitter_icons/follow.png"):
    print(f"{threading.current_thread().name}:{d.wlan_ip} Starting follow_page function")
    screenshot_path = take_screenshot(d,threading.current_thread().name,"twi")
    best_match = find_best_match(screenshot_path, follow_template_path,d)
    if best_match:
        num = random.choice([1, 2])
        if  num == 1:
            d.click(int(best_match[0]), int(best_match[1]))
            print(f"{threading.current_thread().name}:{d.wlan_ip} Followed account!")
            update_results_file("Follows")
            sleep(1)
        else:
            print(f"{threading.current_thread().name}:{d.wlan_ip} didn't followed account!")
        sleep(2)
    else:
        print(f"{threading.current_thread().name}:{d.wlan_ip} Follow icon not found on the screen.")
    print(f"{threading.current_thread().name}:{d.wlan_ip} Finished follow_page function")





def search_sentence(d, name, tolerance=20):
    screen_shot = take_screenshot(d, threading.current_thread().name, "twi")
    print(f"Searching for name: {name}")
    
    # Initialize the OCR reader
    reader = easyocr.Reader(['en'])  # You can add more languages if needed

    # Perform OCR
    result = reader.readtext(screen_shot, detail=1)  # detail=1 provides bounding box and text

    best_match = None
    best_similarity = 0  # Initialize with the lowest possible score (0%)

    # Ensure both name and detected text retain special characters like '@'
    processed_name = name.strip()  # Keep special characters, but strip unnecessary spaces

    # Iterate over detected texts
    for detection in result:
        bbox, text, _ = detection
        top_left, _, bottom_right, _ = bbox

        # Skip any detected text that is above y=200
        if top_left[1] < 180:
            continue  # Ignore this text since it's above the desired y position

        # Keep special characters in the detected text
        processed_text = text.strip()
        if "Go to" in processed_text:
            processed_text = processed_text.replace("Go to",'')
        # Compare using fuzzy matching
        similarity_score = fuzz.ratio(processed_name, processed_text)
        # Check if the similarity score is the highest and within tolerance
        if similarity_score > best_similarity and similarity_score >= (100 - tolerance):
            best_similarity = similarity_score
            best_match = bbox

    if best_match:
        # Bounding box gives four points (top-left, top-right, bottom-right, bottom-left)
        top_left, _, bottom_right, _ = best_match

        # Calculate the center position of the bounding box
        center_x = (top_left[0] + bottom_right[0]) // 2
        center_y = (top_left[1] + bottom_right[1]) // 2
        return (center_x, center_y)

    print("No sufficiently similar text was found.")
    return None


def report_post(d, link,action = 0):
    # Open Twitter app
    d.app_start("com.twitter.android")
    print(f"{threading.current_thread().name}:{d.wlan_ip} :Opened Twitter!")
    sleep(10)

    if "com.twitter.android" in d.app_list_running():
        print(f"{threading.current_thread().name}:{d.wlan_ip} Twitter is running!")
        # Open the tweet in the Twitter app
        d.shell(f"am start -a android.intent.action.VIEW -d '{link}'")
        print(f"{threading.current_thread().name}:{d.wlan_ip} Opened tweet: {link}")
        sleep(3)
        # Click on the share button
        d.click(685, 210)
        sleep(3)
        # Click on the report button
        x,y = search_sentence(d,"Report post")
        sleep(3)
        d.click(int(x), int(y))
        sleep(15)
        if action == 0: 
            handle_user_selection(d,report_twitter_clicks)
        else:
            execute_action(d,twitter_report_keys[action-1],report_twitter_clicks)
        update_results_file("Posts reported")
        d.app_stop("com.twitter.android")


def report_account(d, link):
    # Open Twitter app
    d.app_start("com.twitter.android")
    print(f"{threading.current_thread().name}:{d.wlan_ip} :Opened Twitter!")
    sleep(15)

    if "com.twitter.android" in d.app_list_running():
        print(f"{threading.current_thread().name}:{d.wlan_ip} Twitter is running!")

        # Open the tweet in the Twitter app
        d.shell(f"am start -a android.intent.action.VIEW -d '{link}'")
        print(f"{threading.current_thread().name}:{d.wlan_ip} Opened account: {link}")
        sleep(3)
        # Click on the share button
        d.click(667, 120)
        sleep(3)
        # Click on the report button
        x,y = search_sentence(d,"Report")
        sleep(3)
        d.click(int(x), int(y))
        sleep(8)
        handle_user_selection(d,report_twitter_clicks)
        sleep(4)
        update_results_file("Accounts reported")
        d.app_stop("com.twitter.android")



def support_accounts(d,accounts):
    random.shuffle(accounts)
    for account in accounts:
        search_and_go_to_page(d,account)
        sleep(2)
        scroll_like_and_comment(d,5)


def main(d):
    """
    The main function connects to the Android device and performs various Twitter actions.
    """
    # Start the Twitter app
    d.app_start("com.twitter.android")
    print(f"{threading.current_thread().name}:{d.wlan_ip} Opened Twitter!")
    sleep(12)  # Wait for Twitter to fully load
    d.click(75,1500) # Go to home
    for _ in range(random.randint(4,10)):
        scroll_random_number(d)
        sleep(4)
        # tap_like_button(d)
        sleep(2)
    sleep(2)
    for _ in range(1):
        search_and_go_to_page(d, random.choice(twitter_handles))
        sleep(2)
        follow_page(d)
        sleep(2)
        # Perform scrolling and liking of tweets
        scroll_like_and_comment(d,20)
        d.click(75,1500) # Go to home
        sleep(4)
        for _ in range(random.randint(1,12)):
            scroll_random_number(d)
            sleep(2)
            # tap_like_button(d)
            sleep(2)
        sleep(5)
    support_accounts(d,twitter_handles_specials)
    sleep(3)
    d.app_stop("com.twitter.android")
    sleep(4)
# d = u2.connect("10.0.0.6")
# tap_repost_button(d)
# report_post(d,"https://x.com/marwanbishara/status/1805202165054493148?t=zbQJshyDikFcHUFcMKC1yg&s=19")
# report_account(d,"https://x.com/marwanbishara?t=Ut7owo1yPl0b9VSvGGI4cQ&s=08")

