from string import ascii_lowercase
from utilities import color
from time import sleep
import json
import os

def edit(config_file, current_config, banner):
    animation = True
    while True:
        color.print_("light_blue", banner, save=False)
        if animation:
            sleep(1)
        
        new_config = current_config
        current_directory = new_config["account-file-directory"]
        current_file_name = new_config["account-file-name"]
        current_extension = new_config["account-file-extension"]
        current_domain = new_config["account-domain-name"]
        if current_directory == "default":
            current_directory = os.getcwdb().decode() + "\\"
        if current_file_name == "default":
            current_file_name = "sunset_accounts"
        if current_extension == "default":
            current_extension = ".txt"
        if current_domain == "default":
            current_domain = "outlook"
        color.print_("cyan", "\nConfig options :\n - back\n - account file directory : " + current_directory + "\n - account file name : " + current_file_name + "\n - account file extension : " + current_extension + "\n - account domain : " + current_domain, save=False)
        color.print_("cyan", "(1 = back, 2 = file directory, etc...)", save=False)
        
        if animation:
            sleep(.5)
        
        option = color.input_("yellow", "\nSelect an option : ", save=False)
        match option:
            case "1":
                break
            case "2":
                new_directory = color.input_("yellow", "New account file directory : ", save=False)
                
                if "\\" in new_directory and not new_directory.endswith("\\") and new_directory != "default":
                    new_directory = f"{new_directory}\\"
                elif "/" in new_directory and not new_directory.endswith("/") and new_directory != "default":
                    new_directory = f"{new_directory}/"
                
                if not os.path.exists(new_directory):
                    new_directory = "default"
                
                new_config["account-file-directory"] = new_directory
            case "3":
                new_name = color.input_("yellow", "New account file name : ", save=False)
            
                invalid_new_name = False
                for blacklisted_character in ["<", ">", ":", "\"", "/", "\\", "|", "?", "*"]:
                    if blacklisted_character in new_name:
                        invalid_new_name = True
                        break
            
                if new_name.replace(" ", "") == "" or invalid_new_name:
                    new_name = "default"
            
                new_config["account-file-name"] = new_name
            case "4":
                new_extension = color.input_("yellow", "New account file extension : ", save=False).replace(" ", "")
            
                invalid_new_extension = False
                for blacklisted_character in ["<", ">", ":", "\"", "/", "\\", "|", "?", "*"]:
                    if blacklisted_character in new_extension:
                        invalid_new_extension = True
                        break
            
                if new_extension == "" or invalid_new_extension:
                    new_extension = "default"
            
                new_config["account-file-extension"] = new_extension
            case "5":
                new_domain = color.input_("yellow", "New account domain name : ", save=False).replace(" ", "")
            
                invalid_new_domain = False
                if new_domain not in ["outlook", "hotmail"]:
                    invalid_new_domain = True
            
                if new_domain == "" or invalid_new_domain:
                    new_domain = "default"
            
                new_config["account-domain-name"] = new_domain
        
        if animation:
            animation = False
        os.system("cls")

    with open(config_file, "w+") as config:
        config.write(json.dumps(new_config))
        config.close()

def load(config_file):
    loaded_config = json.load(open(config_file, encoding="utf-8"))
    return {
        "account-file-directory" : loaded_config["account-file-directory"],
        "account-file-name" : loaded_config["account-file-name"],
        "account-file-extension" : loaded_config["account-file-extension"],
        "account-domain-name" : loaded_config["account-domain-name"],
    }
