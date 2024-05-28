import time
import pyautogui
import keyboard


def correct_spelling_copilote():
    pyautogui.hotkey('ctrl', 'i')
    time.sleep(0.3)
    pyautogui.typewrite("Corrige l'orthographe du text")
    time.sleep(0.3)
    pyautogui.press('enter')
    time.sleep(6)
    pyautogui.hotkey('ctrl', 'enter')




def on_release(event):
    if event.event_type == 'up' and event.name == 'alt gr':
        # Perform your desired action here
        print("AltGr (Right Alt) key released!")
        correct_spelling_copilote()

keyboard.on_release(on_release)

# Keep the script running
keyboard.wait()
