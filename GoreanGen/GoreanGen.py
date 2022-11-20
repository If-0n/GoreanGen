import os
from turtle import color, title
import subprocess
from subprocess import call
from colorama import Fore, Back, Style
import requests
import random

def banner():
        print(f" ")
        print(f" ")
        print(Fore.MAGENTA+ f" $$$$$$\                                                     $$$$$$\                      ")
        print(Fore.MAGENTA+ f"$$  __$$\                                                   $$  __$$\                     ")
        print(Fore.MAGENTA+ f"$$ /  \__| $$$$$$\   $$$$$$\   $$$$$$\   $$$$$$\  $$$$$$$\  $$ /  \__| $$$$$$\  $$$$$$$\  ")
        print(Fore.MAGENTA+ f"$$ |$$$$\ $$  __$$\ $$  __$$\ $$  __$$\  \____$$\ $$  __$$\ $$ |$$$$\ $$  __$$\ $$  __$$\ ")
        print(Fore.MAGENTA+ f"$$ |\_$$ |$$ /  $$ |$$ |  \__|$$$$$$$$ | $$$$$$$ |$$ |  $$ |$$ |\_$$ |$$$$$$$$ |$$ |  $$ |")
        print(Fore.MAGENTA+ f"$$ |  $$ |$$ |  $$ |$$ |      $$   ____|$$  __$$ |$$ |  $$ |$$ |  $$ |$$   ____|$$ |  $$ |")
        print(Fore.MAGENTA+ f"\$$$$$$  |\$$$$$$  |$$ |      \$$$$$$$\ \$$$$$$$ |$$ |  $$ |\$$$$$$  |\$$$$$$$\ $$ |  $$ | ")
        print(Fore.MAGENTA+ f" \______/  \______/ \__|       \_______| \_______|\__|  \__| \______/  \_______|\__|  \__| 1.4")
        print(f" ")
        print(f" ")
banner()

while True:
    genorcheck = input(f"{Fore.CYAN}> Generate or Check? (g/c): {Fore.RED}")

    def generate():
        lowercase = "abcdefghijklmnopqrstuvwxyz"
        uppercase = "ABCDEFGHIJKLMNOPQRSTUVWYYZ"
        numbers = "0123456789"

        amount = int(input(f"{Fore.CYAN}> How many to Generate: {Fore.RED}"))
        upper, lower, nums = True, True, True
        all = ""

        if upper:
            all += uppercase
        if lower:
            all += lowercase
        if nums:
            all += numbers

            count = 0
            length = 16
            n = open('nitros.txt', 'w+')
            for x in range(amount):
                code = "".join(random.sample(all,length))
                n.write(code + "\n")
                count += 1
                print(f"{Fore.RED}{code}{Fore.CYAN} | Code Written ({Fore.RED}nitros.txt{Fore.CYAN}){Fore.RED} - x{count}{Fore.CYAN}/{Fore.RED}{amount}{Fore.CYAN}")

    def check():
        with open("nitros.txt", "r") as nitrofile:
            nitros = nitrofile.read().split("\n")
        nitrofile.close()
        with open("proxies.txt", "r") as proxyfile:
            proxies = proxyfile.read().split("\n")
        proxyfile.close()
        count = 0
        for i in range(len(nitros)):
            nitro = nitros[i]
            proxy = proxies[i]
            ProxyParam = {"http://": proxy, "https://": proxy}
            checkurl = requests.get(f"https://discordapp.com/api/v6/entitlements/gift-codes/{nitro}", proxies=ProxyParam, timeout=3)
            if checkurl.status_code == 200:
                count+=1
                print(f"{Fore.CYAN}[+] {Fore.GREEN}{nitro}{Fore.CYAN} | Valid Code{Fore.RED} - x{count}{Fore.CYAN}/{Fore.RED}{len(nitros)-1}")
            else:
                count+=1
                print(f"{Fore.CYAN}[+] {Fore.RED}{nitro}{Fore.CYAN} | Invalid Code{Fore.RED} - x{count}{Fore.CYAN}/{Fore.RED}{len(nitros)-1}")

    def scrapeproxies():
        input(f"{Fore.CYAN}> Press ENTER To Scrape HTTP Proxies")
        url = requests.get("https://api.openproxylist.xyz/http.txt")
        urlresult = url.text
        linecount = 0
        with open('proxies.txt', 'w') as proxyscrapelist:
            proxyscrapelist.write(urlresult)
            file = open('proxies.txt')
            for line in file:
                if line != "\n":
                    linecount += 1
            print(f"{Fore.CYAN}[+] Scraped {Fore.RED}{linecount}{Fore.CYAN} Proxies ({Fore.RED}proxies.txt{Fore.CYAN})")
            file.close()
            input(f"{Fore.CYAN}> Press ENTER To Start Checking")

    if genorcheck == "g":
        generate()
    if genorcheck == "c":
        scrapeproxies()
        check()

