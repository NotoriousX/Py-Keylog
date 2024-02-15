# Python Keylogger
Undetectable Python Keylogger with a discord Webhook
Backdoor included. This Python keylogger will start automatically on system startup.
--> Change your discord webhook in the code.

Disclaimer:
This keylogger is developed with the intension of using it for only for educational purpose.





![image](https://github.com/NotoriousX/Py-Keylog/assets/107283754/b55f3902-8207-4003-aab5-5c83547b501e)


This script performs several tasks related to setting up an environment for monitoring keyboard input and sending the logged data to a Discord webhook. Here's a breakdown of its functionality:

Importing Modules: The script imports necessary modules such as os, sys, subprocess, shutil, urllib.request, zipfile, requests, pynput, winshell, and win32com.client.

Functions Definitions:

Sets up a Discord webhook URL for sending key logs.
Checks for Python and pip installations and installs them if necessary.
Adds Python's installation directory to the system's PATH environment variable.
Installs required dependencies.
Sets up a listener for keyboard events using pynput.
Starts the listener and waits for key presses.
After the listener is finished, it creates a shortcut to the script in the Windows startup folder using create_startup_shortcut().
Script Execution:

If the script is run directly (not imported as a module), it calls the main() function.
Overall, this script is intended to set up an environment for monitoring keyboard input, sending the logged data to a Discord webhook, and ensuring that the monitoring script starts automatically on Windows startup.




