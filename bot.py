import re
import random
from os import system
from time import sleep
import warnings
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

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
        
        # Wait for CAPTCHA to be solved
        if self._wait_for_captcha_to_solve():
            print("[+] CAPTCHA solved! Proceeding...")
        else:
            print("[x] CAPTCHA solving timeout. Exiting...")
            self.driver.quit()
            return
        
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
            options.add_argument("--window-size=800,700")
            options.add_argument("--disable-blink-features=AutomationControlled")
            options.add_experimental_option("excludeSwitches", ["enable-automation"])
            options.add_experimental_option('useAutomationExtension', False)
            options.add_argument("--log-level=3")
            options.add_argument("--disable-extensions")
            options.add_argument("--disable-images")
            
            driver = webdriver.Chrome(options=options)
            driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
            print("[+] Chrome loaded successfully with stealth options.")
            return driver
        except Exception as e:
            print(f"[x] Error loading Chrome: {e}")
            exit(1)

    def _print_banner(self):
        print("+--------------------------------------------------------+")
        print("|   Made by : theoantr                                   |")
        print("|   Github  : https://github.com/theoantr/tiktokbot.git |")
        print("+--------------------------------------------------------+")

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

    def _wait_for_captcha_to_solve(self, timeout=120):
        """
        Wait for CAPTCHA to be solved. Return True if solved, False otherwise.
        """
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.invisibility_of_element_located((By.XPATH, "//div[contains(@class, 'captcha-box')]"))
            )
            return True
        except TimeoutException:
            return False

    def _print_services_list(self):
        print("\nAvailable Services:")
        for service, details in self.services.items():
            print(f" - {details['title']}: {details['status']}")

    def _choose_service(self):
        service_keys = list(self.services.keys())
        print("\nSelect a service:")
        for i, key in enumerate(service_keys, 1):
            print(f"{i}. {self.services[key]['title']}")
        choice = int(input("Enter the number of your choice: "))
        return service_keys[choice - 1]

    def _choose_video_url(self):
        return input("Enter the video URL: ")

    def _start_service(self, service, video_url):
        print(f"\nStarting {self.services[service]['title']} service for video: {video_url}")
        # Add logic to interact with the specific service


if __name__ == "__main__":
    bot = Bot()
    bot.start()
