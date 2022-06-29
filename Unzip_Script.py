import zipfile
target = 'KSB_EDIFiles_05_26_2021.zip'
handle = zipfile.ZipFile(target)
handle.extractall('E:\HCPM\KSB\EDI_Inbox')
handle.close()