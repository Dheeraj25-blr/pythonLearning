from ncclient import manager
from getpass import getpass
from xml.dom.minidom import parseString
from xmltodict import parse

username = input("Enter your username: ")
password = getpass("Enter your password: ")

router_details = {
    "host" : "192.168.10.238",
    "port" : 830,
    "username" : username,
    "password" : password,
    "hostkey_verify" : False
}

netconf = manager.connect(**router_details)
print("NETCONF Connection was established successfully: ")


    
int_filter = """
<filter>
    <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
            <interface>
                
            </interface>
    </interfaces>
</filter>
"""

running_conf = netconf.get_config(filter = int_filter, source = "running")
pretty_output = parseString(running_conf.xml).toprettyxml()
print(pretty_output)

int_dict = parse(pretty_output)
print(int_dict['rpc-reply'],['name'])
