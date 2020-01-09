import pandas as pd

# Create DataFrame - empty DataFrame
df = pd.DataFrame()
print(df)


# Create DataFrame - based on Lists
data = [1,2,3,4,5]
df = pd.DataFrame(data)
print(df)

data = [['Alex',10],['Bob',12],['Clarke',13]]
df = pd.DataFrame(data,columns=['Name','Age'])
print(df)

df = pd.DataFrame(data,columns=['Name','Age'],dtype=float)
print(df)

# Create DataFrame - based on Dict of ndarrays / Lists
data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
df = pd.DataFrame(data)
print(df)

df = pd.DataFrame(data, index=['rank1','rank2','rank3','rank4'])
print(df)

# Create DataFrame - based on List of Dicts
data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]
df = pd.DataFrame(data)

data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]
df = pd.DataFrame(data, index=['first', 'second'])
df = pd.DataFrame(data, index=['first', 'second'], columns=['a', 'b'])
df = pd.DataFrame(data, index=['first', 'second'], columns=['a', 'b1'])

# Create DataFrame - based on Dict of Series
d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
   'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}
df = pd.DataFrame(d)

# Column Selection
print(df['two'])
print(df[['one','two']])

# Add column
df['three']=pd.Series([10,20,30],index=['a','b','c'])
print(df)
df['four']=df['one']+df['three']
print(df)

# Delete column using DEL function
del df['one']
print(df)

# Delete column using pop function using POP function
df.pop('two')
print(df)

# Delete column using drop function
df.drop(['one'], axis=1, inplace=True)

# Row select - label
d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']), 
   'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}
df = pd.DataFrame(d)
print(df.loc['b'])

# Row select - integer
print(df.iloc[2])

# Row select - slice rows / multiple rows
print(df[2:4])

# Add rows
df = pd.DataFrame([[1, 2], [3, 4]], columns = ['a','b'])
df2 = pd.DataFrame([[5, 6], [7, 8]], columns = ['a','b'])
df = df.append(df2)

# Delete rows using drop function
print(df)
print(df.drop(['a','d']))
print(df)
df.drop(['a','d'], inplace=True)
print(df)
