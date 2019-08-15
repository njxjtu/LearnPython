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


#Question 7
#Which county has had the largest absolute change in population within the period 2010-2015? (Hint: population values are stored in columns POPESTIMATE2010 through POPESTIMATE2015, you need to consider all six columns.)
#e.g. If County Population in the 5 year period is 100, 120, 80, 105, 100, 130, then its largest change in the period would be |130-80| = 50.
#This function should return a single string value.

def answer_seven():
    census_df['maxpop'] = census_df[['POPESTIMATE2010','POPESTIMATE2011','POPESTIMATE2012','POPESTIMATE2013','POPESTIMATE2014','POPESTIMATE2015']].max(axis=1)
    census_df['minpop'] = census_df[['POPESTIMATE2010','POPESTIMATE2011','POPESTIMATE2012','POPESTIMATE2013','POPESTIMATE2014','POPESTIMATE2015']].min(axis=1)
    census_df['chgpop'] = census_df['maxpop']-census_df['minpop']
    return census_df.sort_values(by='chgpop',ascending=False).head(1)['CTYNAME']
answer_seven()

#Question 8
#In this datafile, the United States is broken up into four regions using the "REGION" column.
#Create a query that finds the counties that belong to regions 1 or 2, whose name starts with 'Washington', and whose POPESTIMATE2015 was greater than their POPESTIMATE 2014.
#This function should return a 5x2 DataFrame with the columns = ['STNAME', 'CTYNAME'] and the same index ID as the census_df (sorted ascending by index).

def answer_eight():
    df3 = census_df.loc[census_df['REGION'].isin([1,2]) & census_df['CTYNAME'].str.startswith('Washington', na=False) & (census_df['POPESTIMATE2015']>census_df['POPESTIMATE2014'])]
    return df3
answer_eight()
