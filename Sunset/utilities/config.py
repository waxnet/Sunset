from time import sleep
import json
import os

def edit(config_file, current_config, banner, output_input):
    animation = True
    while True:
        new_config = current_config
        print_, input_ = output_input[0], output_input[1]

        print_("light_blue", banner, save=False)
        if animation: sleep(1)
        print_("cyan", "\nCurrent config :\n - back\n - file directory : " + new_config["accounts-file-directory"] + "\n - file name : " + new_config["accounts-file-name"] + "\n - file extension : " + new_config["accounts-file-extension"], save=False)
        print_("cyan", "(Use numbers : 1 = return to the generator, 2 = set file directory)", save=False)
        if animation: sleep(0.5)

        option = input_("yellow", "\nSelect an option : ", save=False)
        if option == "1": break
        elif option == "2":
            new_directory = input_("yellow", "Set new accounts file directory : ", save=False)
            if "\\" in new_directory and not new_directory.endswith("\\") and new_directory != "default": new_directory = f"{new_directory}\\"
            elif "/" in new_directory and not new_directory.endswith("/") and new_directory != "default": new_directory = f"{new_directory}/"
            new_config["accounts-file-directory"] = new_directory
        elif option == "3": new_config["accounts-file-name"] = input_("yellow", "Set new accounts file name : ", save=False)
        elif option == "4": new_config["accounts-file-extension"] = input_("yellow", "Set new accounts file extension : ", save=False)
        
        if animation: animation = False
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
