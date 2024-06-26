import inputs
import pygetwindow as gw
import time
import keyboard
import pyperclip
import pyautogui
import ctypes
import os


time_when_several_prompts = 10
use_f5_refresh=False

dico_prompting={}

dico_prompting["A_DOWN"]=""
dico_prompting["A_UP"]=""
dico_prompting["B_DOWN"]=""
dico_prompting["B_UP"]=""
dico_prompting["Y_DOWN"]=""
dico_prompting["Y_UP"]=""
dico_prompting["X_DOWN"]=""
dico_prompting["X_UP"]=""

dico_prompting["DOWN_DOWN"]="Can you do in python ?"
dico_prompting["UP_DOWN"]= ["Can you do in C# ?", "Can you do in Javascript ?", "Can you do in Python ?"]
dico_prompting["RIGHT_DOWN"]="Can you do in Lua ?"
dico_prompting["LEFT_DOWN"]="Can you do in Rust ?"

dico_prompting["SIDE_RIGHT_DOWN"]=""
dico_prompting["SIDE_LEFT_DOWN"]=""

dico_prompting["THUMB_RIGHT_DOWN"]="translate in japonese and correct ponctuation. Export in Markdown"
dico_prompting["THUMB_LEFT_DOWN"]="Translate in chinese and correct ponctuation. Export in Markdown"




dico_prompting["MENU_RIGHT_DOWN"]="Find me emoji representing following Text. Export in Markdown and in text"
dico_prompting["MENU_LEFT_DOWN"]="Give me dictionnary definition of following word. Export in Markdown"


dico_prompting["LEFT_TRIGGER_DOWN"]="Translate that in french and correct ponctuation. Export in Markdown"
dico_prompting["RIGHT_TRIGGER_DOWN"]="Translate that in english and correct ponctuation. Export in Markdown"



bool_create_new_window = False


# Threshold for trigger pressure (80%)
TRIGGER_THRESHOLD = 0.8 * 255  # Assuming trigger values range from 0 to 255


def prompt_chat_gpt_by_firefox(prompt_text):
    global bool_create_new_window
    time.sleep(0.1)
    keyboard.press_and_release('ctrl+c')
    time.sleep(0.1)
    keyboard.press_and_release('ctrl+x')
    time.sleep(0.1)

    clipboard_content = pyperclip.paste()
    if(clipboard_content==""):    
        print("Cliboard content")
        return

    if not isinstance(prompt_text, list):
        prompt_text = [prompt_text]
    
    for t in prompt_text:
        if(t==""):    
            print("No prompting text")
            continue
      
#test
        # Find the Firefox window by title
        firefox_windows = gw.getWindowsWithTitle('Mozilla Firefox')

        # Open Firefox if it's not already open
        if firefox_windows is None or len(firefox_windows)==0:
            
            firefox_path = "C:/Program Files/Mozilla Firefox/firefox.exe"
            
            if not os.path.exists(firefox_path):
                print("Firefox path does not exist and firefox is not open. Please install Firefox or open it manually.")
                continue
            
            print ("Opening Firefox")
            ctypes.windll.shell32.ShellExecuteW(None, "open", firefox_path, None, None, 1)
            continue
        firefox_window = gw.getWindowsWithTitle('Mozilla Firefox')[0]
        # Focus the Firefox window
        firefox_window.activate()

    
        firefox_window.show()
        firefox_window.maximize()

        time.sleep(1)
        if bool_create_new_window:
            keyboard.press_and_release('ctrl+t')
            time.sleep(3)
            keyboard.write("https://chat.openai.com/")
            keyboard.press_and_release('enter')
            time.sleep(3)
        else:
            if(use_f5_refresh==True):
                keyboard.press_and_release('ctrl+f5')
        time.sleep(3)

        time.sleep(0.1)
        pyperclip.copy(t)
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

        if(len(prompt_text)>1):
            time.sleep(time_when_several_prompts)






def listen_to_xbox_buttons():
    while True:
        events = inputs.get_gamepad()
        for event in events:
            
            if event.code in ['ABS_X', 'ABS_Y', 'ABS_RX', 'ABS_RY',"SYN_REPORT"]:
                continue
            string_event = f"{event.ev_type} {event.code} {event.state}"
            print(string_event)
            if event.code == 'BTN_SOUTH':  # A button
                if event.state == 1:
                    print("A button pressed")
                    prompt_chat_gpt_by_firefox(dico_prompting["A_DOWN"])
                else:
                    print("A button released")
            elif event.code == 'BTN_EAST':  # B button
                if event.state == 1:
                    print("B button pressed")
                    prompt_chat_gpt_by_firefox(dico_prompting["B_DOWN"] )
                else:
                    print("B button released")
            elif event.code == 'BTN_WEST':  # X button
                if event.state == 1:
                    print("X button pressed")                    
                    prompt_chat_gpt_by_firefox(dico_prompting["X_DOWN"])
                else:
                    print("X button released")
            elif event.code == 'BTN_NORTH':  # Y button
                if event.state == 1:
                    print("Y button pressed")
                    prompt_chat_gpt_by_firefox(dico_prompting["Y_DOWN"])
                else:
                    print("Y button released")
            elif event.code == 'BTN_TL':  # Left button
                if event.state == 1:
                    print("Left button pressed")
                    
                    prompt_chat_gpt_by_firefox(dico_prompting["SIDE_LEFT_DOWN"])
                else:
                    print("Left button released")
            elif event.code == 'BTN_TR':  # Right button
                if event.state == 1:
                    print("Right button pressed")
                    prompt_chat_gpt_by_firefox(dico_prompting["SIDE_RIGHT_DOWN"])

                else:
                    print("Right button released")
            
            elif event.code == 'BTN_SELECT':  # Select button
                if event.state == 1:
                    print("Select button pressed")
                    prompt_chat_gpt_by_firefox(dico_prompting["MENU_RIGHT_DOWN"])
                else:
                    print("Select button released")
            elif event.code == 'BTN_START':  # Start button
                if event.state == 1:
                    print("Start button pressed")
                    prompt_chat_gpt_by_firefox(dico_prompting["MENU_LEFT_DOWN"])
                else:
                    print("Start button released")
            elif event.code == 'BTN_THUMBL':  # Left thumbstick button
                if event.state == 1:
                    print("Left thumbstick button pressed")
                    prompt_chat_gpt_by_firefox(dico_prompting["THUMB_LEFT_DOWN"])
                else:
                    print("Left thumbstick button released")
            elif event.code == 'BTN_THUMBR':  # Right thumbstick button
                if event.state == 1:
                    print("Right thumbstick button pressed")
                    prompt_chat_gpt_by_firefox(dico_prompting["THUMB_RIGHT_DOWN"])
                else:
                    print("Right thumbstick button released")
            elif event.code == 'BTN_TL2':  # Left trigger button
                if event.state == 1:
                    print("Left trigger button pressed")
                    # Add your code here for the left trigger button press
                else:
                    print("Left trigger button released")
            elif event.code == 'BTN_TR2':  # Right trigger button
                if event.state == 1:
                    print("Right trigger button pressed")
                    # Add your code here for the right trigger button press
                else:
                    print("Right trigger button released")

            elif string_event.endswith('ABS_HAT0Y 1'):  # Up arrow
                    print("Down arrow pressed")
                    prompt_chat_gpt_by_firefox(dico_prompting["DOWN_DOWN"])
            elif string_event.endswith('ABS_HAT0Y -1'):  # Down arrow
                    print("Up arrow pressed")
                    prompt_chat_gpt_by_firefox(dico_prompting["UP_DOWN"])
            elif string_event.endswith('ABS_HAT0X 1'):  # Left arrow
                    print("Right arrow pressed")
                    prompt_chat_gpt_by_firefox(dico_prompting["RIGHT_DOWN"])
            elif string_event.endswith('ABS_HAT0X -1'):  # Right arrow
                    print("Left arrow pressed")
                    prompt_chat_gpt_by_firefox(dico_prompting["LEFT_DOWN"])
            elif event.ev_type == 'Absolute' and event.code.startswith('ABS_Z'):
                trigger_value = event.state
                if trigger_value > TRIGGER_THRESHOLD:
                    print("Trigger pressure Left exceeded:", event.code, trigger_value)
                    prompt_chat_gpt_by_firefox(dico_prompting["LEFT_TRIGGER_DOWN"])
                    # You can customize the action here, like displaying a notification
            elif event.ev_type == 'Absolute' and event.code.startswith('ABS_RZ'):
                trigger_value = event.state
                if trigger_value > TRIGGER_THRESHOLD:
                    prompt_chat_gpt_by_firefox(dico_prompting["RIGHT_TRIGGER_DOWN"])
                    print("Trigger pressure Right exceeded:", event.code, trigger_value)
                    # You can customize the action here, like displaying a notification


            



listen_to_xbox_buttons()
