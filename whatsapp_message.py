from datetime import datetime
import pyautogui
import keyboard
import time

def send_message_snapchat(message):
    now = datetime.now()
    date = now.strftime("%m/%d/%Y %I:%M %p")

    pyautogui.typewrite(f'~~~~{date}~~~~')
    pyautogui.press('enter')

    pyautogui.typewrite(message)
    pyautogui.press('enter')

    pyautogui.typewrite(f'~~~~~~~~~~~~~~~~~~~~~~~')
    keyboard.press_and_release('enter')