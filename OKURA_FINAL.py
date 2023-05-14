import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import calendar

#load in data
data_filepath = "NASA Harvest Data - April.csv"
nasa_data = pd.read_csv(data_filepath)

# cut down data to two columns
mod_data = nasa_data[['CreationDate', 'Are there no crops (fallow or pasture), one crop, or multiple crops growing in the field?']]

# rename column with long name
mod_data.rename({'Are there no crops (fallow or pasture), one crop, or multiple crops growing in the field?': 'CropType'}, axis=1, inplace=True)

# convert CreationDate column to month abbreviation only
mod_data['month'] = pd.DatetimeIndex(mod_data['CreationDate']).month
mod_data['month'] = mod_data['month'].apply(lambda x: calendar.month_abbr[x])

#Create dataframe and populate with 0s
index = ['Jan', 'Feb', 'Mar', 'Apr']
columns = ['Fallow', 'Multiple crops', 'One crop', 'Pasture', 'Home garden or irregular', 'Windbreak', 'MonthTotal']
df = pd.DataFrame(index=index, columns=columns)
df = df.fillna(0)

#Populate dateframe with totals of each crop type according to month
for i in index:
    m = 0
    for j in columns:
        n = len(mod_data[(mod_data["month"]==i) & (mod_data["CropType"]==j)])
        df.loc[i][j] = n
        m += n
    df.loc[i]['MonthTotal'] = m

#Grid
sns.set(style="whitegrid", color_codes=True)

#initialize subplots and set fig size
f, ax = plt.subplots(figsize=(11.7, 8.27))

# set color code and specify bars
sns.set_color_codes("deep")
sns.barplot(x="MonthTotal", y=df.index, data=df, label="Total", color="r")
sns.barplot(x="One crop", y=df.index, data=df, label="One Crop", color="c")

# title
plt.title('Number of One Crop Fields Observed In Each Month', fontsize=20)

# legend
ax.legend(ncol=1, loc="center right")
ax.set(xlim=(0, 300), ylabel="MONTH", xlabel="# OF RECORDS")

# Show plot
plt.show()
