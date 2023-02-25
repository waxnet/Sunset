from utilities import log
import os

def run():
    try:
        appdata = os.getenv("appdata")
        if not os.path.exists(f"{appdata}/Sunset"):
            main_folder = f"{appdata}/Sunset"
            os.mkdir(main_folder)
            os.mkdir(f"{main_folder}/drivers")
        return True
    except:
        return False
