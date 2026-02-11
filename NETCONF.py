from ncclient import manager
from getpass import getpass
from xml.dom.minidom import parseString

username = input("Enter your username: ")
password = getpass("Enter your password: ")

device = {
    "host" : "192.168.10.92",
    "port" : 830,
    "username" : username,
    "password" : password,
    "hostkey_verify" : False
}

netconf = manager.connect(**device)
print("NETCONF Connection established with the device successfully")

running_conf = netconf.get_config(source = "running")
print(running_conf)

running_conf = netconf.get_config(source = "running")
pretty_output = parseString(running_conf.xml).toprettyxml()
print(pretty_output)

myfile = open(r"C:\Users\Dheeraj.k\Documents\python\pythonLearning\output.txt", "w")
myfile.write(pretty_output)
print("Configurations exported successfully..!")
