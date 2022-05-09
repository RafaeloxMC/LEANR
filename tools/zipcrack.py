import zipfile
import colorama
from colorama import Fore, Back, Style
from time import sleep
from datetime import datetime
import os
pre = Fore.WHITE + "[" + Fore.GREEN + "~" + Fore.WHITE + "] "
os.system("title LEANR - ZipCrack")
zip_file = input(pre + Fore.MAGENTA + "Enter path of the zip file: " + Fore.RESET)

os.system("cd ./output/zipcrack/")
foldername = str(datetime.now().strftime("%Y-%m-%d-%H-%M-%S"))
os.system("mkdir " + str(foldername))

def extract_zip(zip_file, password):
    try:
        zip_file.extractall("./output/zipcrack/" + str(foldername), pwd=bytes(password, 'utf-8'))
        return password
    except:
        print(Fore.RED + "[X] Password not found: " + password + Fore.RESET)
        return 

def main():
    print(Fore.GREEN + "Starting..." + Fore.RESET)
    zfile = zipfile.ZipFile(zip_file)
    while open("tools/passlist.txt", "r"):
        for line in open("tools/passlist.txt", "r").readlines():
            password = line.strip('\n')
            guess = extract_zip(zfile, password)
            if guess:
                print(Fore.GREEN + "[+] Password found: " + guess + Fore.RESET)
                os.system("rmdir /s /q ./../../" + str(foldername) + "/")
                os.system("rmdir /s /q ./" + str(foldername) + "/")
                exit()
                

if __name__ == "__main__":
    main()

#fh = open('test.zip', 'rb')
#z = zipfile.ZipFile(fh)
#for name in z.namelist():
#    outpath = "C:\\"
#    z.extract(name, outpath)
#fh.close()

#with zipfile.ZipFile('test.zip', "r") as z:
#    z.extractall("C:\\")
