import pandas as pd
import numpy as np
import scipy as sp

print(pd.datetime.now()) # current date and time
print(pd.Timestamp('2017-03-01')) # timestamp
print(pd.Timestamp(1587687255,unit='s'))
print(pd.date_range("11:00", "13:30", freq="30min").time)
print(pd.to_datetime(pd.Series(['Jul 31, 2009','2010-01-10', None])))
print(pd.to_datetime(['2005/11/23', '2010.12.31', None]))
print(pd.date_range('1/1/2011', periods=5))
print(pd.date_range('1/1/2011', periods=5,freq='M'))
start = pd.datetime(2011, 1, 1)
end = pd.datetime(2011, 1, 5)
print(pd.date_range(start, end))

print(pd.Timedelta('2 days 2 hours 15 minutes 30 seconds'))
print(pd.Timedelta(6,unit='h'))
print(pd.Timedelta(days=2))

s = pd.Series(pd.date_range('2012-1-1', periods=3, freq='D'))
td = pd.Series([ pd.Timedelta(days=i) for i in range(3) ])
df = pd.DataFrame(dict(A = s, B = td))

print(df)
df['C']=df['A']+df['B']
print(df)