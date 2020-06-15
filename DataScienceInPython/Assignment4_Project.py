'''
Assignment 4 - Hypothesis Testing
This assignment requires more individual learning than previous assignments - you are encouraged to check out the pandas documentation to find functions or methods you might not have used yet, or ask questions on Stack Overflow and tag them as pandas and python related. And of course, the discussion forums are open for interaction with your peers and the course staff.

Definitions:

A quarter is a specific three month period, Q1 is January through March, Q2 is April through June, Q3 is July through September, Q4 is October through December.
A recession is defined as starting with two consecutive quarters of GDP decline, and ending with two consecutive quarters of GDP growth.
A recession bottom is the quarter within a recession which had the lowest GDP.
A university town is a city which has a high percentage of university students compared to the total population of the city.
Hypothesis: University towns have their mean housing prices less effected by recessions. Run a t-test to compare the ratio of the mean price of houses in university towns the quarter before the recession starts compared to the recession bottom. (price_ratio=quarter_before_recession/recession_bottom)

The following data files are available for this assignment:

From the Zillow research data site there is housing data for the United States. In particular the datafile for all homes at a city level, City_Zhvi_AllHomes.csv, has median home sale prices at a fine grained level.
From the Wikipedia page on college towns is a list of university towns in the United States which has been copy and pasted into the file university_towns.txt.
From Bureau of Economic Analysis, US Department of Commerce, the GDP over time of the United States in current dollars (use the chained value in 2009 dollars), in quarterly intervals, in the file gdplev.xls. For this assignment, only look at GDP data from the first quarter of 2000 onward.
Each function in this assignment below is worth 10%, with the exception of run_ttest(), which is worth 50%.
'''
import pandas as pd
import numpy as np
from scipy.stats import ttest_ind

# Use this dictionary to map state names to two letter acronyms
states = {'OH': 'Ohio', 'KY': 'Kentucky', 'AS': 'American Samoa', 'NV': 'Nevada', 'WY': 'Wyoming', 'NA': 'National', 'AL': 'Alabama', 'MD': 'Maryland', 'AK': 'Alaska', 'UT': 'Utah', 'OR': 'Oregon', 'MT': 'Montana', 'IL': 'Illinois', 'TN': 'Tennessee', 'DC': 'District of Columbia', 'VT': 'Vermont', 'ID': 'Idaho', 'AR': 'Arkansas', 'ME': 'Maine', 'WA': 'Washington', 'HI': 'Hawaii', 'WI': 'Wisconsin', 'MI': 'Michigan', 'IN': 'Indiana', 'NJ': 'New Jersey', 'AZ': 'Arizona', 'GU': 'Guam', 'MS': 'Mississippi', 'PR': 'Puerto Rico', 'NC': 'North Carolina', 'TX': 'Texas', 'SD': 'South Dakota', 'MP': 'Northern Mariana Islands', 'IA': 'Iowa', 'MO': 'Missouri', 'CT': 'Connecticut', 'WV': 'West Virginia', 'SC': 'South Carolina', 'LA': 'Louisiana', 'KS': 'Kansas', 'NY': 'New York', 'NE': 'Nebraska', 'OK': 'Oklahoma', 'FL': 'Florida', 'CA': 'California', 'CO': 'Colorado', 'PA': 'Pennsylvania', 'DE': 'Delaware', 'NM': 'New Mexico', 'RI': 'Rhode Island', 'MN': 'Minnesota', 'VI': 'Virgin Islands', 'NH': 'New Hampshire', 'MA': 'Massachusetts', 'GA': 'Georgia', 'ND': 'North Dakota', 'VA': 'Virginia'}
print(states)
f = open('university_towns.txt', 'r')
file_contents = f.read()
#print(file_contents)
f.close()

def get_list_of_university_towns():
    '''Returns a DataFrame of towns and the states they are in from the 
    university_towns.txt list. The format of the DataFrame should be:
    DataFrame( [ ["Michigan", "Ann Arbor"], ["Michigan", "Yipsilanti"] ], 
    columns=["State", "RegionName"]  )
    
    The following cleaning needs to be done:

    1. For "State", removing characters from "[" to the end.
    2. For "RegionName", when applicable, removing every character from " (" to the end.
    3. Depending on how you read the data, you may need to remove newline character '\n'. '''
    
    f = open('university_towns.txt', 'r')
    file_contents = f.readlines()
    #print(len(file_contents))
    f.close()
    df = pd.DataFrame(columns=['State', 'RegionName'])
    idx = 0
    #with open('university_towns.txt') as file:
    for line in file_contents:
            if '[edit]' in line:
                tempstate = line.split('[')[0]
                tempstate = tempstate.replace('\n','').strip()
            else:
                if ':' in line:
                    temptown = line.split(':')[0]
                    temptown = temptown.replace('\n','').strip()
                    df.loc[idx]=[tempstate, temptown]
                    idx += 1
                elif '(' in line:
                    temptown = line.split('(')[0]
                    temptown = temptown.replace('\n','').strip()
                    df.loc[idx]=[tempstate, temptown]
                    idx += 1
                else:
                    temptown = line.strip()
                    df.loc[idx]=[tempstate, temptown]
                    idx += 1
                
    return df


''' This is a solution from online that matches the correct answer. However I don't know why my solution doesn't match the answer
import re
    import pandas as pd

    # Open the file, read the lines, and close the file
    fo = open('university_towns.txt', "r")
    lines = fo.readlines()
    fo.close()

    # remove empty lines
    new_lines = []
    for line in lines:
        if not re.match(r'^\s*$', line):
            new_lines.append(line)

    lines = new_lines.copy()

    # Strip the white space at the beginning and end of each line
    for index, line in enumerate(lines):
        lines[index] = line.strip()

        # Loop through the lines to form a dataframe
    df_result = pd.DataFrame(columns=('State', 'RegionName'))
    i = 0  # counter for each new line in the dataframe
    state_string = ""  # Empty initial state string
    region_string = ""  # Empty initial region string
    for line in lines:
        if '[edit]' in line:
            state_string = line.replace('[edit]', "")
        else:
            region_string = re.sub(r' \(.*', "", line)
            df_result.loc[i] = [state_string, region_string]
            i += 1
            
    return df_result
 '''
#print(get_list_of_university_towns())

def get_recession_start():
    '''Returns the year and quarter of the recession start time as a 
    string value in a format such as 2005q3

    NOTE: 
    A recession is defined as starting with two consecutive quarters of GDP decline, and ending with two consecutive quarters of GDP growth.
    '''
    gdp = pd.read_excel('gdplev.xls', header=5, skiprows=2, usecols=[4,5,6])
    gdp.columns = ['quarter', 'gdp_current', 'gdp_chained']
    #print(gdp[220:])
    first = gdp.iloc[212]
    second = gdp.iloc[213]
    recessQuarter = ""
    for index, row in gdp.iloc[214:].iterrows():
      #print(row)
      if row['gdp_chained'] < second['gdp_chained'] and second['gdp_chained'] < first['gdp_chained']:
            recessQuarter = second['quarter']
            break
      else :
            first = second
            second = row
    return recessQuarter
#print(get_recession_start())

def get_recession_end():
    '''Returns the year and quarter of the recession end time as a 
    string value in a format such as 2005q3
    
    NOTE: A recession is defined as starting with two consecutive quarters of GDP decline, and ending with two consecutive quarters of GDP growth.
    '''
    gdp = pd.read_excel('gdplev.xls', header=5, skiprows=2, usecols=[4,5,6])
    gdp.columns = ['quarter', 'gdp_current', 'gdp_chained']
    first = gdp.iloc[212]
    second = gdp.iloc[213]
    recessQuarter = ""
    for index, row in gdp.iloc[214:].iterrows():
      #print(row)
      if row['gdp_chained'] > second['gdp_chained'] and second['gdp_chained'] > first['gdp_chained'] and row['quarter']> get_recession_start():
            return row['quarter']
      else :
            first = second
            second = row
    return recessQuarter

#print(get_recession_end())


def get_recession_bottom():
    '''Returns the year and quarter of the recession bottom time as a 
    string value in a format such as 2005q3

    NOTE: A recession bottom is the quarter within a recession which had the lowest GDP.
    '''
    
    gdp = pd.read_excel('gdplev.xls', header=5, skiprows=2, usecols=[4,5,6])
    gdp.columns = ['quarter', 'gdp_current', 'gdp_chained']
    bottom = gdp.iloc[212]
    start = get_recession_start()
    end = get_recession_end()
    if not start:
      return ""
    if not end:
      return ""
    for index, row in gdp.iloc[214:].iterrows():
      if row['quarter'] == start or row['quarter'] <= end:
            bottom = row
    for index, row in gdp.iloc[214:].iterrows():
      if row['quarter'] >= start and row['quarter'] <= end and row['gdp_chained'] < bottom['gdp_chained']:
            bottom = row
    return bottom['quarter']

#print(get_recession_bottom())

def convert_housing_data_to_quarters():
    '''Converts the housing data to quarters and returns it as mean 
    values in a dataframe. This dataframe should be a dataframe with
    columns for 2000q1 through 2016q3, and should have a multi-index
    in the shape of ["State","RegionName"].
    
    Note: Quarters are defined in the assignment description, they are
    not arbitrary three month periods.
    
    The resulting dataframe should have 67 columns, and 10,730 rows.
    '''
    df = pd.read_csv("City_Zhvi_AllHomes.csv", encoding = "latin")
    newdf = pd.DataFrame()
    df_state_region = df.loc[:, ['State', 'RegionName']]
    df_housing_price = df.loc[:, '2000-01':'2016-09']
    newdf = df_state_region #pd.concat(df_state_region, df_housing_price, axis=1)
    months = df_housing_price.columns
    for (columnName, columnData) in df_housing_price.iteritems():
      current_loc = months.get_loc(columnName)
      if "-01" in columnName:
            tempDF = df_housing_price.iloc[:, current_loc:current_loc+3]
            newdf[columnName.replace('-01','q1')] = tempDF.mean(axis=1, skipna = True)
      if "-04" in columnName:
            tempDF = df_housing_price.iloc[:, current_loc:current_loc+3]
            newdf[columnName.replace('-04','q2')] = tempDF.mean(axis=1, skipna = True)
      if "-07" in columnName:
            tempDF = df_housing_price.iloc[:, current_loc:current_loc+3]
            newdf[columnName.replace('-07','q3')] = tempDF.mean(axis=1, skipna = True)
      if "-10" in columnName:
            tempDF = df_housing_price.iloc[:, current_loc:current_loc+3]
            newdf[columnName.replace('-10','q4')] = tempDF.mean(axis=1, skipna = True)

    newdf.set_index(['State', 'RegionName'], inplace=True)
    return newdf
  
#print(convert_housing_data_to_quarters())

def run_ttest():
    '''First creates new data showing the decline or growth of housing prices
    between the recession start and the recession bottom. Then runs a ttest
    comparing the university town values to the non-university towns values, 
    return whether the alternative hypothesis (that the two groups are the same)
    is true or not as well as the p-value of the confidence. 
    
    Return the tuple (different, p, better) where different=True if the t-test is
    True at a p<0.01 (we reject the null hypothesis), or different=False if 
    otherwise (we cannot reject the null hypothesis). The variable p should
    be equal to the exact p value returned from scipy.stats.ttest_ind(). The
    value for better should be either "university town" or "non-university town"
    depending on which has a lower mean price ratio (which is equivilent to a
    reduced market loss).'''
    states = {'OH': 'Ohio', 'KY': 'Kentucky', 'AS': 'American Samoa', 'NV': 'Nevada', 'WY': 'Wyoming', 'NA': 'National', 'AL': 'Alabama', 'MD': 'Maryland', 'AK': 'Alaska', 'UT': 'Utah', 'OR': 'Oregon', 'MT': 'Montana', 'IL': 'Illinois', 'TN': 'Tennessee', 'DC': 'District of Columbia', 'VT': 'Vermont', 'ID': 'Idaho', 'AR': 'Arkansas', 'ME': 'Maine', 'WA': 'Washington', 'HI': 'Hawaii', 'WI': 'Wisconsin', 'MI': 'Michigan', 'IN': 'Indiana', 'NJ': 'New Jersey', 'AZ': 'Arizona', 'GU': 'Guam', 'MS': 'Mississippi', 'PR': 'Puerto Rico', 'NC': 'North Carolina', 'TX': 'Texas', 'SD': 'South Dakota', 'MP': 'Northern Mariana Islands', 'IA': 'Iowa', 'MO': 'Missouri', 'CT': 'Connecticut', 'WV': 'West Virginia', 'SC': 'South Carolina', 'LA': 'Louisiana', 'KS': 'Kansas', 'NY': 'New York', 'NE': 'Nebraska', 'OK': 'Oklahoma', 'FL': 'Florida', 'CA': 'California', 'CO': 'Colorado', 'PA': 'Pennsylvania', 'DE': 'Delaware', 'NM': 'New Mexico', 'RI': 'Rhode Island', 'MN': 'Minnesota', 'VI': 'Virgin Islands', 'NH': 'New Hampshire', 'MA': 'Massachusetts', 'GA': 'Georgia', 'ND': 'North Dakota', 'VA': 'Virginia'}
    housing_data_quarters = convert_housing_data_to_quarters()
    housing_data_quarters = housing_data_quarters.reset_index()
    print('housing_data_quarters')
    print(housing_data_quarters)
    housing_data_quarters['StateAcronyms'] = housing_data_quarters['State'].map(states)
    recession_start = get_recession_start()
    recession_bottom = get_recession_bottom()
    quarters = housing_data_quarters.columns
    
    print('housing_data_quarters')
    print(housing_data_quarters)
    print('recession_start')
    print(recession_start)
    print('recession_bottom')
    print(recession_bottom)

    univ_towns = get_list_of_university_towns()
    univ_towns['univ_town'] = True

    print('univ_towns')
    print(univ_towns)

    df = pd.merge(housing_data_quarters, univ_towns, how="left", left_on=['StateAcronyms', 'RegionName'], right_on=['State', 'RegionName'])
    df['univ_town'].fillna(False, inplace=True)
    df['price_ratio']=df[recession_start]/df[recession_bottom]
    univ_town_ratio = df[df['univ_town']==True]['price_ratio']
    non_univ_town_ratio = df[df['univ_town']==False]['price_ratio']
    ttest_result = ttest_ind(univ_town_ratio, non_univ_town_ratio, nan_policy='omit')

    p=ttest_result[1]

    if p<0.01:
      different = True 
    else:
      different = False

    if univ_town_ratio.mean()<non_univ_town_ratio.mean():
      better = "university town"
    else :
      better = "non-university town"
    return (different, p, better)


print(run_ttest())
