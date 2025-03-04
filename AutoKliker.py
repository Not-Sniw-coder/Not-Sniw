import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode

x = input("This is an auto clicker, are you sure you want to run it? (y/n): ")
if x == "y":
    TOGGLE_KEY = KeyCode(char="c")
    activated = False
    mouse = Controller()

    def on_press(key):
        global activated
        if key == TOGGLE_KEY:
            activated = not activated

    def doClick():
        global activated
        while True:
            if activated:
                mouse.click(Button.left, 5) #click speed
                time.sleep(0.01) #delete to crash your computer
    threading.Thread(target = doClick).start()

    listner = Listener(on_press=on_press)
    listner.start()
    
    input()
else:
    print("Auto clicker not starting, bye!")