import pandas as pd
import numpy as np

def f_add(input1, input2):
    return input1+input2

print(f_add(3,5))

#pipe()
dic = {'Score_Math':pd.Series([66,57,75,44,31,67,85,33,42,62,51,47]),
   'Score_Science':pd.Series([89,87,67,55,47,72,76,79,44,92,93,69])}
df = pd.DataFrame(dic)
print(df)
print(df.pipe(f_add,2))

df = pd.DataFrame([[4, 9]] * 3, columns=["col1", "col2"])
print(df)
df.apply(np.sqrt)
df.apply(np.sum, axis=0)
df.apply(np.sum, axis=1)
print(df.apply(lambda x: [1, 2], axis=1))
N=20
df = pd.DataFrame({
   'A': pd.date_range(start='2016-01-01',periods=N,freq='D'),
   'x': np.linspace(0,stop=N-1,num=N),
   'y': np.random.rand(N),
   'C': np.random.choice(['Low','Medium','High'],N).tolist(),
   'D': np.random.normal(100, 10, size=(N)).tolist()
})
print(df)
df1 = pd.DataFrame(np.random.randn(6,3),columns=['col1','col2','col3'])
df2 = pd.DataFrame(np.random.randn(2,3),columns=['col1','col2','col3'])

# Padding NAN's
print(df2.reindex_like(df1))

# Now Fill the NAN's with preceding Values
print ("Data Frame with Forward Fill:")
print(df2.reindex_like(df1,method='ffill'))

# Now Fill the NAN's with preceding Values
print ("Data Frame with Forward Fill limiting to 1:")
print(df2.reindex_like(df1,method='ffill',limit=1))

# Renaming
df1 = pd.DataFrame(np.random.randn(6,3),columns=['col1','col2','col3'])
print(df1)

print ("After renaming the rows and columns:")
print(df1.rename(columns={'col1' : 'c1', 'col2' : 'c2'}, index = {0 : 'apple', 1 : 'banana', 2 : 'durian'}))

# Iterating
print("Iterating")
print(df)
for col in df:
   print(col)
print("Iterating key, value")
for key,value in df.iteritems():
   print(key,value)
print("Iterating - iterrows()")
df = pd.DataFrame(np.random.randn(4,3),columns = ['col1','col2','col3'])
for row_index,row in df.iterrows():
   print(row_index,row)
print("Iterating - itertuples()")
for row in df.itertuples():
    print(row)

# Sorting - (by label or by actual value)
unsorted_df=pd.DataFrame(np.random.randn(10,2),index=[1,4,6,2,3,5,9,8,0,7],columns=['col2','col1'])
print("Unsorted df")
print(unsorted_df)
sorted_df=unsorted_df.sort_index()
print("Sorted df by label - index label")
print(sorted_df)
sorted_df=unsorted_df.sort_index(ascending=False)
print("Sorted df by label - index label - descending")
print(sorted_df)
sorted_df=unsorted_df.sort_index(axis=1)
print("Sorted df by label - column labels")
print(sorted_df)
sorted_df=unsorted_df.sort_values(by='col1')
print("Sorted df by value")
print(sorted_df)
sorted_df=unsorted_df.sort_values(by=['col1','col2'])
print("Sorted df by value")
print(sorted_df)
sorted_df=unsorted_df.sort_values(by=['col1','col2'],kind='mergesort')
print("Sorted df by value, choose the algorithm from mergesort, heapsort and quicksort. Mergesort is the only stable algorithm")
print(sorted_df)
