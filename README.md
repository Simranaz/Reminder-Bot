# SReminder Bot

**Project Description**
This is a simple Python script that sends automated reminders using PyAutoGUI. The script continuously types and sends reminders at set intervals, ensuring you stay on track with important tasks such as drinking water, taking medicine, and walking your dog.

**Features**

Sends automated reminders at specified time intervals.
Uses pyautogui to simulate keyboard typing and pressing "Enter."
Displays timestamps for when each message is sent.

**Requirements**
**Python Concepts Used:**
Loops: A while True loop is used for continuous execution.
Time Module: time.sleep() introduces delays between messages.
Datetime Module: Captures and displays the current timestamp.
PyAutoGUI Module: Automates keyboard input for message typing and sending.

**Required Libraries**
To run this script, you need to install:
1. PyAutoGUI
pyautogui allows Python to control the keyboard and mouse, which is essential for automating text input.
Install it using:
pip install pyautogui
2. Time Module
The built-in time module is used to introduce delays in sending messages.
3. Datetime Module
The built-in datetime module captures the timestamp for each reminder.
How to Run
Install Python (if not already installed).
Install pyautogui using the command mentioned above.
Run the script in a Python environment.
Place the cursor in the desired text field (e.g., a chat window or Notepad) before execution.
**Usage Warning**
Since PyAutoGUI controls the keyboard, ensure that the correct text field is active before running the script.
To stop the script, manually interrupt it using Ctrl + C in the terminal.
**Future Enhancements**
Add GUI to configure reminders.
Allow customization of reminder messages and intervals.
Integrate with email or notification services for better reminders.
**License**
This project is open-source and free to use.
