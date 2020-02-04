import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(3, 3), index=['a', 'c', 'e'],columns=['one','two', 'three'])
df = df.reindex(['a', 'b', 'c'])

print(df)
print("NaN replaced with '0':")
print(df.fillna(0))
print(df.fillna(method='pad'))      # forward fill
print(df.fillna(method='backfill')) # back fill
print(df.dropna())                  # drop na
df = pd.DataFrame({'one':[10,20,30,40,50,2000], 'two':[1000,0,30,40,50,60]})
print(df.replace(1000,10))
print(df.replace({1000:10,2000:60}))
