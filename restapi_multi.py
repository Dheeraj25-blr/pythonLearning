import requests
from requests.auth import HTTPBasicAuth
from getpass import getpass
import json

asa_username = input("Enter your username: ")
asa_password = getpass("Enter your password: ")

user_choice = int(input("Enter the number of interfaces you would like to configure: "))

for int in range(0, user_choice):
    int_number = input("Enter the interface number you are willing to configure (for ex: If Interface is GigabitEthernet0/3: the number will be 3): ") 



    asa_url = "https://192.168.11.167/api/interfaces/physical/GigabitEthernet0_API_SLASH_{}".format(int_number)

    asa_creds = HTTPBasicAuth(username = asa_username, password = asa_password)

    asa_headers = {"Content-Type":"application/json"}

    int_ip = input("Enter the interface IP: ")
    int_mask = input("Enter the interface mask: ")
    int_desc = input("Enter the interface description: ")
    int_zone = input("Enter the interface Zone name: ")



    int_payload = {
    "securityLevel": 0,
    "kind": "object#GigabitInterface",
    "channelGroupMode": "active",
    "flowcontrolLow": -1,
    "name": int_zone,
    "duplex": "auto",
    "forwardTrafficSFR": False,
    "hardwareID": "GigabitEthernet0/{}".format(int_number),
    "mtu": 1500,
    "lacpPriority": -1,
    "flowcontrolHigh": -1,
    "ipAddress": {
        "ip": {
        "kind": "IPv4Address",
        "value": int_ip
        },
        "kind": "StaticIP",
        "netMask": {
        "kind": "IPv4NetMask",
        "value": int_mask
        }
    },
    "flowcontrolOn": False,
    "shutdown": False,
    "interfaceDesc": int_desc,
    "managementOnly": False,
    "channelGroupID": "",
    "speed": "auto",
    "forwardTrafficCX": False,
    "flowcontrolPeriod": -1
    }


    query = requests.put(url = asa_url, auth = asa_creds, headers = asa_headers, data = json.dumps(int_payload), verify = False)

    print(query.status_code)
    print(query.text)