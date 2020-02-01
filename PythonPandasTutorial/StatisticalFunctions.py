import pandas as pd
import numpy as np

s = pd.Series([1,2,3,4,5,4])
print(s.pct_change())

df = pd.DataFrame(np.random.randn(5, 2))
print(df)
print(df.pct_change())

s1 = pd.Series(np.random.randn(10))
s2 = pd.Series(np.random.randn(10))
print(s1.cov(s2))
print("Covariance")
frame = pd.DataFrame(np.random.randn(10, 5), columns=['a', 'b', 'c', 'd', 'e'])
print(frame['a'].cov(frame['b']))
print(frame.cov())

s = pd.Series(np.random.randn(5), index=list('abcde'))
print("Series: ")
print(s)
s['d'] = s['b'] # so there's a tie
print(s.rank())

df = pd.DataFrame(np.random.randn(10, 4),
   index = pd.date_range('1/1/2000', periods=10),
   columns = ['A', 'B', 'C', 'D'])
print(df)
print(df.rolling(window=3).mean())
