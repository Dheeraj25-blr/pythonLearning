from netmiko import ConnectHandler
from getpass import getpass

username = input("Enter the username: ")
password = getpass("Enter the password: ")

router_details = {
    "ip" : "192.168.11.205",
    "device_type" : "cisco_ios",
    "username" : username,
    "password" : password
}

ssh = ConnectHandler(**router_details)
print("Connection is established using ssh..!: ")

user_input = int(input("""Which routing protocol would you like to configure?
                       1. Static routes
                       2. EIGRP
                       3. OSPF
                       Please make choice (1/2/3) : """))
if user_input == 1:
    print("You have selected Static Routing.\nPlease provide the information below to proceed: ")
    user_input1 = int(input("Enter the number of static routes to configure..!: "))
    for static in range(0, user_input1):
        int_name = input("Enter the interface name: ")
        int_ip = input("Enter the interface IP: ")
        int_mask = input("Enter the interface mask: ")
        desc = input("Enter the interface description: ")

        commands = ["interface " + int_name , "ip address " + int_ip + " " + int_mask, "description " + desc, "no shutdown "]
        int_configs = ssh.send_config_set(commands)
        print(int_configs)

        int_details = ssh.send_commands("show ip interface brief")
        print(int_details)

elif user_input == 2:

    print("You have selected EIGRP rouing.\nPlease Provide the information below to proceed: ")
    user_input2 = int(input("Enter the number of EIGRP to configure..!: "))
    for eigrp in range(0, user_input2):
        as_number = input("Enter the EIGRP AS number: ")
        network = input("Enter the router network ID: ")
        mask = input("Enter the network mask: ")

        commands = [f"router eigrp {as_number}",f"network {network} {mask}","no auto-summary"]
        int_configs = ssh.send_config_set(commands)
        print(int_configs)

        int_details = ssh.send_command("show run | sec eigrp")
        print(int_details)

elif user_input == 3:
    print("You have Selected OSPF routing.\nPlease Provide OSPF information below to configure: ")
    user_input3 = int(input("Enter the OSPF Process ID to configure..!: "))
    for ospf in range(0, user_input3):
        process_id = input("Enter the OSPF Process ID: ")
        network = input("Enter the network ID: ")
        wildcardmask = input("Enter the wildcardmask: ")
        area_id = input("Enter the area ID: ")

        commands = ["router ospf " + str(process_id), "network " + network + " " + wildcardmask  +  " area " + str(area_id)]
        int_configs = ssh.send_config_set(commands)
        print(int_configs)

        int_details = ssh.send_command("show run | sec ospf")
        print(int_details)


        ssh.save_config()

