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

user_input = int(input("Enter the number of static routes that you wish to configure: "))
for static in range(0, user_input):

    nw_id = input("Enter the network ID: ")
    mask = input("Enter the subnet mask: ")
    next_hop = input("Enter the next hop address: ")

    commands = ["ip route " + nw_id + " " + mask + " " + next_hop]
    static_configs = ssh.send_config_set(commands)
    print(static_configs)

    static_details = ssh.send_command("show run | inc ip route")
    print(static_details)

    ssh.save_config()
    