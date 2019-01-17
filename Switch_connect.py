from netmiko import ConnectHandler
import getpass
import re

device_ip = "10.1.0.200" #input("What is the IP of the device? > ")
username = input("Username: ")
password = getpass.getpass("Password: ")
file_name = input("What do you want to name the file? > ")
print("\nPlease wait...")
#print("Please wait while the information is gathered and written to " + file_name + "...")

cisco_device = {
    'device_type': 'cisco_ios',
    'ip': '',
    'username': '',
    'password': '',
}

cisco_device['ip'] = device_ip
cisco_device['username'] = username
cisco_device['password'] = password

# connect to tacobox
net_connect = ConnectHandler(**cisco_device)
# ask for IP to get to
device_ip = input("What IP do you want to get to? > ")
print("\nPlease wait...")
# device_output = net_connect.send_command(device_command)
# connect to new device
net_connect = ConnectHandler(**cisco_device)

device_command = input("What command do you want to run? > ")
device_output = net_connect.send_command(device_command)

file = open(file_name, 'w')
file.write(device_output)
file.close()

print("\nThis task has been completed...\n")

# print(" This is device_output:\n", device_output)

################
# Gather -- CDP #
################

# cdp = {
#     'device_id': '',
#     'ip_address': '',
#     'interface': '',
# }

# cdp1 = {
#     'device_id': '',
#     'ip_address': '',
#     'interface': '',
# }


# device_list = []
# ip_list = []
# interface_list = []



# if "Device ID" in device_output:
#     device_find = re.findall('Device ID: (\w+.+)', device_output)
#     device_list.append(device_find)
       
# if "IP address" in device_output:
#     ip_find = re.findall('IP address: (\w+.+)', device_output)
#     ip_list.append(ip_find)

# if "Interface" in device_output:
#     int_find = re.findall('Interface: (\w+.\d+)', device_output)
#     interface_list.append(int_find)

#cdp2 = dict(zip([ip_list], [interface_list]))

#print(device_list)
#print(ip_list)
#print(interface_list)
#print("This is CDP:\n", cdp)
#print("This is CDP1:\n", cdp1)
# print(device_list)
# print(ip_list)
# print(interface_list)

#print(cdp2)

#(\d+.+)
# (?!SEP)




#"show cdp neighbor detail | in Device|IP|Interface"