import requests
from requests.auth import HTTPBasicAuth
from getpass import getpass
import json

asa_username = input("Enter your username: ")
asa_password = getpass("Enter your password: ")

asa_url = "https://192.168.11.167/api/interfaces/physical/GigabitEthernet0_API_SLASH_1"

asa_creds = HTTPBasicAuth(username = asa_username, password = asa_password)

asa_headers = {"Content-Type":"application/json"}

int_payload = {
  "securityLevel": 0,
  "kind": "object#GigabitInterface",
  "channelGroupMode": "active",
  "flowcontrolLow": -1,
  "name": "gig1",
  "duplex": "auto",
  "forwardTrafficSFR": False,
  "hardwareID": "GigabitEthernet0/1",
  "mtu": 1500,
  "lacpPriority": -1,
  "flowcontrolHigh": -1,
  "ipAddress": {
    "ip": {
      "kind": "IPv4Address",
      "value": "192.168.1.6"
    },
    "kind": "StaticIP",
    "netMask": {
      "kind": "IPv4NetMask",
      "value": "255.255.255.0"
    }
  },
  "flowcontrolOn": False,
  "shutdown": False,
  "interfaceDesc": "Add description test",
  "managementOnly": False,
  "channelGroupID": "",
  "speed": "auto",
  "forwardTrafficCX": False,
  "flowcontrolPeriod": -1
}


query = requests.put(url = asa_url, auth = asa_creds, headers = asa_headers, data = json.dumps(int_payload), verify = False)

print(query.status_code)
print(query.text)