from random import randint
import os

def crash(data):
    if not os.path.exists("crashlogs"):
        os.mkdir("crashlogs")

    with open(f"crashlogs/crash-{randint(100000, 999999)}.log", "w+") as crash:
        crash.write(str(data))
        crash.close()
