from datetime import datetime
import shutil
import json

date = datetime.now()
day, month, year = date.day, date.month, date.year
console_columns = shutil.get_terminal_size().columns

def get_banner(banners_file):
    loaded_banners = json.load(open(banners_file, encoding="utf-8"))
    banner = ""

    if day == 25 and month == 12: parts = loaded_banners["christmas"].splitlines()
    elif day == 31 and month == 10: parts = loaded_banners["halloween"].splitlines()
    elif day == 1 and month == 1: parts = loaded_banners["new-year"].splitlines()
    else: parts = loaded_banners["default"].splitlines()

    for part in parts: banner = banner + part.center(console_columns) + "\n"

    return banner

def get_config_banner(banners_file):
    loaded_banners = json.load(open(banners_file, encoding="utf-8"))
    banner = ""

    parts = loaded_banners["config"].splitlines()

    for part in parts: banner = banner + part.center(console_columns) + "\n"

    return banner
