import os
from colorama import Fore
import requests

version = requests.get("https://pastebin.com/raw/t908yfgm").text

os.system("cls")
print(Fore.MAGENTA + """
██▓    ▓█████ ▄▄▄       ███▄    █  ██▀███  
▓██▒    ▓█   ▀▒████▄     ██ ▀█   █ ▓██ ▒ ██▒
▒██░    ▒███  ▒██  ▀█▄  ▓██  ▀█ ██▒▓██ ░▄█ ▒
▒██░    ▒▓█  ▄░██▄▄▄▄██ ▓██▒  ▐▌██▒▒██▀▀█▄  
░██████▒░▒████▒▓█   ▓██▒▒██░   ▓██░░██▓ ▒██▒
░ ▒░▓  ░░░ ▒░ ░▒▒   ▓▒█░░ ▒░   ▒ ▒ ░ ▒▓ ░▒▓░
░ ░ ▒  ░ ░ ░  ░ ▒   ▒▒ ░░ ░░   ░ ▒░  ░▒ ░ ▒░
░ ░      ░    ░   ▒      ░   ░ ░   ░░   ░ 
░  ░   ░  ░     ░  ░         ░    ░     
                                        """ + Fore.RESET)
print("LEANR Multitool v" + version + "\n")