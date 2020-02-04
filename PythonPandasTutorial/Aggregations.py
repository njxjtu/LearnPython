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

