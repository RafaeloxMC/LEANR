import os
from colorama import Fore, Back, Style
print(Fore.RESET)
print(Fore.MAGENTA)
os.system("title LEANR - Pinger")
pre = Fore.WHITE + "[" + Fore.GREEN + "~" + Fore.WHITE + "] "

ip=input(pre + Fore.MAGENTA + "Enter IP: " + Fore.RESET)

def run():
    os.system("ping " + ip)
    run()
run()