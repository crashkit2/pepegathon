import pandas as pd
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
