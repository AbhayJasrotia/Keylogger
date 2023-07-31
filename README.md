# Key Logger Project

A simple key logger project that captures keyboard events and logs them into a file.

## Table of Contents

- [Project Description](#project-description)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [How it Works](#how-it-works)
- [Contributing](#contributing)
- [License](#license)
- [Developer](#developer)

## Project Description

This project is a basic key logger written in Python. It allows you to capture keyboard events and save them in log files. It can be used for various purposes, such as monitoring user activity or debugging keyboard-related issues.

Please note that using key loggers without the consent of the users may violate privacy laws and ethical considerations. Ensure that you have proper authorization before deploying such a tool.

## Features

- Captures keyboard events and logs them into a file.
- Logs key presses, space, backspace, and enter key events.
- Creates log files with timestamps for easy tracking.

## Installation

To use the key logger, follow these steps:

1. Install the required Python packages:

```bash
pip install pyxhook
```

1. Download the source code from the repository.

## Usage
1. Run the script in your terminal or command prompt:
```bash
python key_logger.py
```
The key logger will start capturing keyboard events and save them in log files located in the logs directory.

*Press Ctrl + C to stop the key logger.*

## How it Works
The key logger uses the pyxhook library to capture keyboard events. When you run the script, it sets up a hook to capture key presses. The on_keypress function is called whenever a key is pressed.

The on_keypress function checks the key pressed and logs it into the file specified by log_file. It writes regular characters as they are and converts special keys such as space, backspace, and enter into more human-readable format before logging.

If there are any errors or exceptions during the key logging process, they are also recorded in the log file for later analysis.

## Contributing
Contributions are welcome! If you find any issues or want to add new features, feel free to submit a pull request.

## License
This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

## Developer
**[Abhay Jasrotia](https://www.linkedin.com/in/abhay-jasrotia-907487236/)**
