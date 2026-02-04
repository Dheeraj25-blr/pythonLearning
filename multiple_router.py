from netmiko import ConnectHandler
from getpass import getpass

username = input("Enter the username: ")
password = getpass("Enter the password: ")

R1 = "192.168.11.184"
R2 = "192.168.11.185"
R3 = "192.168.11.187"

devices = [R1, R2, R3]

for router in devices:
    device = {
        "ip": router,
        "device_type":"cisco_ios",
        "username": username,
        "password": password
    }

    ssh = ConnectHandler(**device)
    print("Connection established for routers using ssh" + router)

    user_input = int(input("Enter the interface would you like to wish..!:  "))
    for interface in range(0, user_input):
        int_name = input("Enter the interface name: ")
        int_ip = input("Enter the interface IP:  ")
        int_mask = input("Enter the interface mask: ")
        desc = input("Enter the interface description: ")

        commands = ["interface " + int_name , "ip address " + int_ip + "  " + int_mask, "description " + desc, " no shutdown "]
        int_configs = ssh.send_config_set(commands)
        print(int_configs)

        int_details = ssh.send_command("show ip interface brief")
        print(int_details)

        ssh.save_config()
