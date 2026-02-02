from netmiko import ConnectHandler

R1 = {
    "ip": "192.168.11.3",
    "username": "admin",
    "password": "cisco",
    "device_type": "cisco_ios"
}

ssh = ConnectHandler(**R1)

print("Connection with Router 1 established Successfully")

user_input = int(input("How many interfaces would you like to configure:  "))

for interface in range(0, user_input):


    int_name = input("Enter the interface name:  ")
    int_ip = input("Enter the interface IP:  ")
    int_mask = input("Enter the interface mask:  ")
    int_desc = input("Enter the interface description:  ")

    commands = ["interface " + int_name, "ip address " + int_ip + " " + int_mask, "desc " + int_desc, "no shutdown"]
    int_conf = ssh.send_config_set(commands)
    print(int_conf)

    int_details = ssh.send_command("Show ip interface brief")
    print(int_details)

    ssh.save_config()
   
