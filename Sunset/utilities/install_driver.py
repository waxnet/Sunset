from utilities import log
import requests
import zipfile
import os

def run(driver_version):
    try:
        drivers_folder = os.getenv("appdata") + "/Sunset/drivers"
        for file in os.listdir(drivers_folder):
            if file.replace(".exe", "") != driver_version:
                os.remove(f"{drivers_folder}/{file}")
        
        if os.path.exists(f"{drivers_folder}/{driver_version}.exe"):
            return True

        request = requests.get(f"https://chromedriver.storage.googleapis.com/{driver_version}/chromedriver_win32.zip")
        if not request.ok:
            return False
        
        zipped_driver_directory = f"{drivers_folder}/driver.zip"
        with open(zipped_driver_directory, "wb") as zipped_driver:
            zipped_driver.write(request.content)
            zipped_driver.close()
            with zipfile.ZipFile(zipped_driver_directory,"r") as zipped_driver:
                zipped_driver.extractall(drivers_folder)
        os.remove(zipped_driver_directory)
        if os.path.exists(f"{drivers_folder}/LICENSE.chromedriver"):
            os.remove(f"{drivers_folder}/LICENSE.chromedriver")
        os.rename(f"{drivers_folder}/chromedriver.exe", f"{drivers_folder}/{driver_version}.exe")
        return True
    except:
        return False
