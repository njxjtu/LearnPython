import pandas as pd
import numpy as np

### Creation ###

# Create empty Series
s = pd.Series()
print(s)

# Create Series from ndarray(N-Dimentional array)
s = pd.Series( np.array(['a', 'b', 'c']) )  # default index: 0, 1, 2
s = pd.Series( np.array(['a', 'b', 'c']), index=[101, 102, 103] )  # specify index: 101, 102, 103

# Create Series from dict
dict01 = {'a' : 0., 'b' : 1., 'c' : 2.}
s = pd.Series(dict01)
print(s)       # dictionary keys become the index

# Create Series from Scalar
s = pd.Series(2, index=[0, 1, 2, 3])
print(s)     # Scalar value is repeated to match the length of index

### Access ###

# Access data from Series with position
s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])
print(s[0])
print(s[:3])
print(s[-3:])

# Access data from Series with label
print(s['a'])
print(s[['a','c','d']]


### Functions ###
print(s.axes)
print(s.empty)
print(s.ndim)
print(s.size)
print(s.values)
print(s.head(2))
print(s.tail(2))
