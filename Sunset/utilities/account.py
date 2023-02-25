from string import digits, punctuation, ascii_letters
from random import randint, sample, choice
import os

def generate_credentials():
    account = {}

    holder = (
        "".join(sample(ascii_letters, randint(5, 6))),
        "".join(sample(ascii_letters, randint(5, 6)))
    )

    account["email"] = holder[0] + holder[1] + "@outlook.com"
    
    account["password"] = "".join(sample(ascii_letters + digits + punctuation, 10))

    account["country"] = choice(["United States", "United Kingdom", "Canada", "Australia", "Ireland"])
    
    account["birthmonth"] = choice(["May", "October", "January", "March", "July", "August", "December"])
    account["birthday"] = randint(1, 31)
    account["birthyear"] = randint(2000, 2004)

    return account

def save(credentials, directory, file_name, extension):
    if directory == "default":
        directory = os.getcwdb().decode() + "\\"
    if file_name == "default":
        file_name = "sunset_accounts"
    if extension == "default":
        extension = ".txt"
    accounts_directory = f"{directory}{file_name}{extension}"
    
    if os.path.exists(accounts_directory):
        with open(accounts_directory, "r") as previous_accounts:
            start_of_file = previous_accounts.read()
            previous_accounts.close
    else:
        start_of_file = "Accounts generated with Sunset!"

    with open(accounts_directory, "w+") as accounts_file:
        accounts_file.write(f"{start_of_file}\n\nEmail : " + credentials["email"] + "\nPassword : " + credentials["password"])
        accounts_file.close()
