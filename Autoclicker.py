import pyautogui
import time

def autoclicker(duration):
    end_time = time.time() + duration
    while time.time() < end_time:
        pyautogui.click()

if __name__ == "__main__":
    duration = 10  
    time.sleep(3)  
    autoclicker(duration)