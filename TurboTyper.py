import time
from pynput.keyboard import Controller, Listener, Key
import pytesseract
pytesseract.pytesseract.tesseract_cmd = '/opt/homebrew/bin/tesseract'
import pyautogui
from pynput.mouse import Controller as MouseController

#import random

coordinates = []
click_count = 0

def extract_text_from_image(image):
    custom_config = r'--oem 3 --psm 6'
    text = pytesseract.image_to_string(image, config=custom_config)
    return text

def main():
    global coordinates, click_count
    print("Pick out an area by pressing command at the two corners (left top to bottom right) ")
    try:
        TOGGLE_KEY = Key.cmd
        mouse_controller = MouseController()
        
        def on_press(key):
            global coordinates, click_count
            
            if key == TOGGLE_KEY and click_count < 2:
                x, y = mouse_controller.position
                coordinates.append((x, y))
                click_count += 1
                print(f"Recorded at: ({x}, {y})")
                
                if click_count >= 2:
                    return False

        keyboard_listener = Listener(on_press=on_press)
        keyboard_listener.start()
        keyboard_listener.join()

        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]

        left = int(min(x1, x2))
        top = int(min(y1, y2))
        width = int(abs(x2 - x1))
        height = int(abs(y2 - y1))

        region = (left, top, width, height)

        screenshot = pyautogui.screenshot(region=region)

        message = extract_text_from_image(screenshot)
        message = message.replace('\n', ' ').strip()

        print("Processed text:", message)

        print("Switch to the target application within 1 second...")
        time.sleep(1)

        keyboard = Controller()
        
        #n = random.uniform(0.05, 0.1)

        for char in message:
            keyboard.type(char)
            time.sleep(0.06)
            #time.sleep(n)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()