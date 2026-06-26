import requests
import json
import shutil
from colorama import Fore, Style, init
init(autoreset=True)  # Tự động reset màu sau mỗi lần print, không cần reset thủ công

width = shutil.get_terminal_size().columns
def lay_webhook_url():
    try:
        with open("config.json", "r") as file:
            discord_webhook = json.load(file)
    
    except FileNotFoundError:
        discord_webhook = {"discord_webhook_url": ""}
        print("File not found, Webhook has been set to None")
        input()
        pass
    
    if len(discord_webhook["discord_webhook_url"]) == 0:
        print("Cannot find Discord Webhook url, did you put it in?".center(width))
        
        while True:
            print("=====".center(width))
            print("Do you want to add your Discord webhook to our system now? yes/no".center(width))
            put = input(">>>")
            put = str(put)
            if put.lower() == "yes":
                discord_webhook["discord_webhook_url"] = input("Please enter your Discord Webhook: ")
                
                try:
                    with open("config.json", "w") as file: 
                        json.dump(discord_webhook, file, indent=4)
                        return discord_webhook
                        
                except FileNotFoundError:
                    print("There is something ain't right!")
            
            elif put.lower() == "no": 
                return None

            else:
                continue
        
    else: 
        return discord_webhook
    
def gui_discord(message):
    webhook_data = lay_webhook_url()
    if webhook_data is None:
        print(Fore.YELLOW + "WARNING: Because you didn't enter your Discord Webhook, we cannot send your message to Discord.")
        return


    url = webhook_data["discord_webhook_url"]

    payload = {"content": message}
    response = requests.post(url, json=payload)

    if response.status_code == 204:
        print(Fore.GREEN +"Message has been send successfully!".center(width))
    else:
        print(Fore.RED + f"There is something ain't right! Please try again. Your error code is {response.status_code}")
