from colorama import Fore

colors = {
    "white" : Fore.WHITE,
    "black" : Fore.BLACK,
    "blue" : Fore.BLUE,
    "cyan" : Fore.CYAN,
    "green" : Fore.GREEN,
    "magenta" : Fore.MAGENTA,
    "red" : Fore.RED,
    "yellow" : Fore.YELLOW,

    "light_white" : Fore.LIGHTWHITE_EX,
    "light_black" : Fore.LIGHTBLACK_EX,
    "light_blue" : Fore.LIGHTBLUE_EX,
    "light_cyan" : Fore.LIGHTCYAN_EX,
    "light_green" : Fore.LIGHTGREEN_EX,
    "light_magenta" : Fore.LIGHTMAGENTA_EX,
    "light_red" : Fore.LIGHTRED_EX,
    "light_yellow" : Fore.LIGHTYELLOW_EX,
}
history = []

def load_history():
    for batch in history:
        print(colors[batch[0]] + batch[1] + Fore.RESET)

def print_(color, message, save=True):
    print(colors[color] + message + Fore.RESET)
    if save: history.append([color, message])

def input_(color, message, save=True):
    data = input(colors[color] + message + Fore.RESET)
    if save: history.append([color, message + Fore.RESET + data])
    return data
