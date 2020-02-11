import pandas as pd
import numpy as np
import scipy as sp

s = pd.Series(["a","b","c","a"], dtype="category")
print(s)
cat = pd.Categorical(['a', 'b', 'c', 'a', 'b', 'c'])
print(cat)
cat=pd.Categorical(['a','b','c','a','b','c','d'], ['c', 'b', 'a'])
print(cat)
cat=pd.Categorical(['a','b','c','a','b','c','d'], ['c', 'b', 'a'],ordered=True)
print(cat)