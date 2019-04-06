# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file

# loading the dataset
data = pd.read_csv(path)

# renaming the column
data.rename(columns = {'Total':'Total_Medals'},inplace = True)

# displaying the first 10 records
data.head(10)

#Code starts here



# --------------

data['Better_Event'] = np.where(data['Total_Summer'] > data['Total_Winter'],'Summer',(
                                np.where( data['Total_Summer'] < data['Total_Winter'],'Winter','Both' )))


better_event = data['Better_Event'].value_counts(ascending = False).idxmax()


# --------------
#Code starts here

top_countries = data[['Country_Name','Total_Summer', 'Total_Winter','Total_Medals']]

# dropping the last row as it contains the sum of all the columns
top_countries = top_countries.iloc[:-1,:]

def top_ten(top_countries,column):
    
    # creating a new empty list
    country_list = list()
    
    # type casting the pandas.Series object to list
    country_list = list(top_countries.nlargest(10,column)['Country_Name'])

    return country_list

top_10_summer, top_10_winter,top_10 = top_ten(top_countries,'Total_Summer'),top_ten(top_countries,'Total_Winter'),top_ten(top_countries,'Total_Medals')

# storing the common elemtns between 3 lists
common = list(set(top_10_summer) & set(top_10_winter) & set(top_10))
print(common)


# --------------
#Code starts here

summer_df = data[data['Country_Name'].isin(top_10_summer)]
winter_df = data[data['Country_Name'].isin(top_10_winter)]
top_df = data[data['Country_Name'].isin(top_10)]

# plotting bar grap

fig,(ax_1,ax_2,ax_3) = plt.subplots(1,3,figsize = (20,10))

summer_df['Country_Name'].value_counts().plot(kind="bar",ax = ax_1)
ax_1.set_xlabel("Country Names")
ax_1.set_ylabel("Frequency")
ax_1.set_title("Top 10 Summer")

winter_df['Country_Name'].value_counts().plot(kind="bar",ax = ax_2)
ax_2.set_xlabel("Country Names")
ax_2.set_ylabel("Frequency")
ax_2.set_title("Top 10 Winter")

top_df['Country_Name'].value_counts().plot(kind="bar",ax = ax_3)
ax_3.set_xlabel("Country Names")
ax_3.set_ylabel("Frequency")
ax_3.set_title("Top 10")

plt.show()


# --------------
#Code starts here


summer_df['Golden_Ratio'] = summer_df['Gold_Summer'] / summer_df['Total_Summer']



summer_max_ratio = max(summer_df['Golden_Ratio'].value_counts().keys())


summer_country_gold = list(summer_df[summer_df['Golden_Ratio'] == summer_max_ratio]['Country_Name'])[0]

winter_df['Golden_Ratio'] = winter_df['Gold_Winter'] / winter_df['Total_Winter']

winter_max_ratio = max(winter_df['Golden_Ratio'].value_counts().keys())


winter_country_gold = list(winter_df[winter_df['Golden_Ratio'] == winter_max_ratio]['Country_Name'])[0]

top_df['Golden_Ratio'] = top_df['Gold_Total'] / top_df['Total_Medals']

top_max_ratio = max(top_df['Golden_Ratio'].value_counts().keys())


top_country_gold = list(top_df[top_df['Golden_Ratio'] == top_max_ratio]['Country_Name'])[0]




# --------------
#Code starts here
data_1 = data.iloc[:-1,:-2]

data_1['Total_Points'] = data_1['Gold_Total'] * 3 + data_1['Silver_Total'] * 2 + data_1['Bronze_Total']

# fnding the maximum value
most_points = data_1['Total_Points'].max()

# finding the country associated with most points
best_country = list(data_1[data_1['Total_Points'] == most_points ]['Country_Name'])[0]



# --------------
#Code starts here

best = data[data['Country_Name'] == best_country]

best = best[['Gold_Total','Silver_Total','Bronze_Total']]

best.plot(kind="bar",stacked = True)
plt.xlabel("United States")
plt.ylabel("Medals Tally")
plt.xticks(rotation = 45)
plt.show()


