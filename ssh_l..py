from netmiko import ConnectHandler

R1 = {
    "device_type": "cisco_ios",
    "ip": "192.168.10.66",
    "username": "admin",
    "password": "cisco"
}

ssh = ConnectHandler(**R1)

print("Connection with Router 1 established Successfully")

commands = ["interface loopback 0", "ip address 192.168.1.1 255.255.255.0", "description Configured using NETMIKO"]
int_conf = ssh.send_config_set(commands)
print(int_conf)

int_details = ssh.send_command("show ip interface brief")

print(int_details)

ssh.save_config()

ssh.disconnect()