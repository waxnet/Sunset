from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from win32api import GetSystemMetrics
from selenium import webdriver
import os

timeout = 0

def start(driver_version):
    driver_directory = os.getenv("appdata") + f"/Sunset/drivers/{driver_version}.exe"

    driver_options = webdriver.ChromeOptions()
    driver_options.add_argument("--log-level=OFF")
    driver_options.add_experimental_option("prefs", {
        "credentials_enable_service" : False,
        "profile.password_manager_enabled" : False
    })
    driver_options.add_experimental_option("excludeSwitches", ["enable-logging"])

    size = (450, 600)
    position = (round(GetSystemMetrics(0) / 2 - size[0] / 2), round(GetSystemMetrics(1) / 2 - size[1] / 2))

    driver = webdriver.Chrome(executable_path=driver_directory, options=driver_options)
    driver.set_window_position(position[0], position[1])
    driver.set_window_size(size[0], size[1])

    return driver

def wait_for_element(driver, id):
    try: return WebDriverWait(driver, timeout).until(expected_conditions.visibility_of_element_located((By.ID, id)))
    except: exit()

def is_displayed(driver, id):
    try:
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.ID, id)))
        return True
    except: return False
