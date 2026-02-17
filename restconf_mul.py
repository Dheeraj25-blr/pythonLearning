import requests
from requests.auth import HTTPBasicAuth
from getpass import getpass
import json

csr_username = input("Enter your username: ")
csr_password = getpass("Enter your password: ")


csr_creds = HTTPBasicAuth(username = csr_username, password = csr_password)

csr_headers = {'Content-Type':'application/yang-data+json'}

user_input = int(input("Enter the number of interfaces that you wish to configure on the device: "))

for int_configs in range(0, user_input):

    user_choice = int(input("Select the type of interface that you wish to configure:\n1. Physical Interface\n2. Loopback Interface\nPlease make a choice: "))

    if user_choice == 1:

        int_name = "GigabitEthernet" + input("Enter the interface number (for eg. 1 for Gig1): ")
        csr_url = f"https://192.168.10.114/restconf/data/ietf-interfaces:interfaces/interface={int_name}"
        int_type = "ethernetCsmacd"

    elif user_choice == 2:
        int_name = "Loopback" + input("Enter the Loopback Interface number (for eg. 1 for Loopback1): ")
        csr_url = "https://192.168.10.114/restconf/data/ietf-interfaces:interfaces"
        int_type = "softwareLoopback"

    else:
        break

    int_ip = input("Enter the interface IP address: ")
    int_mask = input("Enter the interface subnet mask: ")
    int_desc = input("Enter the interface description: ")

    int_payload = {
        "interface":{
            "name": int_name,
            "description": int_desc, 
            "type": f"iana-if-type:{int_type}",
            "enabled": True,
            "ietf-ip:ipv4": {
            "address": [
                { 
                "ip": int_ip,
                "netmask": int_mask
                }
            ]
            },
            "ietf-ip:ipv6": {
            }
        }
    }

    if user_choice == 1:
        int_conf = requests.put(url = csr_url, auth = csr_creds, headers = csr_headers, data = json.dumps(int_payload), verify = False)
    elif user_choice == 2:
        int_conf = requests.post(url = csr_url, auth = csr_creds, headers = csr_headers, data = json.dumps(int_payload), verify = False)

    print(int_conf.status_code)
    print(int_conf.text)