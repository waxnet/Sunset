from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
from utilities import resolve
import os

driver_directory = os.getenv("appdata") + "/Sunset/drivers/driver.exe"
timeout = 0

def set_timeout(seconds):
    global timeout
    timeout = seconds

def start():
    driver_options = webdriver.ChromeOptions()
    driver_options.add_argument("--log-level=OFF")
    driver_options.add_experimental_option("prefs", {
        "credentials_enable_service" : False,
        "profile.password_manager_enabled" : False
    })
    driver_options.add_experimental_option("excludeSwitches",
        ["enable-logging"]
    )

    size = (450, 600)
    position = resolve.position(size)

    driver = webdriver.Chrome(executable_path=driver_directory, options=driver_options)
    driver.set_window_position(position[0], position[1])
    driver.set_window_size(size[0], size[1])

    return driver

def get(driver, url): driver.get(url)

def wait_for_element(driver, id):
    try: return WebDriverWait(driver, timeout).until(expected_conditions.visibility_of_element_located((By.ID, id)))
    except: exit()

def is_displayed(driver, id):
    try:
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.ID, id)))
        return True
    except: return False
