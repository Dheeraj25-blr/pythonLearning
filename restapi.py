import requests
from requests.auth import HTTPBasicAuth
from getpass import getpass
import json

asa_username = input("Enter your username: ")
asa_password = getpass("Enter your password: ")
asa_url = "https://192.168.11.167/api/monitoring/device"

asa_creds = HTTPBasicAuth(username = asa_username, password = asa_password)

asa_headers = {"Accept":"application/json"}

device_metric = requests.get(url = asa_url, auth = asa_creds, headers = asa_headers, verify = False)


print(device_metric.status_code)
data = device_metric.text

py_data = json.loads(data)

pretty_data = json.dumps(py_data, indent = 4)
print(pretty_data)