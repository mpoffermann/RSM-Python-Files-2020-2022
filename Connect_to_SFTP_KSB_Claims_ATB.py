from paramiko import SSHClient, AutoAddPolicy
import re
import os
import pandas as pd
from tabpy.tabpy_tools.client import Client
from tabpy.tabpy_tools.schema import generate_schema
from tabpy.tabpy_server.app import app
import openpyxl

#TABPY_CLIENT = Client('http://localhost:9004/')
#app.ConfigParameters.TABPY_EVALUATE_TIMEOUT = 3000

def test1(*x):
    # Setting variables
    host_key_loc = 'C:/Users/e080189/.ssh/known_hosts/hosts.txt'  # Host key location, you will have to set this up on your local machine
    sFTP_ip = '66.98.100.195'  # sFTP ip address, don't know it? Ping it!
    username = 'Katherine Shaw Bethea Hospital'  # sFTP Username
    password = '2cWELpEA'  # sFTP Pass
    sftp_folder = 'Cerner Claims ATB/Inbox' # Directory in SFTP
    file_folder = 'E:/HCPM/KSB/Cerner Claims ATB/Inbox/'  # Where to load the file
    naming_convention = ''  # What the file starts with
    file_type = '.xlsx'  # File Extension
    file = ""
    remotepath = ""
    target_list = []
    target_rename = ""
    blob_storage_data = ''

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
    sftp.chdir(sftp_folder)
    dir_list = sftp.listdir()


    # Build Search Phrase from naming convention & file type
    search_phrase = naming_convention + ".+." + file_type

    # Retrieve any files with Search Phrase naming covention
    for file in dir_list:
        if re.search(search_phrase, file):
            target = sftp.file(file)
            #target = file
            #target_list.append(target)
            #remotepath = target
            #localpath = file_folder + target
            blob_storage_data = pd.read_excel(target.read(), engine='openpyxl')
            #print(blob_storage_data)
            #sftp.get(remotepath, localpath)
            #sftp.remove(target)

    # Close the connection
    sftp.close()
    client.close()
    print('closed connection')
    print(blob_storage_data.head)
    return blob_storage_data
DF = test1("t")
print(DF.head)
'''
def TEST(*x):
    TABPY_CLIENT = Client('http://localhost:9004/')
    app.ConfigParameters.TABPY_EVALUATE_TIMEOUT = 3000
    print(TABPY_CLIENT.deploy('test1', test1(*x), 'Returns data set from SFTP', override=True))

#print(test1())
print(TEST())

### RUN/MODIFICATION HISTORY ###
1M. COMMENTED OUT THE DEPLOY FUNCTIONS, TO TEST THE SUCCESSFUL LOAD OF THE DATAFRAME INTO PANDAS
1R. ERROR RECEIVED, WAS CALLING WITH AN INDEX OF 0

2M. print(blob_storage_data.columns)
2D. Tried to print the columns of the dataframe object blob_storage_data to determine if data had been picked up.
2R. confirmed column output matched spreadsheet

3M. print(blob_storage_data.head) 
3D. Tried to print the columns of the dataframe object blob_storage_data to determine if data had been picked up.
3R. confirmed

Last Progress Update:
Pretty sure that the script has been successfully deployed. Now I have to figure out how to run it and return the information back into Tableau Prep.
https://www.youtube.com/watch?v=nRtOMTnBz_Y

'''