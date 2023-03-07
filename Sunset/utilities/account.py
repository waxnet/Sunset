from string import digits, punctuation, ascii_letters
from random import randint, sample, choice
import os

def generate_credentials(domain):
    account = {}

    holder = (
        "".join(sample(ascii_letters, randint(5, 6))),
        "".join(sample(ascii_letters, randint(5, 6)))
    )
    if domain == "default":
        domain = "outlook"
    account["email"] = f"{holder[0]}{holder[1]}@{domain}.com"
    
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
    account_directory = f"{directory}{file_name}{extension}"
    
    if os.path.exists(account_directory):
        with open(account_directory, "r") as previous_account:
            start_of_file = previous_account.read()
            previous_account.close
    else:
        start_of_file = "Accounts generated with Sunset!"

    with open(account_directory, "w+") as account_file:
        account_file.write(f"{start_of_file}\n\nEmail : " + credentials["email"] + "\nPassword : " + credentials["password"])
        account_file.close()
