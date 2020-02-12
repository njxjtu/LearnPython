import pandas as pd

df=pd.read_csv("export_dataframe.csv")
print(df)

df=pd.read_csv("export_dataframe.csv",index_col=['Team'])
print(df)

df=pd.read_csv("export_dataframe.csv", names=['a', 'b', 'c','d'])
print(df)

df=pd.read_csv("export_dataframe.csv", skiprows=2)
print(df)