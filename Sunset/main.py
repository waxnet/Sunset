from utilities import (
    install,
    account,
    config,
    chrome,
    assets,
    color,
    proxy,
    log,
    cmd,
)
from msvcrt import getch
from time import sleep
import os

class Sunset:
    def __init__(self):
        super(Sunset, self).__init__()
        
        self.driver_version = "110.0.5481.77"
        self.accounts_per_ip = None
        
        self.print = color.print_
        self.input = color.input_
        
        try:
            self.load()
            self.console()
        except Exception as data:
            log.crash(data)
            exit()

    def load(self):
        cmd.do(["title Sunset", "mode con: cols=120 lines=30", "cls"])
        for _ in range(15):
            print()
        self.print("light_black", "loading...".center(120), save=False)
        for _ in range(14):
            print()
        
        install.sunset()
        install.driver(self.driver_version)
        
    def start(self):
        configuration = config.load("assets/config.json")
        while True:
            for _ in range(self.accounts_per_ip):
                if proxy.data.enabled and proxy.data.current == len(proxy.data.list):
                    proxy.data.enabled = False
                    self.print("light_black", "All proxies have been used, skipping cycle...\n")
                    break
                
                credentials = account.generate_credentials(configuration["account-domain-name"])
                driver = chrome.start(self.driver_version)

                driver.get("https://account.microsoft.com/account?lang=en-en")

                self.print("light_black", "Generating account...")
                if chrome.is_displayed(driver, "id__10"):
                    chrome.wait_for_element(driver, "id__10").click()
                else:
                    chrome.wait_for_element(driver, "createaccounthero").click()

                chrome.wait_for_element(driver, "MemberName").send_keys(credentials["email"])
                chrome.wait_for_element(driver, "iSignupAction").click()

                chrome.wait_for_element(driver, "PasswordInput").send_keys(credentials["password"])
                chrome.wait_for_element(driver, "iOptinEmail").click()
                chrome.wait_for_element(driver, "iSignupAction").click()
                
                entered_country, entered_age = False, False
                if chrome.is_displayed(driver, "Country"):
                    chrome.wait_for_element(driver, "Country").send_keys(credentials["country"])
                    entered_country = True
                if chrome.is_displayed(driver, "BirthMonth"):
                    chrome.wait_for_element(driver, "BirthMonth").send_keys(credentials["birthmonth"])
                    chrome.wait_for_element(driver, "BirthDay").send_keys(credentials["birthday"])
                    chrome.wait_for_element(driver, "BirthYear").send_keys(credentials["birthyear"])
                    entered_age = True
                if chrome.is_displayed(driver, "iSignupAction") and entered_country or entered_age:
                    chrome.wait_for_element(driver, "iSignupAction").click()
                
                if chrome.is_displayed(driver, "wlspispHipControlButtonsContainer"):
                    driver.quit()
                    self.print("light_black", "Phone verification detected, skipping cycle...\n")
                    break
                else:
                    chrome.wait_for_element(driver, "enforcementFrame")
                    self.print("light_black", "Complete the bot verification to continue...")
                    
                    chrome.wait_for_element(driver, "KmsiCheckboxField").click()
                    chrome.wait_for_element(driver, "idBtn_Back").click()
                    
                    account.save(credentials, configuration["account-file-directory"], configuration["account-file-name"], configuration["account-file-extension"])
                    self.print("light_black", "Account generated and stored successfully!\n")

                    driver.quit()
                    sleep(1)
            
            cycle_phrase = "Finished generation cycle, once you have changed your IP press ENTER to resume or any other key to exit..."
            if proxy.data.enabled:
                cycle_phrase = "Finished generation cycle, once you're ready press ENTER to resume or any other key to exit..."
                proxy.data.current += 1
            self.print("yellow", cycle_phrase)
            print()
            
            pressed_key = getch()
            if pressed_key.lower() != b"\r":
                break
        exit()

    def console(self):
        cmd.do(["cls"])
        self.print("light_blue", assets.get_banner("assets/banners.json"))
        sleep(1)
        self.print("cyan", "\nWelcome to Sunset!\n")
        sleep(.25)

        if self.input("yellow", "Do you want to generate new Microsoft Accounts? (y, n) : ").lower().replace(" ", "") != "y":
            exit()

        if self.input("yellow", "Do you want to edit the current configuration? (y, n) : ").lower().replace(" ", "") == "y":
            cmd.do(["cls"])
            config.edit("assets/config.json", config.load("assets/config.json"), assets.get_config_banner("assets/banners.json"))
            cmd.do(["cls"])
            color.load_history()
        
        self.accounts_per_ip = int(self.input("yellow", "How many accounts do you want to generate per IP? (min 1, max 3) : ").lower().replace(" ", ""))
        if self.accounts_per_ip > 3:
            self.accounts_per_ip = 3
        elif self.accounts_per_ip < 1:
            self.accounts_per_ip = 1
        
        if os.path.exists("proxies.txt") and os.path.getsize("proxies.txt") != 0 and self.input("yellow", "Do you want to use proxies? (y, n) : ").lower().replace(" ", "") == "y":
            proxy.data.enabled = True
            if self.input("yellow", "Do you want check the proxies before using them? (y, n) : ").lower().replace(" ", "") == "y":
                proxy.data.check = True
            proxy.parse_proxies()

        self.print("cyan", "\nStarting... (if the captcha doesn't work change IP)\n")
        sleep(1)
        self.start()

Sunset()
