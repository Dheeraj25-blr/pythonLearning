# Define the required libraries
import telnetlib3

# Define important variables
HOST = "192.168.1.2"
user = "Network"
password = "cisco"


#  Using this information for telnet into device 
tn = telnetlib3.Telnet(HOST)

# Handle the Username/Password prompt and supply our values 
tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b'\n')

# Write the commands on the device
tn.write(b'enable\n')
tn.write(b'cisco\n')
tn.write(b'conf ter\n')
tn.write(b'vlan 10\n')
tn.write(b'vlan 20\n')
tn.write(b'vlan 30\n')
tn.write(b'vlan 40\n')
tn.write(b'end\n')
tn.write(b'exit\n')

# Print out what we have done on device with this command
print(tn.read_all().decode())



