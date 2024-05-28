import pygetwindow as gw
import time
import keyboard
import pyperclip

import pyautogui

def prompt_chat_gpt_by_firefox():
    
    keyboard.press_and_release('ctrl+x')
    # Your prompt text
    prompt_text = "Corrige l'orthographe et la grammaire de ce texte. \n\n"


    # Find the Firefox window by title
    firefox_window = gw.getWindowsWithTitle('Mozilla Firefox')[0]

    # Focus the Firefox window
    firefox_window.activate()

    # Show and bring the Firefox window to the foreground
    firefox_window.show()
    firefox_window.maximize()

    time.sleep(1)
    keyboard.press_and_release('ctrl+f5')
    time.sleep(3)


    clipboard_content = pyperclip.paste()
    time.sleep(0.1)
    pyperclip.copy(prompt_text)
    time.sleep(0.1)
    keyboard.press_and_release('ctrl+v')
    time.sleep(0.1)

    keyboard.press_and_release('shift+enter')

    time.sleep(0.1)
    # Restore the original clipboard content
    pyperclip.copy(clipboard_content)
    time.sleep(0.1)
    keyboard.press_and_release('ctrl+v')

    time.sleep(0.1)
    keyboard.press_and_release('enter')



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
        
        prompt_chat_gpt_by_firefox()
        #correct_spelling_copilote()

keyboard.on_release(on_release)

# Keep the script running
keyboard.wait()