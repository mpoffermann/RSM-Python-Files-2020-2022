from paramiko import SSHClient, AutoAddPolicy
import re

# Setting variables
host_key_loc = 'C:/Users/e080189/.ssh/known_hosts/hosts.txt'  # Host key location, you will have to set this up on your local machine
sFTP_ip = '66.98.100.150'  # sFTP ip address, don't know it? Ping it!
username = 'Katherine Shaw Bethea Hospital'  # sFTP Username
password = 'EIjbdjGJ'  # sFTP Pass
file_folder = 'E:/HCPM/KSB/EDI_Inbox/'  # Where to load the file
naming_convention = ''  # What the file starts with
file_type = ''  # File Extension
file = ""
remotepath = ""
target_list = []

# chmod 755 C:/Users/e080189/.ssh/known_hosts/hosts.txt
client = SSHClient()

# LOAD HOST KEYS
client.load_host_keys(host_key_loc)
client.load_system_host_keys()

# Known host policy
client.set_missing_host_key_policy(AutoAddPolicy())

# Connect to sFTP
client.connect(sFTP_ip, username=username, password=password)
print('connection successful')
sftp = client.open_sftp()

# Navigate to appropriate directory
sftp.chdir('Cerner Claims ATB/Inbox')
dir_list = sftp.listdir()

# Build Search Phrase from naming convention & file type
search_phrase = naming_convention + ".+." + file_type

# Retrieve any files with Search Phrase naming covention
for file in dir_list:
    if re.search(search_phrase, file):
        target = file
        target_list.append(target)
        remotepath = target
        localpath = file_folder + target
        sftp.get(remotepath, localpath)
        sftp.remove(target)

# Close the connection
sftp.close()
client.close()
print('closed connection')