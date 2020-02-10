import pandas as pd
import numpy as np
import scipy as sp

df = pd.DataFrame(np.random.randn(10, 4),
   index = pd.date_range('1/1/2000', periods=10),
   columns = ['A', 'B', 'C', 'D'])

print(df)
print(df.rolling(window=3,min_periods=1).sum())
print(df.rolling(2, win_type='gaussian').sum(std=3))
r = df.rolling(window=3,min_periods=1)
print(r['A'].aggregate(np.sum))


ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
   'Kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
   'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
   'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
   'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}
df = pd.DataFrame(ipl_data)
print(df)
print(df.groupby('Team').groups)
grouped = df.groupby('Team')
print(grouped)
print(grouped.agg(np.size))
for name,group in grouped:
   print(name)
   print(group)

print("get a group by the name")
print(grouped.get_group('Kings'))
print(grouped['Points'].agg(np.mean))
print(grouped['Points'].agg([np.sum, np.mean, np.std]))
score = lambda x: (x - x.mean()) / x.std()*10
print(grouped.transform(score))
print(df.groupby('Team').filter(lambda x: len(x) >= 3)) # filter the groups that meet the lambda criteria 02/10/2020
