'''
Question 1 (20%)
Load the energy data from the file Energy Indicators.xls, which is a list of indicators of energy supply and renewable electricity production from the United Nations for the year 2013, and should be put into a DataFrame with the variable name of energy.

Keep in mind that this is an Excel file, and not a comma separated values file. Also, make sure to exclude the footer and header information from the datafile. The first two columns are unneccessary, so you should get rid of them, and you should change the column labels so that the columns are:

['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable']

Convert Energy Supply to gigajoules (there are 1,000,000 gigajoules in a petajoule). For all countries which have missing data (e.g. data with "...") make sure this is reflected as np.NaN values.

Rename the following list of countries (for use in later questions):

"Republic of Korea": "South Korea",
"United States of America": "United States",
"United Kingdom of Great Britain and Northern Ireland": "United Kingdom",
"China, Hong Kong Special Administrative Region": "Hong Kong"

There are also several countries with numbers and/or parenthesis in their name. Be sure to remove these,

e.g.

'Bolivia (Plurinational State of)' should be 'Bolivia',

'Switzerland17' should be 'Switzerland'.



Next, load the GDP data from the file world_bank.csv, which is a csv containing countries' GDP from 1960 to 2015 from World Bank. Call this DataFrame GDP.

Make sure to skip the header, and rename the following list of countries:

"Korea, Rep.": "South Korea", 
"Iran, Islamic Rep.": "Iran",
"Hong Kong SAR, China": "Hong Kong"



Finally, load the Sciamgo Journal and Country Rank data for Energy Engineering and Power Technology from the file scimagojr-3.xlsx, which ranks countries based on their journal contributions in the aforementioned area. Call this DataFrame ScimEn.

Join the three datasets: GDP, Energy, and ScimEn into a new dataset (using the intersection of country names). Use only the last 10 years (2006-2015) of GDP data and only the top 15 countries by Scimagojr 'Rank' (Rank 1 through 15).

The index of this DataFrame should be the name of the country, and the columns should be ['Rank', 'Documents', 'Citable documents', 'Citations', 'Self-citations', 'Citations per document', 'H index', 'Energy Supply', 'Energy Supply per Capita', '% Renewable', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015'].

This function should return a DataFrame with 20 columns and 15 entries.
'''
import pandas as pd
import numpy as np

energy = pd.read_excel('Energy Indicators.xls', header=17,skipfooter=38,usecols=[1,2,3,4,5],na_values='...')
energy = energy.iloc[:, 1:]
energy.columns = ['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable']
energy['Energy Supply'] *= 1000000
energy.replace('Republic of Korea','South Korea', inplace=True)
energy.replace('United States of America','United States', inplace=True)
energy.replace('United Kingdom of Great Britain and Northern Ireland','United Kingdom', inplace=True)
energy.replace('China, Hong Kong Special Administrative Region', 'Hong Kong', inplace=True)

df_obj = energy.select_dtypes(['object'])
energy.Country = energy.Country.str.replace("\(.*\)","").str.replace('[0-9]','')
print("-------------- Energy --------------")
print(energy)
##
# GDP = pd.read_csv('world_bank.csv', index_col=0, skiprows=4)
GDP = pd.read_csv('world_bank.csv', skiprows=4)
GDP.replace('Korea, Rep.','South Korea', inplace=True)
GDP.replace('Iran, Islamic Rep.','Iran', inplace=True)
GDP.replace('Hong Kong SAR, China','Hong Kong', inplace=True)
print("-------------- GDP --------------")
GDP = GDP.iloc[:,[0,50,51,52,53,54,55,56,57,58,59]]
GDP.rename(columns={'Country Name':'Country'}, inplace= True)
GDP.set_index('Country')
print(GDP)
#
ScimEn = pd.read_excel('scimagojr.xlsx')
print("-------------- ScimEn --------------")
ScimEn2 = ScimEn
ScimEn = ScimEn.iloc[0:15,:]
ScimEn.set_index('Country')
print(ScimEn)

final_df = ScimEn.merge(GDP,left_on='Country', right_on='Country', how='left')
final_df = final_df.merge(energy, left_on='Country', right_on='Country', how='left')
print("-------------- Final Result : --------------")
final_df2 = final_df.set_index('Country')
print(final_df2)
print(final_df2.columns)
print("-------------- Test Value: --------------")
print(final_df.loc[final_df['Country'] == 'China'])
'''
Question 2
The previous question joined three datasets then reduced this to just the top 15 entries. When you joined the datasets, but before you reduced this to the top 15 items, how many entries did you lose?
This function should return a single number.
'''
final_sum = ScimEn2.merge(GDP,left_on='Country', right_on='Country')
final_sum = final_sum.merge(energy, left_on='Country', right_on='Country')
print(len(final_sum)-len(final_df2))
'''
Question 3 
What is the average GDP over the last 10 years for each country? (exclude missing values from this calculation.)
This function should return a Series named avgGDP with 15 countries and their average GDP sorted in descending order.
'''
avg = final_df2[['2006', '2007', '2008', '2009','2010', '2011', '2012', '2013', '2014', '2015']].mean(axis=1)
avg = avg.sort_values(ascending = False)
print(avg)
'''
Question 4 (6.6%)
By how much had the GDP changed over the 10 year span for the country with the 6th largest average GDP?
This function should return a single number.
'''

final_df2['avg'] = final_df2[['2006', '2007', '2008', '2009','2010', '2011', '2012', '2013', '2014', '2015']].mean(axis=1)
final_df2_sorted = final_df2.sort_values('avg', ascending=False)
final_df2_sorted['deltaGDP'] = final_df2_sorted['2015']-final_df2_sorted['2006']
print(final_df2_sorted)
print(final_df2_sorted.iloc[5,21])
'''
Question 5 (6.6%)
What is the mean Energy Supply per Capita?
This function should return a single number.
'''
