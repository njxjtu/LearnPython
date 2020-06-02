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

def answer_one():
    energy = pd.read_excel('Energy Indicators.xls', header=9, skipfooter=38, skiprows=range(10,18),na_values='...')
    energy.columns = ['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable']
    energy['Energy Supply'] *= 1000000
    energy['Energy Supply'].replace('...',np.NaN, inplace=True)
    energy.Country = energy.Country.str.replace("\(.*\)","").str.replace('[0-9]','').str.strip()
    di = {"Republic of Korea": "South Korea",
    "United States of America": "United States",
    "United Kingdom of Great Britain and Northern Ireland": "United Kingdom",
    "China, Hong Kong Special Administrative Region": "Hong Kong"}
    energy.replace({"Country": di},inplace = True)
    energy.set_index('Country', inplace = True)
    energy.reset_index(inplace = True)
    ###
    GDP = pd.read_csv('world_bank.csv', skiprows=4)
    GDP.replace('Korea, Rep.','South Korea', inplace=True)
    GDP.replace('Iran, Islamic Rep.','Iran', inplace=True)
    GDP.replace('Hong Kong SAR, China','Hong Kong', inplace=True)
    GDP = GDP.iloc[:,[0,50,51,52,53,54,55,56,57,58,59]]
    GDP.rename(columns={'Country Name':'Country'}, inplace= True)
    GDP.set_index('Country')
    ###
    ScimEn = pd.read_excel('scimagojr-3.xlsx')
    ScimEn = ScimEn.iloc[0:15,1:]
    ###
    final_df = ScimEn.merge(GDP,left_on='Country', right_on='Country')
    final_df = final_df.merge(energy, left_on='Country', right_on='Country')
    return final_df
'''
Question 2
The previous question joined three datasets then reduced this to just the top 15 entries. When you joined the datasets, but before you reduced this to the top 15 items, how many entries did you lose?
This function should return a single number.
'''
def answer_two():
    energy = pd.read_excel('Energy Indicators.xls', header=9, skipfooter=38, skiprows=range(10,18),na_values='...')
    energy.columns = ['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable']
    energy['Energy Supply'] *= 1000000
    energy.Country = energy.Country.str.replace("\(.*\)","").str.replace('[0-9]','').str.strip()
    di = {"Republic of Korea": "South Korea",
    "United States of America": "United States",
    "United Kingdom of Great Britain and Northern Ireland": "United Kingdom",
    "China, Hong Kong Special Administrative Region": "Hong Kong"}
    energy.replace({"Country": di},inplace = True)
    energy.set_index('Country', inplace = True)
    energy.reset_index(inplace = True)
    ###
    GDP = pd.read_csv('world_bank.csv', skiprows=4)
    GDP.replace('Korea, Rep.','South Korea', inplace=True)
    GDP.replace('Iran, Islamic Rep.','Iran', inplace=True)
    GDP.replace('Hong Kong SAR, China','Hong Kong', inplace=True)
    GDP = GDP.iloc[:,[0,50,51,52,53,54,55,56,57,58,59]]
    GDP.rename(columns={'Country Name':'Country'}, inplace= True)
    GDP.set_index('Country')
    ###
    ScimEn = pd.read_excel('scimagojr-3.xlsx')
    #ScimEn = ScimEn.iloc[0:15,1:]
    ###
    inner_df = ScimEn.merge(GDP,left_on='Country', right_on='Country')
    inner_df = inner_df.merge(energy, left_on='Country', right_on='Country')
    outer_df = ScimEn.merge(GDP,left_on='Country', right_on='Country', how='outer')
    outer_df = outer_df.merge(energy, left_on='Country', right_on='Country', how='outer')
    return len(outer_df)-len(inner_df)
'''
Question 3 
What is the average GDP over the last 10 years for each country? (exclude missing values from this calculation.)
This function should return a Series named avgGDP with 15 countries and their average GDP sorted in descending order.
'''
def answer_three():
    Top15 = answer_one()
    Top15.set_index('Country', inplace=True)
    avgGDP = Top15[['2006', '2007', '2008', '2009','2010', '2011', '2012', '2013', '2014', '2015']].mean(axis=1)
    avgGDP = avgGDP.sort_values(ascending = False)
    return avgGDP
#selecting a column of a dataframe will return a series
'''
Question 4 (6.6%)
By how much had the GDP changed over the 10 year span for the country with the 6th largest average GDP?
This function should return a single number.
'''
def answer_four():
    Top15 = answer_one()
    Top15['avg'] = Top15[['2006', '2007', '2008', '2009','2010', '2011', '2012', '2013', '2014', '2015']].mean(axis=1)
    Top15 = Top15.sort_values('avg', ascending=False)
    #Top15['deltaGDP'] = Top15['2015']-Top15['2006']
    #print(Top15.iloc[5,21])
    return Top15.iloc[5]['2015']-Top15.iloc[5]['2006']
'''
Question 5 (6.6%)
What is the mean Energy Supply per Capita?
This function should return a single number.
'''
print("Question 5")
print(final_df2['Energy Supply per Capita'].mean())
print(final_df2.describe())
'''
Question 6 (6.6%)
What country has the maximum % Renewable and what is the percentage?
This function should return a tuple with the name of the country and the percentage.
'''
def answer_six():
    Top15 = answer_one()
    maxCountry = Top15['% Renewable'].idxmax()
    #tempdf = final_df2.loc[final_df2['% Renewable'].idxmax()]
    #print([maxCountry,tempdf.loc['% Renewable']])
    return (Top15.iloc[maxCountry]['Country'],Top15.iloc[maxCountry]['% Renewable'])
'''
Question 7 (6.6%)
Create a new column that is the ratio of Self-Citations to Total Citations. What is the maximum value for this new column, and what country has the highest ratio?
This function should return a tuple with the name of the country and the ratio.
'''
print("Question 7")
def answer_seven():
    Top15 = answer_one()
    Top15['self-total'] = Top15['Self-citations']/Top15['Citations']
    idmax_self_total = Top15['self-total'].idxmax()
    #max_self_total = final_df2['self-total'].max()
    #print([idmax_self_total,max_self_total])
    return (Top15.iloc[idmax_self_total]['Country'],Top15.iloc[idmax_self_total]['self-total'])
'''
Question 8 (6.6%)
Create a column that estimates the population using Energy Supply and Energy Supply per capita. What is the third most populous country according to this estimate?
This function should return a single string value.
'''
print("Question 8")
def answer_eight():
    Top15 = answer_one()
    Top15['estimatedPop'] = Top15['Energy Supply']/Top15['Energy Supply per Capita']
    Top15 = Top15.sort_values('estimatedPop', ascending=False)
    #ThirdCounrty = final_df2_sorted_est.index[2]
    #ThirdEstimatedPop = final_df2_sorted_est.iloc[2,22]
    #print([ThirdCounrty,ThirdEstimatedPop])
    return Top15
'''
Question 9 (6.6%)
Create a column that estimates the number of citable documents per person. What is the correlation between the number of citable documents per capita and 
the energy supply per capita? Use the .corr() method, (Pearson's correlation).
This function should return a single number.
(Optional: Use the built-in function plot9() to visualize the relationship between Energy Supply per Capita vs. Citable docs per Capita)
'''
def answer_nine():
    Top15 = answer_one()
    Top15['estimatedPop'] = Top15['Energy Supply']/Top15['Energy Supply per Capita']
    Top15['estimatedCDPP'] = Top15['Citable documents']/Top15['estimatedPop']
    cor = Top15[['Citations per document','Energy Supply per Capita']].corr(method ='pearson')
    return cor.iloc[0,1]

def plot9():
    import matplotlib as plt
    %matplotlib inline
    
    Top15 = answer_one()
    Top15['PopEst'] = Top15['Energy Supply'] / Top15['Energy Supply per Capita']
    Top15['Citable docs per Capita'] = Top15['Citable documents'] / Top15['PopEst']
    Top15.plot(x='Citable docs per Capita', y='Energy Supply per Capita', kind='scatter', xlim=[0, 0.0006])
'''
Question 10 (6.6%)
Create a new column with a 1 if the country's % Renewable value is at or above the median for all countries in the top 15, and a 0 if the country's % Renewable value is below the median.
This function should return a series named HighRenew whose index is the country name sorted in ascending order of rank.
'''
def answer_ten():
    Top15 = answer_one()
    Top15.set_index('Country',inplace=True)
    print(Top15.columns)
    median_renewable=Top15['% Renewable'].median()
    #print(median_renewable)
    Top15['HighRenew'] = np.where(Top15['% Renewable']>=median_renewable,1,0)
    return Top15['HighRenew']
'''
Question 11 (6.6%)
Use the following dictionary to group the Countries by Continent, then create a dateframe that displays the sample size (the number of countries in each continent bin), and the sum, mean, and std deviation for the estimated population of each country.

ContinentDict  = {'China':'Asia', 
                  'United States':'North America', 
                  'Japan':'Asia', 
                  'United Kingdom':'Europe', 
                  'Russian Federation':'Europe', 
                  'Canada':'North America', 
                  'Germany':'Europe', 
                  'India':'Asia',
                  'France':'Europe', 
                  'South Korea':'Asia', 
                  'Italy':'Europe', 
                  'Spain':'Europe', 
                  'Iran':'Asia',
                  'Australia':'Australia', 
                  'Brazil':'South America'}
This function should return a DataFrame with index named Continent ['Asia', 'Australia', 'Europe', 'North America', 'South America'] and columns ['size', 'sum', 'mean', 'std']
'''
def answer_eleven():
    Top15 = answer_one()
    ContinentDict  = {'China':'Asia', 
                  'United States':'North America', 
                  'Japan':'Asia', 
                  'United Kingdom':'Europe', 
                  'Russian Federation':'Europe', 
                  'Canada':'North America', 
                  'Germany':'Europe', 
                  'India':'Asia',
                  'France':'Europe', 
                  'South Korea':'Asia', 
                  'Italy':'Europe', 
                  'Spain':'Europe', 
                  'Iran':'Asia',
                  'Australia':'Australia', 
                  'Brazil':'South America'}
    Top15["Continent"]=Top15['Country'].map(ContinentDict)
    Top15['estimatedPop'] = Top15['Energy Supply']/Top15['Energy Supply per Capita']
    Top15=Top15.groupby("Continent")
    #data = {'Continent':['Asia', 'Australia', 'Europe', 'North America', 'South America'], 'size':[5, 1, 6, 2, 1]}
    #ContinentDF = pd.DataFrame(data) 
    #print(ContinentDF)
    idxlist = ['Asia', 'Australia', 'Europe', 'North America', 'South America']
    clnlist = ['size', 'sum', 'mean', 'std']
    df = pd.DataFrame(index=idxlist, columns=clnlist)
    df['size']=Top15.size()
    df['sum']=Top15['estimatedPop'].sum()
    df['mean']=Top15['estimatedPop'].mean()
    df['std']=Top15['estimatedPop'].std()
    return df
answer_eleven()
'''
Question 12 (6.6%)
Cut % Renewable into 5 bins. Group Top15 by the Continent, as well as these new % Renewable bins. How many countries are in each of these groups?
This function should return a Series with a MultiIndex of Continent, then the bins for % Renewable. Do not include groups with no countries.
'''
def answer_twelve():
    Top15 = answer_one()
    ContinentDict  = {'China':'Asia', 
                  'United States':'North America', 
                  'Japan':'Asia', 
                  'United Kingdom':'Europe', 
                  'Russian Federation':'Europe', 
                  'Canada':'North America', 
                  'Germany':'Europe', 
                  'India':'Asia',
                  'France':'Europe', 
                  'South Korea':'Asia', 
                  'Italy':'Europe', 
                  'Spain':'Europe', 
                  'Iran':'Asia',
                  'Australia':'Australia', 
                  'Brazil':'South America'}
    Top15['bins'] = pd.cut(Top15['% Renewable'],5)
    Top15["Continent"]=Top15['Country'].map(ContinentDict)
    Top15 = Top15.groupby(['Continent', 'bins'])
    return Top15.size()
'''
Question 13 (6.6%)
Convert the Population Estimate series to a string with thousands separator (using commas). Do not round the results.
e.g. 317615384.61538464 -> 317,615,384.61538464
This function should return a Series PopEst whose index is the country name and whose values are the population estimate string.
'''
def answer_thirteen():
    Top15 = answer_one()
    Top15["estimatePop"] = Top15['Energy Supply'] / Top15['Energy Supply per Capita']
    return Top15['estimatePop'].apply(lambda x: '{0:,}'.format(x))
'''
Optional
Use the built in function plot_optional() to see an example visualization.
'''
def plot_optional():
    import matplotlib as plt
    %matplotlib inline
    Top15 = answer_one()
    ax = Top15.plot(x='Rank', y='% Renewable', kind='scatter', 
                    c=['#e41a1c','#377eb8','#e41a1c','#4daf4a','#4daf4a','#377eb8','#4daf4a','#e41a1c',
                       '#4daf4a','#e41a1c','#4daf4a','#4daf4a','#e41a1c','#dede00','#ff7f00'], 
                    xticks=range(1,16), s=6*Top15['2014']/10**10, alpha=.75, figsize=[16,6]);

    for i, txt in enumerate(Top15.index):
        ax.annotate(txt, [Top15['Rank'][i], Top15['% Renewable'][i]], ha='center')
        
    print("This is an example of a visualization that can be created to help understand the data. \
           This is a bubble chart showing % Renewable vs. Rank. The size of the bubble corresponds to the countries' \
           2014 GDP, and the color corresponds to the continent.")
