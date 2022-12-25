from datetime import datetime
import json
import os

date = datetime.now()
day, month, year = date.day, date.month, date.year
console_x, console_y = os.get_terminal_size()

def get_banner(banners_file):
    loaded_banners = json.load(open(banners_file, encoding="utf-8"))
    banner = ""

    if day == 25 and month == 12: parts = loaded_banners["christmas"].splitlines()
    elif day == 31 and month == 10: parts = loaded_banners["halloween"].splitlines()
    else: parts = loaded_banners["default"].splitlines()

    for part in parts: banner = banner + part.center(console_x) + "\n"

    return banner
