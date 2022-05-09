import requests
from colorama import Fore, Back, Style
from time import sleep
import os
pre = Fore.WHITE + "[" + Fore.GREEN + "~" + Fore.WHITE + "] "
os.system("title LEANR - Pastebin Stealer")
raw_link = input(pre + Fore.MAGENTA + "Enter the link of the paste (raw: e.g. https://pastebin.com/raw/aAbBcC123): "+ Fore.RESET)
name = input(pre + Fore.MAGENTA + "Enter the name of the file(.txt or something): " + Fore.RESET)
print(Fore.GREEN + "Installing..." + Fore.RESET)
restult = requests.get(raw_link)
with open("output/pastebin/"+name, "w") as file:
    file.write(restult.text)
    file.close()

print(Fore.GREEN + "Done!" + Fore.RESET)
#https://pastebin.com/raw/t908yfgm