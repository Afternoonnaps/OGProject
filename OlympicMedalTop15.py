import pandas as pd 

medals = pd.read_csv('summer.csv')

# Select the 'Country' column of medals: country_names
country_names = medals.loc[:,'Country']

# Count the number of medals won by each country: medal_counts
medal_counts = country_names.value_counts()

# Print top 15 countries ranked by medals
print(medal_counts.head(15))

