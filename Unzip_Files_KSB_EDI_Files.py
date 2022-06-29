import zipfile as zf
import os
import re
zip_file = ""
os.chdir('E:/HCPM/KSB/EDI_Inbox')
dir_list = os.listdir()
for zip_file in dir_list:
    if re.search('KSB_EDIFiles.+.zip', zip_file):
        target = zip_file
        handle = zf.ZipFile(target)
        handle.extractall()
        handle.close()
        print("Extracted " + target)
        os.remove(target)
        print("Removed " + target)