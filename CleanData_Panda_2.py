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
    df2 = census_df.sort_values(by=['STNAME', 'CENSUS2010POP'], ascending=False).groupby(census_df['STNAME']).head(3).groupby(census_df['STNAME'])['CENSUS2010POP'].sum().reset_index()
    return df2.sort_values(by='CENSUS2010POP', ascending=False).head(3)
answer_six()

#  Answer:
#       STNAME	CENSUS2010POP
# 4	    California	50167874
# 43	Texas	31606159
# 32	New York	24113524
