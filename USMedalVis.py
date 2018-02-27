import pandas as pd 
import matplotlib.pyplot as plt


medals = pd.read_csv('summer.csv')

#Make medals['Medal'] categorical
medals.Medal = pd.Categorical(values=medals.Medal, categories=['Bronze', 'Silver', 'Gold'], ordered=True)

# Create the DataFrame: usa
usa = medals[medals['Country'] == 'USA']

# Group usa by ['Edition', 'Medal'] and aggregate over 'Athlete'
usa_medals_by_year = usa.groupby(['Year', 'Medal'])['Athlete'].count()

# Reshape usa_medals_by_year by unstacking
usa_medals_by_year = usa_medals_by_year.unstack(level='Medal')

print(usa_medals_by_year)


# Plot the DataFrame usa_medals_by_year
plt.style.use('ggplot')
usa_medals_by_year.plot.area()

plt.show()