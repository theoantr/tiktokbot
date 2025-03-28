# TikTok Automation Suite 🤖

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)
![License](https://img.shields.io/badge/License-MIT-green)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20Mac-lightgrey)


## 📌 Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Troubleshooting](#troubleshooting)
- [Disclaimer](#disclaimer)
- [License](#license)

## 🌟 Features

| Feature          | Description                                      |
|-----------------|--------------------------------------------------|
| ⚡ Fast Automation | Like/Share/View 5-10x faster than manual       |
| 🕵️ Stealth Mode | Randomized delays and human-like behavior  |
| 📊 Multi-Account | Support for multiple TikTok accounts        |
| 🔄 Auto-Retry | Automatic error recovery system              |
| 📈 Analytics | Detailed performance logging                  |

## 🛠 Installation <a name="installation"></a>

### Prerequisites
- Python 3.8+
- Google Chrome (latest version)
- Stable internet connection

```bash
# Clone the repository
git clone https://github.com/theoantr/tiktokbot.git
cd tiktokbot

# Install dependencies
pip install -r requirements.txt

# (Optional) Set up virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

## ⚙️ Configuration <a name="configuration"></a>
Edit `config.ini` with these settings:

```ini
[settings]
delay_min = 2  # Minimum delay between actions (seconds)
delay_max = 5  # Maximum delay
headless = False  # Run browser in background
max_retries = 3  # Auto-retry failed actions
```

## 🚀 Usage <a name="usage"></a>

Run the bot with:

```bash
python bot.py --service views --url "https://www.tiktok.com/@user/video/123"
```

### Available services:
- `views` - Increase video views
- `likes` - Add likes to video
- `shares` - Share video
- `follows` - Follow users

## 🚨 Troubleshooting <a name="troubleshooting"></a>

| Issue            | Solution                                         |
|-----------------|-------------------------------------------------|
| CAPTCHA loops   | Use mobile data + complete manually first      |
| "Session expired" | Re-run setup to refresh cookies               |
| Browser errors  | Run `webdriver-manager update`                 |

## ⚠️ Disclaimer <a name="disclaimer"></a>
This tool is for **educational purposes only**. Using automation may violate TikTok's Terms of Service. The developers assume no responsibility for account restrictions.

## 📝 License <a name="license"></a>
This project is licensed under the MIT License.

---

<div align="center">
  <a href="https://github.com/theoantr/tiktokbot/issues">Report Issue</a> •
  <a href="https://github.com/theoantr/tiktokbot/discussions">Get Help</a> •
  <a href="https://github.com/theoantr/tiktokbot/wiki">Documentation</a>
</div>

