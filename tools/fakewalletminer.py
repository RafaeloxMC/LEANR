from colorama import Fore, Back, Style
import os
import random
from time import sleep

pre = Fore.WHITE + "[" + Fore.GREEN + "~" + Fore.WHITE + "] "

def main():
    targetwallet = input(pre + Fore.MAGENTA + "Enter your wallet address: " + Fore.RESET)
    i = 0
    while(True):
        i+=1;
        letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        random_letters = ""
        for int in range(0, 20):
            random_letters += letters[random.randint(0, len(letters)-1)]
        numbers = "0123456789"
        random_numbers = ""
        for int in range(0, 9):
            random_numbers += numbers[random.randint(0, len(numbers)-1)]
        if i % random.randint(5000, 1000000) == 0:
            print(pre + Fore.MAGENTA + str(i) + Fore.RESET + " | " + Fore.MAGENTA + " Wallet address: " + random_letters + Fore.RESET + " | " + Fore.MAGENTA + " Balance: "+ str(random.randint(0, 4)) + "." + str(random_numbers) + " BTC" + Fore.RESET)
            sleep(3)
        else:
            print(pre + Fore.MAGENTA + str(i) + Fore.RESET + " | " + Fore.MAGENTA + " Wallet address: " + random_letters + Fore.RESET + " | " + Fore.MAGENTA + " Balance: 0.000000000 BTC" + Fore.RESET)

main()