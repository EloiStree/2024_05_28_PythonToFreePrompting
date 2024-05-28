import inputs
import pygetwindow as gw
import time
import keyboard
import pyperclip
import pyautogui


# Threshold for trigger pressure (80%)
TRIGGER_THRESHOLD = 0.8 * 255  # Assuming trigger values range from 0 to 255


def prompt_chat_gpt_by_firefox(prompt_text):
    if(prompt_text==""):    
        print("No prompting text")
        return
    time.sleep(0.1)
    keyboard.press_and_release('ctrl+c')
    time.sleep(0.1)
    keyboard.press_and_release('ctrl+x')

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



dico_prompting={}

dico_prompting["A_DOWN"]=""
dico_prompting["A_UP"]=""
dico_prompting["B_DOWN"]=""
dico_prompting["B_UP"]=""
dico_prompting["Y_DOWN"]=""
dico_prompting["Y_UP"]=""
dico_prompting["X_DOWN"]=""
dico_prompting["X_UP"]=""

dico_prompting["DOWN_DOWN"]=""
dico_prompting["UP_DOWN"]=""
dico_prompting["RIGHT_DOWN"]=""
dico_prompting["LEFT_DOWN"]=""

dico_prompting["SIDE_RIGHT_DOWN"]=""
dico_prompting["SIDE_LEFT_DOWN"]=""

dico_prompting["THUMB_RIGHT_DOWN"]=""
dico_prompting["THUMB_LEFT_DOWN"]=""

dico_prompting["MENU_RIGHT_DOWN"]="Is  right menu?"
dico_prompting["MENU_LEFT_DOWN"]="Is left Menu?"


dico_prompting["LEFT_TRIGGER_DOWN"]="Translate that in french and correct ponctuation. Export in Markdown"
dico_prompting["RIGHT_TRIGGER_DOWN"]="Translate that in english and correct ponctuation. Export in Markdown"


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
