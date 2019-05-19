import pandas as pd
import os
import re
#dataframe creation
file=(r'biglog.csv')
cols=['host','1','user_id','date','tz','endpoint','status','data','referer','user_agent']
df=pd.read_csv(file,delim_whitespace=True,names=cols).drop('1',1)
print(df.head())
#traffic analysis/bytes summary
g=sum(df.data)
print ('Traffic sum = ',g)

#Requests regarding 5xx errors
count = 0
for line in df.status:
    if line >=500 and line <=600:
        count=count+1

print ('5xx Errors found : ',count)

#IP organizer
df=pd.unique(df.host)
print ('Different IPs found (20): ',df)


#Regular Expression
XSScount = 0
SQLinjcount = 0
# Possible LFI server attack counter
LFIcount = 0
general_count = 0
for line in cols:
    if line.find("/js/upload") or line.find("GET /core/files/js/"):
        XSScount = XSScount + 1
    if line.find("POST /core/files/js") or line.find("://"):
        SQLinjcount = SQLinjcount + 1
        general_count = general_count + 1
    if line.find("http://evil.eu/sh") or line.find("GET /?username=admin&password=1235 HTTP/1.0"):
        general_count = general_count + 1
    if line.find("/api/v1/register/\xf5@") or line.find("/cgi-bin/count"):
        SQLinjcount = SQLinjcount + 1
        general_count = general_count + 1
    if line.find("/orders.php/?userid=bob%27%3b%20update%20logintable%") or line.find("/connection.php/"):
        SQLinjcount = SQLinjcount + 1
        XSScount = XSScount + 1
    if line.find("/api/v1/login/?post=%3script%3ealert(1);") or line.find("http://hackersite.com/dsfsdasfsd.php"):
        SQLinjcount = SQLinjcount + 1
        LFIcount = LFIcount + 1
    if line.find("/index.php/%2e%2e%2f%2e%2e%2f%2e%2e%2f/bin") or line.find("/?page=1&customerId=AND"):
        LFIcount = LFIcount + 1
        general_count = general_count + 1
    if line.find("/index.php/") or line.find("/index.php/?username=admin&pa"):
        general_count = general_count + 1
        SQLinjcount = SQLinjcount + 1
    if line.find("/login.php/?page=1&cus") or line.find("/.well-known/assetlinks.json"):
        XSScount = XSScount + 1
        SQLinjcount = SQLinjcount + 1


def readFile(path):
    with open(path) as fin:
        for line in fin:
            actual = re.findall(r'.*GET(.*)HTTP', line)
            print(actual)
    pass


readFile("C:/Users/crash/PycharmProjects/pepegathon/venv/biglog.log.txt")

print ('Traffic sum = ',g)
print ('5xx Errors found : ',count)
print ('Different IPs found (20): ',df)

print ("Possible SQL injection attacks found : ",SQLinjcount)
print ("Possible XSS attacks found : ",XSScount)
print ("Possible LFI attacks found : ",LFIcount)
print ("Found other possible server attacks",general_count)