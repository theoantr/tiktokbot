import re
import random
from os import system
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

class Bot:
    def __init__(self):
        system("cls || clear")
        self._print_banner()
        self.driver = self._init_driver()
        self.services = self._init_services()

    def start(self):
        print("[~] Opening Zefoy... (Complete CAPTCHA manually if needed)")
        self.driver.get("https://zefoy.com")
        
        # Wait for manual CAPTCHA solve
        self._wait_for_element(By.LINK_TEXT, "Youtube")
        print("[+] CAPTCHA solved! Proceeding...")

        # Randomized delays to avoid detection
        sleep(random.uniform(2, 5))
        self.driver.refresh()  # Refresh 1
        sleep(random.uniform(2, 5))
        self.driver.refresh()  # Refresh 2

        self._check_services_status()
        self.driver.minimize_window()
        self._print_services_list()
        service = self._choose_service()
        video_url = self._choose_video_url()
        self._start_service(service, video_url)

    def _init_driver(self):
        try:
            print("[~] Loading Chrome with stealth options...")
            
            options = Options()
            
            # Stealth options
            options.add_argument("--window-size=800,700")
            options.add_argument("--disable-blink-features=AutomationControlled")
            options.add_experimental_option("excludeSwitches", ["enable-automation"])
            options.add_experimental_option('useAutomationExtension', False)
            
            # Disable logging and images for better performance
            options.add_argument("--log-level=3")
            options.add_argument("--disable-extensions")
            options.add_argument("--disable-images")
            
            # Create regular Chrome driver with stealth options
            driver = webdriver.Chrome(options=options)
            
            # Modify navigator.webdriver flag
            driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
            
            print("[+] Chrome loaded successfully with stealth options.")
            return driver
        except Exception as e:
            print(f"[x] Error loading Chrome: {e}")
            print("[!] Make sure you have Chrome installed and chromedriver in your PATH")
            exit(1)

    def _print_banner(self):
        print("+--------------------------------------------------------+")
        print("|                                                        |")
        print("|   Made by : theoantr                                   |")
        print("|   Github  :https://github.com/theoantr/tiktokbot.git   |")
        print("|                                                        |")
        print("+--------------------------------------------------------+")
        print("\n")

    def _init_services(self):
        return {
            "followers": {"title": "Followers", "selector": "t-followers-button", "status": None},
            "hearts": {"title": "Hearts", "selector": "t-hearts-button", "status": None},
            "comments_hearts": {"title": "Comments Hearts", "selector": "t-chearts-button", "status": None},
            "views": {"title": "Views", "selector": "t-views-button", "status": None},
            "shares": {"title": "Shares", "selector": "t-shares-button", "status": None},
            "favorites": {"title": "Favorites", "selector": "t-favorites-button", "status": None},
            "live_stream": {"title": "Live Stream [VS+LIKES]", "selector": "t-livesteam-button", "status": None},
        }

    def _check_services_status(self):
        for service in self.services:
            selector = self.services[service]["selector"]
            try:
                element = self.driver.find_element(By.CLASS_NAME, selector)
                self.services[service]["status"] = "[WORKING]" if element.is_enabled() else "[OFFLINE]"
            except NoSuchElementException:
                self.services[service]["status"] = "[OFFLINE]"

    def _print_services_list(self):
        for index, service in enumerate(self.services):
            title = self.services[service]["title"]
            status = self.services[service]["status"]
            print(f"[{index + 1}] {title.ljust(30)} {status}")
        print("\n")

    def _choose_service(self):
        while True:
            try:
                choice = int(input("[~] Choose an option : "))
                if 1 <= choice <= 7:
                    key = list(self.services.keys())[choice - 1]
                    if self.services[key]["status"] == "[OFFLINE]":
                        print("[!] Service offline. Choose another...\n")
                        continue
                    print(f"[+] Selected: {self.services[key]['title']}\n")
                    return key
                else:
                    print("[!] Invalid option. Try again...\n")
            except ValueError:
                print("[!] Enter a number (1-7).\n")

    def _choose_video_url(self):
        return input("[~] Video URL : ").strip()

    def _start_service(self, service, video_url):
        self._wait_for_element(By.CLASS_NAME, self.services[service]["selector"]).click()
        container = self._wait_for_element(By.CSS_SELECTOR, "div.col-sm-5.col-xs-12.p-1.container:not(.nonec)")
        
        input_element = container.find_element(By.TAG_NAME, "input")
        input_element.clear()
        input_element.send_keys(video_url)

        while True:
            container.find_element(By.CSS_SELECTOR, "button.btn.btn-primary").click()
            sleep(random.uniform(3, 7))  # Randomized delay

            try:
                container.find_element(By.CSS_SELECTOR, "button.btn.btn-dark").click()
                print(f"[~] {self.services[service]['title']} sent!")
            except NoSuchElementException:
                pass

            remaining_time = self._compute_remaining_time(container)
            if remaining_time:
                print(f"[~] Cooldown: {remaining_time // 60}m {remaining_time % 60}s")
                sleep(remaining_time)
            print("\n")

    def _compute_remaining_time(self, container):
        try:
            element = container.find_element(By.CSS_SELECTOR, "span.br")
            if "Please wait" in element.text:
                minutes, seconds = map(int, re.findall(r"\d+", element.text))
                return (minutes * 60 + seconds) + 5  # Extra buffer
        except NoSuchElementException:
            pass
        return None

    def _wait_for_element(self, by, value):
        while True:
            try:
                return self.driver.find_element(by, value)
            except NoSuchElementException:
                sleep(1)


if __name__ == "__main__":
    bot = Bot()
    bot.start()
