import os
import subprocess
import sys

def create_executable():
    script_path = 'pushover_messenger.py'  # Ensure this matches your script name
    
    icon_path = 'app_icon.ico'  # Replace with your icon path
    
    # Ensure the icon exists
    if not os.path.exists(icon_path):
        print(f"Error: Icon file {icon_path} not found!")
        return

    # PyInstaller command
    pyinstaller_command = [
        'pyinstaller',
        '--onefile',           
        '--windowed',          # No console window
        '--name=PushoverMessenger',  # Name of the executable
        f'--icon={icon_path}', # Custom icon
        '--add-data=pushover_config.json:.', 
        script_path            
    ]

    try:
        # Run PyInstaller
        result = subprocess.run(pyinstaller_command, capture_output=True, text=True)
        
        # Check for errors
        if result.returncode != 0:
            print("Error during packaging:")
            print(result.stderr)
        else:
            print("Packaging successful!")
            print("Executable located in the 'dist' directory")
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    create_executable()