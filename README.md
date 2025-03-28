# TikTok Bot Automation 🤖

[![Python Version](https://img.shields.io/badge/python-3.8+-blue?logo=python&logoColor=white)](https://python.org)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub Stars](https://img.shields.io/github/stars/theoantr/tiktokbot?style=social)](https://github.com/theoantr/tiktokbot/stargazers)
[![Open Issues](https://img.shields.io/github/issues/theoantr/tiktokbot)](https://github.com/theoantr/tiktokbot/issues)

A complete automation solution for TikTok growth, using advanced Selenium techniques to safely automate interactions.

## 🌟 Features
- **Multi-Service Support**: Likes, views, shares, follows, favorites
- **Stealth Technology**: Undetectable browsing patterns
- **Smart Scheduling**: Randomized delays between actions
- **Error Recovery**: Automatic retry system
- **Detailed Logging**: Track all bot activities

## 🛠 Installation

### Prerequisites
- Python 3.8+
- Google Chrome (latest version)
- ChromeDriver (auto-installed)

```bash
# Clone repository (HTTPS)
git clone https://github.com/theoantr/tiktokbot.git
cd tiktokbot

# Or clone with SSH
git clone git@github.com:theoantr/tiktokbot.git

# Install dependencies
pip install -r requirements.txt
🚀 Quick Start
Run the bot:

bash
Copy
python bot.py
First-time setup:

Complete CAPTCHA verification when prompted

Allow 1-2 minutes for initial configuration

Normal operation:

Select service from menu (1-7)

Enter target video URL

Let the bot run (recommended 2-3 hours max per session)

⚙️ Configuration
Edit config.py for advanced settings:

python
Copy
# Timing controls (seconds)
MIN_DELAY = 2  
MAX_DELAY = 5

# Stealth settings
HEADLESS = False  # Set True for server use
USER_AGENT = "Mozilla/5.0..."  # Custom user agent

# Proxy settings (optional)
PROXY = ""  # "ip:port" format
📋 Service Reference
#	Service	Description	Cooldown
1	Followers	Gain organic followers	30 min
2	Hearts	Like videos	10 min
3	Comment Hearts	Like comments	15 min
4	Views	Increase video views	5 min
5	Shares	Boost shares	20 min
6	Favorites	Add to favorites	25 min
7	Live Stream	Engage with live streams	60 min
🚨 Troubleshooting
Problem: CAPTCHA not passing
✅ Solution:

Use mobile data instead of WiFi

Complete manually once

Problem: "Browser detected" error
✅ Solution:

bash
Copy
webdriver-manager update
Problem: Slow performance
✅ Solution:

Increase delays in config.py

Close other Chrome instances

📜 License
This project is licensed under the MIT License - see the LICENSE file for complete details.

🤝 Contributing
Fork the repository

Create your feature branch

Commit your changes

Push to the branch

Open a pull request

<div align="center"> <a href="https://github.com/theoantr/tiktokbot/issues">Report Bug</a> • <a href="https://github.com/theoantr/tiktokbot/discussions">Request Feature</a> • <a href="https://github.com/theoantr/tiktokbot/wiki">Documentation</a> </div> ```
