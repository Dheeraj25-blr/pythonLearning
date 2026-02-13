import requests
from requests.auth import HTTPBasicAuth
from getpass import getpass
import json

csr_username = input("Enter the username: ")
csr_password = getpass("Enter the password: ")


csr_creds = HTTPBasicAuth(username = csr_username, password = csr_password)

csr_headers = {"Content-Type":"application/yang-data+json"}

user_choice = int(input("Enter the name of interfaces which you would you like to configure: "))

for int_configs in range(0, user_choice):

    int_name = input("Enter the interface name: ")
    csr_url = f"https://192.168.11.217/restconf/data/ietf-interfaces:interfaces/interface={int_name}"
    int_ip = input("Enter the interface IP address: ")
    int_mask = input("Enter the interface subnet mask: ")
    int_desc = input("Enter the interface description: ")

int_payload = {
  "ietf-interfaces:interface": {
      "name": int_name,
      "description": int_desc,
      "type": "iana-if-type:ethernetCsmacd",
      "enabled": True,
      "ietf-ip:ipv4": {
          "address": [
              {
                  "ip": int_ip,
                  "netmask": int_mask
              }
          ]
      }
  }
}

int_conf = requests.put(url = csr_url, auth = csr_creds, headers = csr_headers, data = json.dumps(int_payload), verify = False)

print(int_conf.text)
print(int_conf.status_code)