from paramiko import SSHClient, AutoAddPolicy
import re
import os
import pandas as pd
import openpyxl
from dotenv import load_dotenv
from cryptography.fernet import Fernet

def ksb_atb(df):
    # Setting variables
    host_key_loc = 'C:/Users/e080189/.ssh/known_hosts/hosts.txt'  # Host key location, you will have to set this up on your local machine
    sFTP_ip = '66.98.100.195'  # sFTP ip address, don't know it? Ping it!
    username = 'Katherine Shaw Bethea Hospital'  # sFTP Username
    sftp_folder = 'Cerner Claims ATB/Inbox' # Directory in SFTP
    file_folder = 'E:/HCPM/KSB/Cerner Claims ATB/Processed/'# Where to load the file
    sftp_folder_new = '/Cerner Claims ATB/Processed/'
    naming_convention = ''  # What the file starts with
    file_type = '.xlsx'  # File Extension
    file = ""
    remotepath = ""
    target_list = []
    target_rename = ""
    blob_storage_data = ''

    #Retrieve Password
    os.chdir('C:/Users/e080189/PycharmProjects/Word_Scambler/venv')
    root = os.getcwd()
    file_name = '\\test.env'
    dotenv_path = root + file_name
    load_dotenv(dotenv_path)
    key = os.environ.get('KEY').encode()
    encpass = os.environ.get('PASS').encode()
    cipher = Fernet(key)
    pass_byte = cipher.decrypt(encpass)
    password = bytes(pass_byte).decode('utf-8')

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
            remotepath = "/" + sftp_folder + "/" + file
            localpath = sftp_folder_new + file
            blob_storage_data = pd.read_excel(target.read(), engine='openpyxl') # Use this for XLSX files
            #blob_storage_data = pd.read_csv(target.read(), engine='python') # Use this for CSV files
            target.close()
            sftp.rename(remotepath,localpath)

    sftp.close()
    client.close()
    blob_storage_data.replace({pd.NaT: None}, inplace = True)
    blob_storage_data = blob_storage_data.astype(str)
    return blob_storage_data

def get_output_schema():
    return pd.DataFrame({
        'PRIORITY_SEQ': prep_string(),
        'CLAIM_STATUS': prep_string(),
        'RUN_DATE': prep_string(),
        'FIN_CLASS': prep_string(),
        'ENCNTR_BALANCE': prep_string(),
        'CLAIM_SUBMISSION_DATE': prep_string(),
        'MEDICAL_SERVICE': prep_string(),
        'BILLING_ENTITY': prep_string(),
        'TOTAL_CLAIM_CHARGES': prep_string(),
        'FIN_NUMBER': prep_string(),
        'DISCH_DT_TM': prep_string(),
        'CLAIM_NUMBER': prep_string(),
        'BO_HP_BALANCE': prep_string(),
        'HEALTH_PLAN': prep_string(),
        'CLAIM_GENERATION_DATE': prep_string(),
        'CLAIM_TYPE': prep_string(),
        'CLAIM_BALANCE': prep_string(),
        'TOTAL_CHARGES': prep_string(),

    });