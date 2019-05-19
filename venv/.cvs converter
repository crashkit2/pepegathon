import os
import sys
import csv

ip_file = (r'biglog.log.txt')
op_file = (ip_file.split("."))

print("Opening " + ip_file)

f0 = open(ip_file, "r")
lstInput = []
for oLine in f0:
    try:
        lstLine = oLine.replace("\n", "").split("Info type:")
    except Exception as e:
        print(e)
        pass
    lstInput.append(lstLine)

f0.close()

fw = open(op_file[0] + ".csv", "w")
for oLine in lstInput:
    szWriteLine = ",".join(oLine)
    fw.write(szWriteLine + "\n")
fw.close()
