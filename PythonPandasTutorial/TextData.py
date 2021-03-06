import pandas as pd
import numpy as np

s = pd.Series(['Tom', '   William Rick', 'John', 'Alber@t', np.nan, '1234','SteveSmith','lower','UPPER'])
print(s.str.lower())
print(s.str.upper())
print(s.str.len())
print ("Before Stripping:")
print(s)
print ("After Stripping:")
print(s.str.strip())
print(s.str.split(' '))
print(s.str.cat(sep='_'))
print(s.str.get_dummies())
print(s.str.contains(' '))
print(s.str.replace('@','$'))
print(s.str.repeat(2))
print(s.str.count('m'))
print(s.str.startswith ('T'))
print(s.str.endswith('t'))
print(s.str.find('e'))  ## returns the index of the first found pattern
print(s.str.findall('e'))
print(s.str.swapcase())
print(s.str.islower())
print(s.str.isupper())
print(s.str.isnumeric())
