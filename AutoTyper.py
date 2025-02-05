import pyautogui
import time
import os
from PIL import Image
import pytesseract

def extract_text_from_image(image_path):
    image = Image.open(image_path)
    custom_config = r'--oem 3 --psm 6'
    text = pytesseract.image_to_string(image, config=custom_config)
    return text

def main():
    try:
        screenshot_path = os.path.expanduser("~/Desktop/screenshot.png")

        if os.path.exists(screenshot_path):
            os.remove(screenshot_path)
            print(f"Deleted existing screenshot: {screenshot_path}")

        print("Take a screenshot using cmd + shift + 4 and save it to the desktop as 'screenshot.png'.")
        time.sleep(7)

        while not os.path.exists(screenshot_path):
            print("Waiting for screenshot to be saved...")
            time.sleep(1)

        message = extract_text_from_image(screenshot_path)

        # Remove newline characters and leading/trailing whitespace
        message = message.replace('\n', ' ').strip()

        print("Proccessed text:", message)

        print("Switch to the target application within 1 second...")
        time.sleep(1)

        pyautogui.write(" " + message)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
