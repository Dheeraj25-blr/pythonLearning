from netmiko import ConnectHandler
from getpass import getpass

username = input("Enter the username: ")
password = getpass("Enter the password: ")

router_details = {
    "ip": "192.168.11.73",
    "username": username,
    "password": password,
    "device_type": "cisco_ios"
}

ssh = ConnectHandler(**router_details)

print("Connection with router 1 established successfully")

user_input = int(input("Enter the number of eigrp that you wish to configure: "))
for i in range(0, user_input):
    as_number = input("Enter the EIGRP AS number: ")
    network = input("Enter the network ID: ")
    

    commands = [f"router eigrp {as_number}", f"network {network}","no auto-summary","exit" ] 
    eigrp_configs = ssh.send_config_set(commands)
    print(eigrp_configs)

    eigrp_details = ssh.send_command("show ip eigrp neighbors")
    print(eigrp_details)

    ssh.save_config()
    