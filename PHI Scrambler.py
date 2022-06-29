import pandas as pd
import csv
import os
import pyodbc as pyo

#Establish connection to Excel File
#os.chdir('E:/HCPM/HRMC/DNU')
#mapping_doc = pd.read_excel('ClaimsData_PHI_Check.xlsx', sheet_name='New Table')

#conn_obj = mc.connect(host = 'rsmphiportal.database.windows.net', user='Quigley',passwd='JK2%m!Oe3qNb')
server = 'rsmphiportal.database.windows.net'
database = 'Quigley'
username = 'Quigley'
password = 'JK2%m!Oe3qNb'
cnxn = pyo.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

#New Mapping Dataframe
new_mapping = cnxn.cursor()
table_name = 'NewMapping'
#table_name = 'DEMO_' + mapping_doc['Original Table'][0]
query = 'Select * from ' + table_name
new_mapping.execute(query)
new_mapping_df = pd.DataFrame.from_records(new_mapping)
original_column = list(new_mapping_df[1].drop_duplicates())
original_table = list(new_mapping_df[0].drop_duplicates())
#original_table.append('abcd')
#print(original_table)

#Workhorse Query Cursor
workhorse = cnxn.cursor()
for table in original_table:
    for column in original_column:
        try:
            query = "Update dbo." + table + " SET " + table + "." + column + " = NewMapping.[New Mapping] FROM NewMapping ," + table + " WHERE NewMapping.[Original Mapping] = " + table + "." + column
            print(query)
            workhorse.execute(query)
        except:
            pass
            print('Passed on '+query)
        workhorse.commit()