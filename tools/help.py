from colorama import Fore, Back, Style
import os

pre = Fore.WHITE + "[" + Fore.GREEN + "~" + Fore.WHITE + "] "

files = os.listdir("tools")
print(pre + Fore.MAGENTA + "Available tools: " + Fore.RESET + "\n")
for file in files:
    if file.endswith(".py"):
        name = file.removesuffix(".py")
        print(" -  " + Fore.MAGENTA + name + Fore.RESET)