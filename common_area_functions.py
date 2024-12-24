import logging
import random
import threading
from time import sleep
import cv2
import easyocr
from fuzzywuzzy import fuzz
import numpy as np
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from PIL import Image
from common_area_items import *
import pytesseract

keyboard_dic = {
    "q": [(40, 1200)],
    "w": [(110, 1200)],
    "e": [(180, 1200)],
    "r": [(250, 1200)],
    "t": [(320, 1200)],
    "y": [(390, 1200)],
    "u": [(460, 1200)],
    "i": [(530, 1200)],
    "o": [(600, 1200)],
    "p": [(670, 1200)],
    "a": [(70, 1285)],
    "s": [(140, 1285)],
    "d": [(210, 1285)],
    "f": [(280, 1285)],
    "g": [(350, 1285)],
    "h": [(420, 1285)],
    "j": [(490, 1285)],
    "k": [(560, 1285)],
    "l": [(630, 1285)],
    "z": [(150, 1400)],
    "x": [(220, 1400)],
    "c": [(290, 1400)],
    "v": [(360, 1400)],
    "b": [(430, 1400)],
    "n": [(500, 1400)],
    "m": [(570, 1400)],
    ".": [(570,1500)],
    ",": [(150,1500)],
    " ": [(400,1500)],
    "_": [(65,1500),(250,1300),(65,1500)],
    "0":[(65,1500),(680,1190),(65,1500)],
    "1":[(65,1500),(40,1190),(65,1500)],
    "2":[(65,1500),(110,1190),(65,1500)],
    "3":[(65,1500),(180,1190),(65,1500)],
    "4":[(65,1500),(250,1190),(65,1500)],
    "5":[(65,1500),(320,1190),(65,1500)],
    "6":[(65,1500),(390,1190),(65,1500)],
    "7":[(65,1500),(460,1190),(65,1500)],
    "8":[(65,1500),(530,1190),(65,1500)],
    "9":[(65,1500),(610,1190),(65,1500)],
    "'":[(65,1500),(288,1400),(65,1500)],
    "@":[(65,1500),(72,1275),(65,1500)],
    "#":[(65,1500),(145,1275),(65,1500)],
    "$":[(65,1500),(219,1275),(65,1500)],
    "%":[(65,1500),(292,1275),(65,1500)],
    "&":[(65,1500),(360,1275),(65,1500)],
    "!":[(65,1500),(502,1387),(65,1500)],
    "?":[(65,1500),(578,1387),(65,1500)],    
}
keyboard_dic_only_nums = {
    "1":[(72,1160)],
    "2":[(280,1160)],
    "3":[(475,1160)],
    "4":[(72,1265)],
    "5":[(280,1265)],
    "6":[(475,1265)],
    "7":[(72,1380)],
    "8":[(280,1380)],
    "9":[(475,1380)],
    "0":[(280,1500)],
}


def tap_keyboard(d, text:str, keyboard = keyboard_dic):
    """
    Simulates tapping on the screen using the keyboard coordinates for each character in the text.
    """
    is_upper = False
    for char in text:
        if char.isupper():
            is_upper = True
            char = char.lower()
        if char not in keyboard and not char.isupper():
            char = " "  
        for i,_ in enumerate(keyboard[char]):
            if is_upper:
                is_upper = False
                d.click(50,1386)
                sleep(0.2)
            x, y = keyboard[char][i]
            d.click(x, y)  # Simulate a tap on the screen at the corresponding coordinates
            update_results_file("Actions")
            sleep(random.uniform(0.1, 0.2))  # Add a small delay between taps
                

def search_sentence(d, name: str, plat, tolerance=20, usegpu=True):
    """
    Searches for a word or sentence in the screenshot using OCR.

    Args:
        d: Device object.
        name (str): The text to search for (word or sentence).
        plat: Platform identifier.
        tolerance (int): Allowed similarity percentage (default=20).
        usegpu (bool): Whether to use GPU for OCR (default=True).
    
    Returns:
        tuple: Coordinates of the match center (x, y) or None if no match found.
    """
    screen_shot = take_screenshot(d, threading.current_thread().name, plat)
    logging.info(f"{threading.current_thread().name}:{d.wlan_ip} Searching for text: {name}")

    while name.lower().strip() == "israel" and plat == "twi":
        name = random.choice(twitter_handles)
        logging.info(f"{threading.current_thread().name}:{d.wlan_ip} Searching for text: {name}")
    
    # Determine if we're searching for a word or a sentence
    is_word_search = len(name.split()) == 1 and name.__len__()<10

    # Initialize the OCR reader
    reader = easyocr.Reader(['en'], gpu=usegpu)

    # Perform OCR
    result = reader.readtext(screen_shot, detail=1)

    best_similarity = 0  # Initialize with the lowest possible score (0%)
    best_match_text = ""  # To store the closest matching text (word or sentence)
    best_match_bbox = []  # To store the bounding box for the best match

    # Process the name for matching
    processed_name = name.strip()

    if is_word_search:
        # Word search logic
        for detection in result:
            bbox, text, _ = detection
            top_left, _, bottom_right, _ = bbox

            # Skip text outside the vertical range
            if top_left[1] < 180 or (top_left[1] > 1050 and name != "2123" and name != "Tagree"):
                continue

            # Split the detected text into words
            words = text.strip().split()

            for word in words:
                similarity_score = fuzz.ratio(processed_name.lower(), word.lower())
                
                if similarity_score > best_similarity:
                    best_similarity = similarity_score
                    best_match_text = word
                    best_match_bbox = bbox
    else:
        # Sentence search logic
        # Group detected text into rows by their y-coordinates
        rows = {}
        for detection in result:
            bbox, text, _ = detection
            top_left, _, bottom_right, _ = bbox
            y_center = (top_left[1] + bottom_right[1]) // 2

            # Skip text outside the vertical range
            if top_left[1] < 180 or (top_left[1] > 1050 and name != "2123" and name != "Report post" and name!= "Tagree"):
                continue

            # Skip rows with single-character text
            if len(text.strip()) == 1:
                continue

            # Group rows by y-coordinate
            row_key = round(y_center, -1)
            if row_key not in rows:
                rows[row_key] = []
            rows[row_key].append((bbox, text.strip()))

        # Combine rows into multi-line text blocks
        combined_blocks = []
        sorted_row_keys = sorted(rows.keys())
        for i, row_key in enumerate(sorted_row_keys):
            current_block = " ".join(text for _, text in rows[row_key])
            combined_bboxes = [bbox for bbox, _ in rows[row_key]]

            for offset in range(1, 3):
                if i + offset < len(sorted_row_keys):
                    next_row_key = sorted_row_keys[i + offset]
                    if abs(next_row_key - row_key) <= 0:
                        next_row_text = " ".join(text for _, text in rows[next_row_key])
                        current_block += " " + next_row_text
                        combined_bboxes.extend(bbox for bbox, _ in rows[next_row_key])
                    else:
                        break

            combined_blocks.append((current_block, combined_bboxes))

        # Search for the best match across all combined blocks
        for combined_text, bboxes in combined_blocks:
            if "Go to" in combined_text:
                combined_text = combined_text.replace("Go to", '')

            similarity_score = fuzz.ratio(processed_name, combined_text)

            if similarity_score > best_similarity:
                best_similarity = similarity_score
                best_match_text = combined_text
                best_match_bbox = bboxes

    if best_similarity >= (100 - tolerance) and best_match_bbox:
        # Calculate the center of the bounding box for the best match
        if is_word_search:
            top_left_x, top_left_y = best_match_bbox[0]
            bottom_right_x, bottom_right_y = best_match_bbox[2]
        else:
            all_top_lefts = [bbox[0] for bbox in best_match_bbox]
            all_bottom_rights = [bbox[2] for bbox in best_match_bbox]

            top_left_x = min(coord[0] for coord in all_top_lefts)
            top_left_y = min(coord[1] for coord in all_top_lefts)
            bottom_right_x = max(coord[0] for coord in all_bottom_rights)
            bottom_right_y = max(coord[1] for coord in all_bottom_rights)

        center_x = (top_left_x + bottom_right_x) // 2
        center_y = (top_left_y + bottom_right_y) // 2

        logging.info(f"{threading.current_thread().name}:{d.wlan_ip} Best match found: \"{best_match_text}\" with similarity: {best_similarity}%")
        return int(center_x), int(center_y)

    # Log the best match even if it doesn't meet the tolerance
    if best_match_text:
        logging.info(f"{threading.current_thread().name}:{d.wlan_ip} Closest match: \"{best_match_text}\" with similarity: {best_similarity}%")

    logging.info(f"{threading.current_thread().name}:{d.wlan_ip} No sufficiently similar text was found.")
    return None





def take_screenshot(d, thread=threading.current_thread().name, app="twi", crop_area=None):
    """
    Takes a screenshot of the device and optionally crops it to a specific region.

    Args:
        d: Device object.
        thread (str): Thread name for logging and filename.
        app (str): Application name for filename.
        crop_area (tuple): Optional tuple defining the cropping area (x1, y1, x2, y2).

    Returns:
        str: Path to the saved screenshot or cropped image.
    """
    filename = f"Screenshots/{thread}-screenshot_{app}.png"
    cropped_filename = f"Screenshots/{thread}-screenshot_{app}_cropped.png"

    logging.info(f"{thread}:{d.wlan_ip} Taking screenshot...")
    d.screenshot(filename)
    logging.info(f"Screenshot saved as {filename}.")

    # Crop the image if crop_area is specified
    if crop_area:
        x1, y1, x2, y2 = crop_area
        with Image.open(filename) as img:
            cropped_img = img.crop((x1, y1, x2, y2))  # Crop the specified region
            cropped_img.save(cropped_filename)
            logging.info(f"Cropped screenshot saved as {cropped_filename}.")
        return cropped_filename

    return filename


def find_best_match(image_path, users_template_path, d):
    """
    Finds the best match of a user's button icon in the screenshot using template matching.
    """
    sleep(0.5)
    logging.info(f"{threading.current_thread().name}:{d.wlan_ip} Starting find_best_match function")
    
    img = cv2.imread(image_path)
    template = cv2.imread(users_template_path)

    if img is None or template is None:
        logging.info(f"{threading.current_thread().name}:{d.wlan_ip} Error loading images.")
        return None

    h, w = template.shape[:2]
    result = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(result >= threshold)

    matches = []
    for pt in zip(*loc[::-1]):
        matches.append((pt, result[pt[1], pt[0]]))

    if matches:
        # Get the best match (highest confidence value)
        best_match = max(matches, key=lambda x: x[1])
        best_coordinates = (best_match[0][0] + w // 2, best_match[0][1] + h // 2)
        best_value = best_match[1]
        logging.info(f"{threading.current_thread().name}:{d.wlan_ip} Best match found with value: {best_value} at {best_coordinates}")
    else:
        # If no matches found above threshold, find the closest match
        _, max_val, _, max_loc = cv2.minMaxLoc(result)
        best_coordinates = (max_loc[0] + w // 2, max_loc[1] + h // 2)
        best_value = max_val
        logging.info(f"{threading.current_thread().name}:{d.wlan_ip} No matches above threshold, closest match found with value: {best_value} at {best_coordinates}")
        return None
    
    logging.info(f"{threading.current_thread().name}:{d.wlan_ip} Finished find_best_match function")
    
    return best_coordinates

def handle_user_selection(d,report_dict):
    logging.info("Select a report reason:")
    numbered_report_dict = show_tree(report_dict)

    # User input for selection
    user_choice = input("Enter the number of the report reason you want to select: ")

    if user_choice.isdigit() and int(user_choice) in numbered_report_dict:
        action = numbered_report_dict[int(user_choice)]
        if isinstance(action, dict):  # If the selection has subcategories
            handle_user_selection(action)  # Show subcategories
        else:
            execute_action(d,action,report_dict)  # Execute the action for the selected reason
    else:
        logging.info("Invalid selection. Please enter a valid number.")

def show_tree(report_dict, level=0):
    numbered_dict = {}
    count = 1
    for key in report_dict.keys():
        logging.info("  " * level + f"{count}. {key}")
        numbered_dict[count] = key  # Store the original key for action retrieval
        count += 1
        if isinstance(report_dict[key], dict):
            # Recursive call for subcategories
            sub_count = show_tree(report_dict[key], level + 1)
            numbered_dict.update(sub_count)
    return numbered_dict

def execute_action(d,reason,report_dict):
    # Execute the corresponding action for the selected reason
    if reason in report_dict:
        action = report_dict[reason]
        actions = action.split(':')
        logging.info(f"Executing action for '{reason}': {actions}")
        sleep(2)
        for act in actions:
            exec(act)
            sleep(5)  
    else:
        logging.info("No action found for this reason.")


file_lock = threading.Lock()

def update_results_file(action_type, counter=1):
    """
    Updates the results file with the incremented count for the given action.
    
    Parameters:
    action_type (str): The action type to update ('Likes', 'Comments', 'Follows', 'Reports', 'Scrolls').
    """
    file_path = "result.txt"
    
    with file_lock:  # Ensure only one thread accesses the file at a time
        # Load current values
        with open(file_path, "r") as file:
            data = file.readlines()

        # Parse current counts from the file
        stats = {}
        for line in data:
            key, value = line.strip().split(" - ")
            stats[key] = int(value)
        
        # Increment the relevant action count
        if action_type in stats:
            stats[action_type] += counter

        # Write updated values back to the file
        with open(file_path, "w") as file:
            for key, value in stats.items():
                file.write(f"{key} - {value}\n")




def startAccount():
    # Set up the WebDriver to connect to the existing Chrome instance with remote debugging
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("debuggerAddress", "localhost:9222")  # Connect to the remote debugging port

    # Set up the Chrome WebDriver path
    chrome_driver_path = 'C:/Users/goldf/OneDrive/Documents/chromedriver_win32/chromedriver.exe'

    # Initialize the WebDriver with the specified options to connect to the existing browser
    driver = webdriver.Chrome(options=chrome_options)

    # Open ChatGPT in the existing Chrome window (this will use the existing session)
    driver.get("https://chat.openai.com/")

    # Wait for the page to load
    time.sleep(15)

    # Send a prompt
    prompt_text = "Generate an image of a futuristic city skyline at sunset with flying cars."
    chat_input = driver.find_element(By.XPATH, '//*[@id="prompt-textarea"]/p')  # Find the text input box
    chat_input.send_keys(prompt_text)
    time.sleep(1)
    chat_input.send_keys(Keys.ENTER)

    # Wait for the image to be generated (adjust timing as needed)
    time.sleep(30)

    # Locate the generated image and download it
    try:
        image_element = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/main/div[1]/div[1]/div/div/div/div/article[2]/div/div/div[2]/div/div[1]/div[1]/div/div/div/div[2]/img')
        image_url = image_element.get_attribute("src")

        # Download the image using requests
        image_response = requests.get(image_url)
        
        # Save the image
        if image_response.status_code == 200:
            with open("generated_image.png", 'wb') as f:
                f.write(image_response.content)
            logging.info("Image downloaded successfully.")
        else:
            logging.info("Failed to download the image.")

    except Exception as e:
        logging.info(f"Error: {e}")

    # Close the browser if necessary
    driver.quit()


def reopen_app(d, package_name, wait_time=5):
    """
    Stops and reopens an app on the device.

    Parameters:
    d (uiautomator2.Device): The connected device instance.
    package_name (str): The package name of the app to be reopened (e.g., "com.twitter.android").
    wait_time (int): Time in seconds to wait after reopening the app.
    """
    try:
        # Check if the app is running
        if package_name in d.app_list_running():
            logging.info(f"{threading.current_thread().name}:{d.wlan_ip} Stopping app: {package_name}")
            d.app_stop(package_name)  # Stop the app
            sleep(2)

        # Start the app
        logging.info(f"{threading.current_thread().name}:{d.wlan_ip} Starting app: {package_name}")
        d.app_start(package_name)  # Start the app

        # Wait for the app to fully load
        sleep(wait_time)

        # Confirm the app is running
        if package_name in d.app_list_running():
            logging.info(f"{threading.current_thread().name}:{d.wlan_ip} Successfully reopened app: {package_name}")
        else:
            logging.warning(f"{threading.current_thread().name}:{d.wlan_ip} Failed to reopen app: {package_name}")

    except Exception as e:
        logging.error(f"Error while reopening app {package_name}: {e}")

def open_vpn(d,duration):
    logging.info(f"{threading.current_thread().name}: {d.wlan_ip} : Opened nordVPN!")
    d.app_start("com.nordvpn.android")
    start_time = time.time()
    sleep(20)
    while not search_sentence(d, "Pause Disconnect", "twi"):
        duration = duration+time.time()-start_time
        logging.info(f"{threading.current_thread().name}: {d.wlan_ip} : Trying to reconnect...")
        sleep(120)


def close_apps(device):
    device.app_stop("com.twitter.android")
    device.app_stop("com.zhiliaoapp.musically")
    device.app_stop("com.nordvpn.android")
    logging.info(f"{device.wlan_ip} closed apps.")


def image_to_string(image_path):
    """
    Converts text in an image to a string using OCR.

    Args:
        image_path (str): Path to the image file.

    Returns:
        str: Extracted text from the image.
    """
    try:
        # Load the image
        image = Image.open(image_path)

        # Extract text from the image using pytesseract
        extracted_text = pytesseract.image_to_string(image)

        # Clean the extracted text
        extracted_text = extracted_text.strip()
        if extracted_text=='ia)':
            extracted_text = '11'
        if extracted_text == '':
            extracted_text = "Mar"

        return extracted_text

    except Exception as e:
        print(f"Error: {e}")
        return None
    

def rnd_value(x):
    """
    Generates a random value within ±5 of the given number x.

    Args:
        x (int or float): The base value.

    Returns:
        int or float: A random value within the range [x - 5, x + 5].
    """
    return random.randint(x - 40, x + 40)