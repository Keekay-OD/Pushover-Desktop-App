# Pushover Messenger Desktop App 📬

## Overview

Pushover Messenger desktop is a desktop application that allows you to send notifications easily through the Pushover API. With a simple, intuitive Tkinter-based interface, you can quickly send messages, manage settings, and keep track of your message history.

![Main Page](https://imgur.com/KFb3ZWb)
![Settings](https://imgur.com/31RkTVf)
![Message History](https://imgur.com/7BFVntz)
[Imgur](https://imgur.com/KFb3ZWb)

[img]https://i.imgur.com/KFb3ZWb.png[/img]
## Features 🚀

- 🔐 Secure API Configuration
- 📨 Easy Message Sending
- 📋 Message History Tracking
- 💾 Persistent Settings Storage
- 🖥️ Clean, User-Friendly Interface

## Prerequisites 🛠️

Before you begin, ensure you have the following:

- Python 3.8+
- Pushover Account (free tier available)
- Internet Connection

## Installation 

### Option 1: Run from Source

1. Clone the repository:
```bash
git clone https://github.com/Keekay-OD/Pushover-Desktop-App.git
cd Pushover-Desktop-App
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python pushover_messenger.py
```

### Option 2: Use Executable

1. Download the latest release from the [Releases](link-to-releases) page
2. Run `PushoverMessenger.exe`

## Getting Started 🚀

### Pushover API Setup

1. Create a Pushover Account at [https://pushover.net/](https://pushover.net/)
2. Register a new application in your Pushover dashboard
3. Obtain your:
   - User Key
   - API Token/Key

### Application Usage

1. **Settings Tab**
   - Enter your Pushover User Key
   - Enter your Pushover API Token
   - Click "Save Settings"

2. **Send Message Tab**
   - Write your message
   - Optional: Add a title
   - Click "Send Message"

3. **History Tab**
   - View all sent messages
   - Clear message history if needed

## Troubleshooting ⚠️

- Ensure your Pushover credentials are correct
- Check your internet connection
- Verify you have the latest version of the app

## Configuration Files 📁

- `pushover_config.json`: Stores API credentials
- `message_history.json`: Maintains message send history

## Building from Source 🔧

### Requirements
- Python 3.8+
- PyInstaller

### Packaging Steps
```bash
pip install pyinstaller requests
python package.py
```

## Contributing 🤝

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License 📄

Distributed under the MIT License. See `LICENSE` for more information.

## Contact 📧

Keekay-OD

[https://github.com/Keekay-OD/Pushover-Desktop-App](https://github.com/Keekay-OD/Pushover-Desktop-App)

## Acknowledgements 🙏

- [Pushover](https://pushover.net/) for their awesome notification service
- [Tkinter](https://docs.python.org/3/library/tkinter.html) for the GUI framework
- [Requests](https://docs.python-requests.org/en/master/) for HTTP requests

---

**Disclaimer**: This project is not officially associated with Pushover. It's a community-created tool to interact with the Pushover API.
