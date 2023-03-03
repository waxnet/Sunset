from time import sleep
import json
import os

def edit(config_file, current_config, banner, output_input):
    animation = True
    while True:
        new_config = current_config
        print_, input_ = output_input[0], output_input[1]

        print_("light_blue", banner, save=False)
        if animation:
            sleep(1)
        print_("cyan", "\nConfig options :\n - back\n - file directory : " + new_config["accounts-file-directory"] + "\n - file name : " + new_config["accounts-file-name"] + "\n - file extension : " + new_config["accounts-file-extension"], save=False)
        print_("cyan", "(1 = back, 2 = file directory, etc...)", save=False)
        if animation:
            sleep(.5)

        option = input_("yellow", "\nSelect an option : ", save=False)
        match option:
            case "1":
                break
            case "2":
                new_directory = input_("yellow", "Set new accounts file directory : ", save=False)
                
                if "\\" in new_directory and not new_directory.endswith("\\") and new_directory != "default":
                    new_directory = f"{new_directory}\\"
                elif "/" in new_directory and not new_directory.endswith("/") and new_directory != "default":
                    new_directory = f"{new_directory}/"
                
                if not os.path.exists(new_directory):
                    new_directory = "default"
                
                new_config["accounts-file-directory"] = new_directory
            case "3":
                new_name = input_("yellow", "Set new accounts file name : ", save=False)
            
                invalid_new_name = False
                for blacklisted_character in ["<", ">", ":", "\"", "/", "\\", "|", "?", "*"]:
                    if blacklisted_character in new_name:
                        invalid_new_name = True
                        break
            
                if new_name.replace(" ", "") == "" or invalid_new_name:
                    new_name = "default"
            
                new_config["accounts-file-name"] = new_name
            case "4":
                new_extension = input_("yellow", "Set new accounts file extension : ", save=False)
            
                invalid_new_extension = False
                for blacklisted_character in ["<", ">", ":", "\"", "/", "\\", "|", "?", "*"]:
                    if blacklisted_character in new_extension:
                        invalid_new_extension = True
                        break
            
                if new_extension.replace(" ", "") == "" or invalid_new_extension:
                    new_extension = "default"
            
                new_config["accounts-file-extension"] = new_extension
        
        if animation:
            animation = False
        os.system("cls")

    with open(config_file, "w+") as config:
        config.write(json.dumps(new_config))
        config.close()

def load(config_file):
    loaded_config = json.load(open(config_file, encoding="utf-8"))
    return {
        "accounts-file-directory" : loaded_config["accounts-file-directory"],
        "accounts-file-name" : loaded_config["accounts-file-name"],
        "accounts-file-extension" : loaded_config["accounts-file-extension"]
    }
