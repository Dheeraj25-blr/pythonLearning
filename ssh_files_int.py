from netmiko import ConnectHandler
from getpass import getpass

router_ip = open(r"C:\Users\Dheeraj.k\Documents\python\pythonLearning\routers.txt", "r")

for abc in router_ip:

    print("The connection is initialized with " + abc)

    username_r = input("Enter the username: ")
    password_r = getpass("Enter the password: ")

    router_details = {
        "ip": abc,
        "device_type" : "cisco_ios",
        "username" : username_r,
        "password" : password_r
    }

    ssh = ConnectHandler(**router_details)
    print("SSH connection was established successfully with " + abc)

    commands_file = open(r"C:\Users\Dheeraj.k\Documents\python\pythonLearning\commands.txt", "r")
    output_file = open(r"C:\Users\Dheeraj.k\Documents\python\pythonLearning\output.txt", "a")

    for show_command in commands_file:
        details = ssh.send_command(show_command)
        output_file.write("\nThe below information is fetched from  " + abc)
        output_file.write("\n" + details + "\n")
    output_file.close()
    commands_file.close()
    ssh.disconnect()
    print("Output exported Successfully.....!")
router_ip.close