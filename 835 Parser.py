import edi.parser
import json
import os

CLAIM_FOLDER = "E:\HCPM\TEST\EDI_Inbox"
CONFIG_FOLDER = "E:\HCPM\TEST\Testing"

os.chdir(CLAIM_FOLDER)
files = os.listdir()
filename    = os.sep.join([CLAIM_FOLDER,files[0]])
conf        = json.loads(open( os.sep.join([CONFIG_FOLDER,'837.json']) ).read())
