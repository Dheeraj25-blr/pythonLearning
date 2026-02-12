from ncclient import manager        #python -m pip install ncclient
from getpass import getpass
from xml.dom.minidom import parseString
from xmltodict import parse         #python -m pip install xmltodict
from pprint import pprint

router_details = {
    'host':'192.168.10.238',
    'username':'admin',
    'password':'cisco',
    'port':'830',
    'hostkey_verify':False
}

netconf = manager.connect(**router_details)
print("NETCONF Connection was created successfully..!")

int_filter = """
<filter>
    <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
    </interfaces>
</filter>
"""

running_conf = netconf.get_config(filter = int_filter, source = "running")
pretty_running_conf = parseString(running_conf.xml).toprettyxml()
int_dict = parse(pretty_running_conf)
int_list = int_dict['rpc-reply']['data']['interfaces']['interface']

for int_details in int_list:
    print(int_details['name'])
    try:
        int_ip = int_details['ipv4']['address']['ip']
    except:
        int_ip = "not configured"

    print("The IP on above mentioned interface is " + int_ip)