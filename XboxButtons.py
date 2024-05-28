import inputs

def listen_to_xbox_buttons():
    while True:
        events = inputs.get_gamepad()
        for event in events:
            if event.code == 'BTN_SOUTH':  # A button
                if event.state == 1:
                    print("A button pressed")
                else:
                    print("A button released")
            elif event.code == 'BTN_EAST':  # B button
                if event.state == 1:
                    print("B button pressed")
                else:
                    print("B button released")
            elif event.code == 'BTN_WEST':  # X button
                if event.state == 1:
                    print("X button pressed")
                else:
                    print("X button released")
            elif event.code == 'BTN_NORTH':  # Y button
                if event.state == 1:
                    print("Y button pressed")
                else:
                    print("Y button released")
            elif event.code == 'BTN_TL':  # Left button
                if event.state == 1:
                    print("Left button pressed")
                else:
                    print("Left button released")
            elif event.code == 'BTN_TR':  # Right button
                if event.state == 1:
                    print("Right button pressed")
                else:
                    print("Right button released")

listen_to_xbox_buttons()