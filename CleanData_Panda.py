# Install pandas: py -m pip install panda
# get data from csv
import pandas as pd

df = pd.read_csv('olympics.csv', index_col=0, skiprows=1)

for col in df.columns:
    if col[:2]=='01':
        df.rename(columns={col:'Gold'+col[4:]}, inplace=True)
    if col[:2]=='02':
        df.rename(columns={col:'Silver'+col[4:]}, inplace=True)
    if col[:2]=='03':
        df.rename(columns={col:'Bronze'+col[4:]}, inplace=True)
    if col[:1]=='№':
        df.rename(columns={col:'#'+col[1:]}, inplace=True)
        
names_ids = df.index.str.split('\s\(') # split the index by '('

df.index = names_ids.str[0] # the [0] element is the country name (new index) 
df['ID'] = names_ids.str[1].str[:3] # the [1] element is the abbreviation or ID (take first 3 characters from that)

df = df.drop('Totals')
df.head()


# What is the first country in df? This function should return a Series.
# You should write your whole answer within the function provided. The autograder will call
# this function and compare the return value against the correct solution value
def answer_zero():
    # This function returns the row for Afghanistan, which is a Series object. The assignment
    # question description will tell you the general format the autograder is expecting
    return df.iloc[0]

# You can examine what your function returns by calling it in the cell. If you have questions
# about the assignment formats, check out the discussion forums for any FAQs
answer_zero() 


# Which country had the biggest difference between their summer and winter gold medal counts? This function should return a single string value.
def answer_two():
    return (df['Gold']-df['Gold.1']).abs().idxmax()
answer_two()

# Which country has the biggest difference between their summer gold medal counts and winter gold medal counts relative to their total gold medal count? (Summer Gold−Winter Gold)/Total Gold Only include countries that have won at least 1 gold in both summer and winter.
# This function should return a single string value.
def answer_three():
    df1 = df[(df['Gold']>0) & (df['Gold.1']>0)]
    return (df1['Gold']-df1['Gold.1']).abs().div(df1['Gold']+df1['Gold.1']+df1['Gold.2']).idxmax()
answer_three()

'''
Write a function that creates a Series called "Points" which is a weighted value where each gold medal (Gold.2) counts for 3 points, silver medals (Silver.2) for 2 points, and bronze medals (Bronze.2) for 1 point. The function should return only the column (a Series object) which you created, with the country names as indices.
This function should return a Series named Points of length 146
'''
def answer_four():
    Points = df['Gold.2'].mul(3)+df['Silver.2'].mul(2)+df['Bronze.2'].mul(1)
    return Points
answer_four()
