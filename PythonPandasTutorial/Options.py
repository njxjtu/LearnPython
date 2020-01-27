import pandas as pd
import numpy as np

print(pd.get_option("display.max_rows"))
print(pd.get_option("display.max_columns"))
pd.set_option("display.max_rows",80)
pd.reset_option("display.max_rows") ## Using reset_option(), we can change the value back to the default number of rows to be displayed
pd.describe_option("display.max_rows")

with pd.option_context("display.max_rows",10):
   print(pd.get_option("display.max_rows"))
print(pd.get_option("display.max_rows"))
print(pd.get_option("display.precision"))


## selection
df = pd.DataFrame(np.random.randn(8, 4), index = ['a','b','c','d','e','f','g','h'], columns = ['A', 'B', 'C', 'D'])
print(df.loc[:,['A','C']])
print(df.loc[['a','b','f','h'],['A','C']])
print(df.loc['a':'h'])
print(df.iloc[1:5,2:4])
