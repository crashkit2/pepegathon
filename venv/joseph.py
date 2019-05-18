#f=open ('website-access-copy.log','r')

#for line in f:
 #   print (line.split(' ]')[0])

import csv

with open('website-access-copy.log','r') as csv_file:
    csv_reader=csv.reader(csv_file)

    for line in csv_reader:
        print(line)