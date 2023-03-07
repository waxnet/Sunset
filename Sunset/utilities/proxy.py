from utilities import color
import requests

class data:
    enabled = False
    check = False
    current = 0
    list = []

def parse_proxies():
    with open("proxies.txt") as proxies_file:
        data.list = proxies_file.readlines()
        proxies_file.close()
    
    if data.check:
        color.print_("light_black", "\nChecking proxies...")
        for proxy in data.list:
            try:
                requests.get("https://account.microsoft.com/account?lang=en-en", proxies={
                    "https" : proxy
                }, timeout=5)
            except:
                data.list.remove(proxy)
        
        good_proxies = len(data.list)
        if good_proxies == 0:
            data.enabled = False
        
        phrase = f"Found {good_proxies} good proxy!"
        if good_proxies > 1 or good_proxies == 0:
            phrase = f"Found {good_proxies} good proxies!"
        
        color.print_("light_black", phrase)
