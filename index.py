#https://github.com/IStuniI/LEANR.git
#main imports
import os
import sys
from time import sleep

os.system("@echo off")
os.system("pip install -r requirements.txt")
os.system("cls")

#imports from requirements.txt
from colorama import Fore, Back, Style
import requests
import subprocess

#Main VARS
class infos():
    import requests
    version = requests.get("https://raw.githubusercontent.com/RafaeloxMC/LEANR/main/version.md").text

pre = Fore.WHITE + "[" + Fore.GREEN + "~" + Fore.WHITE + "] "





def mainline():
    os.system("title LEANR - The moddable multitool")
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
    print("LEANR - the moddable multitool v" + infos.version + "\n")
    while True:
        commandinput = input(pre + Fore.MAGENTA + Fore.RESET)
        if commandinput.lower() == "restart":
            subprocess.call([sys.executable, os.path.realpath(__file__)] + sys.argv[1:])
            os.system("cls")

        elif commandinput.lower() == "update":
            os.system("cls")
            UpdateCheck()



        else:
            if os.path.exists("tools/"+commandinput + ".py"):
                os.system("python tools/"+commandinput + ".py")
            else:
                print(pre + Fore.RED + "Command not found." + Fore.RESET)
                















def Boot(): #check if files exist
    if not os.path.exists("tools"):
        print(pre + Fore.RED + "Error: tools folder not found.Please RE-INSTALL" + Fore.RESET)
        sleep(10000)
    if not os.path.exists("license.txt"):
        print(pre + Fore.RED + "Error: license.txt not found.Please RE-INSTALL" + Fore.RESET)
        sleep(10000)
    if not os.path.exists("requirements.txt"):
        print(pre + Fore.RED + "Error: requirements.txt not found.Please RE-INSTALL" + Fore.RESET)
        sleep(10000)
    if not os.path.exists("output"):
        print(pre + Fore.RED + "Error: output folder not found.Please RE-INSTALL" + Fore.RESET)
        sleep(10000)
    startup()
        


def startup():
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
    print("LEANR - the moddable multitool v" + infos.version)
    print(pre + Fore.MAGENTA + "Copyright (C) 2022 LEANR" + Fore.RESET)
    sleep(1)
    UpdateCheck()

def UpdateCheck():
    os.system("cls")
    print(pre + Fore.MAGENTA + "Checking for updates..." + Fore.RESET)
    try:
        r = requests.get("https://raw.githubusercontent.com/RafaeloxMC/LEANR/main/version.md")
        if r.status_code == 200:
            if infos.version != r.text:
                print(Fore.MAGENTA + "There is a new version available! Download it here:")
                sys.exit()
    except:
        print(pre + "Couldn't connect to the servers. Please check your internet connection.")
        sys.exit()
    print(pre + Fore.MAGENTA + "No updates available." + Fore.RESET)
    LicenseCheck()

def LicenseCheck():
    os.system("cls")
    with open("license.txt", "r") as f:
        last_line = f.readlines()[-1]
        if last_line.lower() == "iaccept=true":
            print(Fore.GREEN + "License accepted.")
            sleep(1)
            os.system("cls")
            mainline()

        else:
            print(Fore.RED + "License not accepted. Please accept the license to continue.")
            sleep(100)
            

Boot()

#MADE BY Stein#7722 AND Rаfа#1872
#
#COPYRIGHT 2022