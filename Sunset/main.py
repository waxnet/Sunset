from utilities import (
    install_sunset, 
    install_driver,
    account,
    config,
    chrome,
    assets,
    color,
    cmd,
)
from msvcrt import getch
from time import sleep

class Sunset:
    def __init__(self):
        super(Sunset, self).__init__()
        
        self.driver_version = "110.0.5481.77"
        self.accounts_per_ip = None
        
        self.print = color.print_
        self.input = color.input_

        self.install()
        self.console()

    def install(self):
        is_sunset_installed = install_sunset.run()
        is_driver_installed = install_driver.run(self.driver_version)
        if not is_sunset_installed or not is_driver_installed: exit()

    def start(self):
        chrome.timeout = 60
        configuration = config.load("assets/config.json")
        while True:
            for _ in range(self.accounts_per_ip):
                credentials = account.generate_credentials()
                driver = chrome.start(self.driver_version)

                driver.get("https://account.microsoft.com/account?lang=en-en")

                self.print("light_black", "Generating account...")
                if chrome.is_displayed(driver, "createaccounthero"): chrome.wait_for_element(driver, "createaccounthero").click()
                else: chrome.wait_for_element(driver, "id__10").click()

                chrome.wait_for_element(driver, "MemberName").send_keys(credentials["email"])
                chrome.wait_for_element(driver, "iSignupAction").click()

                chrome.wait_for_element(driver, "PasswordInput").send_keys(credentials["password"])
                chrome.wait_for_element(driver, "iOptinEmail").click()
                chrome.wait_for_element(driver, "iSignupAction").click()

                chrome.wait_for_element(driver, "Country").send_keys(credentials["country"])
                chrome.wait_for_element(driver, "BirthMonth").send_keys(credentials["birthmonth"])
                chrome.wait_for_element(driver, "BirthDay").send_keys(credentials["birthday"])
                chrome.wait_for_element(driver, "BirthYear").send_keys(credentials["birthyear"])
                chrome.wait_for_element(driver, "iSignupAction").click()

                chrome.wait_for_element(driver, "enforcementFrame")
                self.print("light_black", "Complete the bot verification to continue...")

                chrome.wait_for_element(driver, "KmsiCheckboxField").click()
                chrome.wait_for_element(driver, "idBtn_Back").click()
                
                account.save(credentials, configuration["accounts-file-directory"], configuration["accounts-file-name"], configuration["accounts-file-extension"])
                self.print("light_black", "Account generated and stored successfully!\n")

                driver.quit()
                sleep(1)
            
            self.print("yellow", "Finished generation cycle, once you have changed your IP press ENTER to resume or any other key to exit..."); print()
            
            pressed_key = getch()
            if pressed_key.lower() != b"\r": exit()

    def console(self):
        cmd.do(["title Sunset", "mode con: cols=120 lines=30", "cls"])

        self.print("light_blue", assets.get_banner("assets/banners.json")); sleep(1)
        self.print("cyan", "\nWelcome to Sunset!\n"); sleep(.25)

        if self.input("yellow", "Do you want to generate new Microsoft Accounts? (y, n) : ").lower().replace(" ", "") != "y": exit()

        if self.input("yellow", "Do you want to edit the current configuration? (y, n) : ").lower().replace(" ", "") == "y":
            cmd.do(["cls"])
            config.edit("assets/config.json", config.load("assets/config.json"), assets.get_config_banner("assets/banners.json"), [self.print, self.input])
            cmd.do(["cls"])
            color.load_history()
        
        self.accounts_per_ip = int(self.input("yellow", "How many accounts do you want to generate per IP? (max 2, min 1) : ").lower().replace(" ", ""))
        if self.accounts_per_ip > 2: self.accounts_per_ip = 2
        elif self.accounts_per_ip < 1: self.accounts_per_ip = 1

        self.print("cyan", "\nStarting... (if you get sent to the phone verification page or the captcha doesn't work change IP)\n"); sleep(3)
        self.start()

Sunset()
