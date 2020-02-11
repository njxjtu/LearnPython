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

cat = pd.Categorical(["a", "c", "c", np.nan], categories=["b", "a", "c"])
df = pd.DataFrame({"cat":cat, "s":["a", "c", "c", np.nan]})

print(df.describe())
print(df["cat"].describe())
print(cat.categories)
print(cat.ordered)

s = pd.Series(["a","b","c","a"], dtype="category")
s = s.cat.add_categories([4])
print(s.cat.categories)
print(s.cat.remove_categories("a"))
