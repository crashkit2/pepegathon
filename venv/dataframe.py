import pandas as pd
#dataframe creation
file=(r'biglog.csv')
cols=['host','1','user_id','date','tz','endpoint','status','data','referer','user_agent']
df=pd.read_csv(file,delim_whitespace=True,names=cols).drop('1',1)
print(df.head())

sum1= sum(df.data)
#summary of data collumn
print (sum1)