import time
import keyboard
import os
from paddleocr import PaddleOCR

ocr = PaddleOCR(use_angle_cls=True, lang='ch')

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

        message = ocr.ocr(screenshot_path, cls=True)

        message = "".join([line[1][0] for line in message[0]])
        message = message.replace('\n', '').strip()

        print("Proccessed text:", message)

        print("Switch to the target application within 1 second...")
        time.sleep(1)

        keyboard.write(message)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()