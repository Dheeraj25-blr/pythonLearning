from ncclient import manager
from getpass import getpass

username = input("Enter your username: ")
password = getpass("Enter your password: ")

router_details = {
    "host" : "192.168.10.92",
    "port" : 830,
    "username" : username,
    "password" : password,
    "hostkey_verify" : False
}

netconf = manager.connect(**router_details)
print("NETCONF Connection was established successfully: ")

user_choice = int(input("Enter the number of interfaces would you like to wish..!: "))
for ip in range(0, user_choice):

    user_choice = int(input("Please select the interface you would wish.\n1. Physical Interface\n2. Loopback Interface\nPlease make a choice(1/2): "))

    if user_choice == 1:
        int_type = "ethernetCsmacd"
    elif user_choice == 2:
        int_type = "softwareLoopback"
    else:
        print("Invalid input detected. Please try again...")

    int_name = input("Enter the interface name: ")
    int_ip = input("Enter the interface ip address: ")
    int_mask = input("Enter the interface subnet mask: ")
    int_desc = input("Enter the interface description: ")

int_payload = f"""
    <config>
        <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
            <interface>
                <name>{int_name}</name>
                <description>{int_desc}</description>
                <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:{int_type}</type>
                <enabled>true</enabled>
                <ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
                    <address>
                        <ip>{int_ip}</ip>
                        <netmask>{int_mask}</netmask>
                        </address>
                    </ipv4>
                    <ipv6 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip"/>
            </interface>
        </interfaces>
    </config>
    """

int_config = netconf.edit_config(int_payload, target = "running")
print(int_config)
