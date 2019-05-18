import pandas as pd
#dataframe creation
file=(r'biglog.csv')
cols=['host','1','user_id','date','tz','endpoint','status','data','referer','user_agent']
df=pd.read_csv(file,delim_whitespace=True,names=cols).drop('1',1)
print(df.head())
#traffic analysis
g=sum(df.data)
print ('Traffic sum = ',g)

df=pd.unique(df.host)
print ('Different IPs found (20): ',df)
#summary of data collumn
