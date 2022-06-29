import Word_Scambler as ws
import os
import csv

os.chdir('C:/Users/e080189/Desktop')
with open('name_change.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file,delimiter=",")
    line_count = 0
    row_count = 2
    df = []
    for row in csv_reader:
        if line_count == 0:
            df.append(row)
            line_count += 1
        else:
           row.append(ws.word_scrambler(row[0]))
           df.append(row)
           line_count += 1

with open('name_change.csv', 'w') as csv_file:
    csv_writer = csv.writer(csv_file,delimiter=',')
    for i in df:
        csv_writer.writerow(i)