from colorama import Fore, Back, Style

import subprocess

pre = Fore.WHITE + "[" + Fore.GREEN + "~" + Fore.WHITE + "] "

print(pre + Fore.MAGENTA + "Your ip adress is: " + Fore.RESET + subprocess.getoutput("curl -s https://api.ipify.org") + Fore.RESET)