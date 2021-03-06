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

'''
Question 1
Which country has won the most gold medals in summer games?
This function should return a single string value.
'''
def answer_one():
    return df['Gold'].idxmax()
answer_one()

# Question 2: Which country had the biggest difference between their summer and winter gold medal counts? This function should return a single string value.
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
'''

Part 2
For the next set of questions, we will be using census data from the United States Census Bureau. Counties are political and geographic subdivisions of states in the United States. This dataset contains population data for counties and states in the US from 2010 to 2015. See this document for a description of the variable names.

The census dataset (census.csv) should be loaded as census_df. Answer questions using this as appropriate.
'''

# Question 5
# Which state has the most counties in it? (hint: consider the sumlevel key carefully! You'll need this for future questions too...)
# This function should return a single string value.

import panda as pd
census_df = pd.read_csv('census.csv')
census_df.head()

def answer_five():
    return census_df.groupby(census_df['STNAME']).count().COUNTY.idxmax()
answer_five()

# Question 6
# Only looking at the three most populous counties for each state, what are the three most populous states (in order of highest population to lowest population)? Use CENSUS2010POP.
# This function should return a list of string values.

def answer_six():
    df2=census_df[census_df['SUMLEV']==50]
    df2=df2[['STNAME','CTYNAME','CENSUS2010POP']].sort_values(by=['STNAME', 'CENSUS2010POP'], ascending=[True,False])
    df2=df2.groupby(df2['STNAME']).head(3).groupby(df2['STNAME'])['CENSUS2010POP'].sum()
    #print(df2.nlargest(3).index)
    #print(type(df2.nlargest(3).index.tolist()))
    return df2.nlargest(3).index.tolist()

#  Answer:
#  ['California', 'Texas', 'Illinois']


#Question 7
#Which county has had the largest absolute change in population within the period 2010-2015? (Hint: population values are stored in columns POPESTIMATE2010 through POPESTIMATE2015, you need to consider all six columns.)
#e.g. If County Population in the 5 year period is 100, 120, 80, 105, 100, 130, then its largest change in the period would be |130-80| = 50.
#This function should return a single string value.

def answer_seven():
    df2=census_df[census_df['SUMLEV']==50]
    df2['maxpop'] = df2[['POPESTIMATE2010','POPESTIMATE2011','POPESTIMATE2012','POPESTIMATE2013','POPESTIMATE2014','POPESTIMATE2015']].max(axis=1)
    df2['minpop'] = df2[['POPESTIMATE2010','POPESTIMATE2011','POPESTIMATE2012','POPESTIMATE2013','POPESTIMATE2014','POPESTIMATE2015']].min(axis=1)
    df2['chgpop'] = df2['maxpop']-df2['minpop']
    return df2.sort_values(by='chgpop',ascending=False).iloc[0,6]

# Answer: 'Harris County'

#Question 8
#In this datafile, the United States is broken up into four regions using the "REGION" column.
#Create a query that finds the counties that belong to regions 1 or 2, whose name starts with 'Washington', and whose POPESTIMATE2015 was greater than their POPESTIMATE 2014.
#This function should return a 5x2 DataFrame with the columns = ['STNAME', 'CTYNAME'] and the same index ID as the census_df (sorted ascending by index).

def answer_eight():
    df3 = census_df.loc[census_df['REGION'].isin([1,2]) & census_df['CTYNAME'].str.startswith('Washington', na=False) & (census_df['POPESTIMATE2015']>census_df['POPESTIMATE2014'])]
    return df3[['STNAME', 'CTYNAME'] ]
answer_eight()
