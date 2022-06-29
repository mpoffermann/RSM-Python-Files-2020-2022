import os
from os.path import join, dirname
from dotenv import dotenv_values
from dotenv import load_dotenv
from cryptography.fernet import Fernet

# GET PASSWORD FROM test.env
root = 'C:\\Users\\e80189\\PyCharmProjects\\Word_Scrambler\\venv'
file_name = '\\test.env'
dotenv_path = root + file_name
print(dotenv_path)
load_dotenv(dotenv_path)
key = os.environ.get('KEY').encode()
encpass = os.environ.get('PASS').encode()
cipher = Fernet(key)
pass_byte=cipher.decrypt(encpass)
password = bytes(pass_byte).decode('utf-8')
print(password)
