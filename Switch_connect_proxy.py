from jumpssh import SSHSession
# from netmiko import ConnectHandler
import getpass
# import re

device_ip = input("What is the IP of the device? > ")
username = input("Username: ")
password = getpass.getpass("Password: ")
file_name = input("What do you want to name the file? > ")
# remote_ip = "10.1.0.240"
# remote_ip = input("What IP do you want to get to? > ")
# device_command = "show ip int brief"
device_command = input("What command do you want to run? > ")


# establish ssh connection between your local machine and the jump server
gateway_session = SSHSession(device_ip, username, password=password).open()

# print("Connected to TACOBOX")
# print(gateway_session.get_cmd_output(device_command))


# from jump server, establish connection with a remote server
# remote_session = gateway_session.get_remote_session(remote_ip, password=password, retry=3, retry_interval=10)


# command will be executed remotely and output will be returned locally and printed
# print(remote_session.get_cmd_output(device_command))

file = open(file_name, 'w')
file.write(gateway_session.get_cmd_output(device_command))
file.close()

print("\nThis task has been completed...\n")













