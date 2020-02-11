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

# Groupby
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
print(df.groupby('Team').filter(lambda x: len(x) >= 3)) # filter the groups that meet the lambda criteria
export_csv = df.to_csv(r'export_dataframe.csv', index = None, header=True) 

# Merging, Joinging
left = pd.DataFrame({
   'id':[1,2,3,4,5],
   'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
   'subject_id':['sub1','sub2','sub4','sub6','sub5']})
right = pd.DataFrame(
   {'id':[1,2,3,4,5],
   'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
   'subject_id':['sub2','sub4','sub3','sub6','sub5']})
print("left")
print(left)
print("right")
print(right)
print(pd.merge(left,right,on='id'))
print("Merge on multiple keys")
print(pd.merge(left,right,on=['id','subject_id']))
print(pd.merge(left, right, on='subject_id', how='left'))
print(pd.merge(left, right, how='outer', on='subject_id'))

# Concatenating objects
one = pd.DataFrame({
   'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
   'subject_id':['sub1','sub2','sub4','sub6','sub5'],
   'Marks_scored':[98,90,87,69,78]},
   index=[1,2,3,4,5])

two = pd.DataFrame({
   'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
   'subject_id':['sub2','sub4','sub3','sub6','sub5'],
   'Marks_scored':[89,80,79,97,88]},
   index=[1,2,3,4,5])
print("one")
print(one)
print("two")
print(two)
print(pd.concat([one,two]))
print(pd.concat([one,two],keys=['x','y']))
print(pd.concat([one,two],keys=['x','y'],ignore_index=True))
print(pd.concat([one,two],axis=1))
print(one.append(two))
print(one.append([two,one,two])) # taking multiple objects

