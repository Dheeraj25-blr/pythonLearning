import requests
from requests.auth import HTTPBasicAuth
from getpass import getpass
import json

csr_username = input("Enter the username: ")
csr_password = getpass("Enter the password: ")

csr_url = "https://192.168.11.217/restconf/data/ietf-interfaces:interfaces/interface=GigabitEthernet2"


csr_creds = HTTPBasicAuth(username = csr_username, password = csr_password)

csr_headers = {"Content-Type":"application/yang-data+json"}

int_payload = {
  "ietf-interfaces:interface": {
      "name": "GigabitEthernet2",
      "description": "Configured using RESTCONF",
      "type": "iana-if-type:ethernetCsmacd",
      "enabled": True,
      "ietf-ip:ipv4": {
          "address": [
              {
                  "ip": "12.10.10.1",
                  "netmask": "255.255.255.0"
              }
          ]
      }
  }
}

int_conf = requests.put(url = csr_url, auth = csr_creds, headers = csr_headers, data = json.dumps(int_payload), verify = False)

print(int_conf.text)
print(int_conf.status_code)