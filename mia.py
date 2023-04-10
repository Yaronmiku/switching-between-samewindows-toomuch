#switching between "same windows" too much

import win32gui
import time
import PySimpleGUI as sg
from collections import Counter 
#Counter counts the frequency of elements in an iterable, 
#like characters in a string or items in a list.

def show_popup(message):
    # Define the layout for the popup message
    layout = [[sg.Text(message)]]

    # Create the PySimpleGUI window with the defined layout
    window = sg.Window('Popup Message', layout, finalize=True, keep_on_top=True, no_titlebar=True)
    
    # Calculate the screen size and popup size
    screen_width, screen_height = sg.Window.get_screen_size()
    popup_width, popup_height = window.size
    
    # Set the location of the window to the center of the screen
    location = (screen_width // 2 - popup_width // 2, screen_height // 2 - popup_height // 2)

    # Move the window to the calculated location
    window.move(*location)

    # Display the window and wait for it to be closed
    event, values = window.read(timeout=10000)

    # Close the window after seconds
    window.close()

def get_active_window_title():
    window = win32gui.GetForegroundWindow()
    title = win32gui.GetWindowText(window)
    return title

def check_activity(): #list all application, sort how much each in 5sec, "count" if >1 = execute
    active_windows = Counter() # Create an empty counter to store active window titles
    while True:
        time.sleep(5) # Wait for 5 seconds
        new_window = get_active_window_title() # Get the title of the currently active window
        active_windows[new_window] += 1 # Increment the count for the new active window title
        repeated_windows = [window_title for window_title, count in active_windows.items() if count > 1] # Get the window titles that have occurred more than once
        if repeated_windows:
            print(f"test -- {active_windows}") # Debug
            show_popup("Stop switching same window frequency 0(n)= waste time perfectionist")
            active_windows.clear() # Clear the counter for the next 5-second interval

""" def check_activity(): #count switching between different applications- each 5 seconds //finish
    while True:
        title = get_active_window_title()
        count = 0
        while count <2: #When count variable at least 2 / more than 1, the inner loop will terminate, and the program will move on to the next line of code.
            time.sleep(5)
            new_title = get_active_window_title()
            if new_title != title: #If title changed.
                title = new_title
                count += 1
            else:
                count = 0
        print(f"test -- '{title}' ") #debug
        show_popup(f'stop switching "window" frequency 0(n)=waste time perfectionist')
        time.sleep(1) #"1-second delay for performance optimization." """

if __name__ == "__main__":
    check_activity()