from netmiko import ConnectHandler
from getpass import getpass

router_dictionary = {
    "R1": "192.168.10.87",
    "R2": "192.168.10.88",
    "R3": "192.168.10.89"
}

print(router_dictionary)

user_choice = input("Select the router which you would like to configure (R1/R2/R3):  ")
user_choice = user_choice.upper()

router_ip = router_dictionary[user_choice]

router_details = {
    "ip": router_ip,
    "device_type": "cisco_ios",
    "username": input("Enter the username: "),
    "password": getpass("Enter the password: ")
}

ssh = ConnectHandler(**router_details)
print("The Connection was established with  "  +  router_ip)

user_input = int(input("Enter the number of interfaces you would like to configure:  "))
for interface in range(0, user_input):
    int_name = input("Enter the interface name: ")
    int_ip = input("Enter the interface IP:  ")
    int_mask = input("Enter the interface mask: ")
    desc = input("Enter the interface description: ")

    commands = ["interface " + int_name, "ip address " + int_ip +"  " + int_mask, "description " + desc, "no shutdown"]
    int_configs = ssh.send_config_set(commands)
    print(int_configs)

    int_details = ssh.send_command("show ip interface brief")

    print(int_details)
