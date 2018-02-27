import pandas as pd 

medals = pd.read_csv('summer.csv')

# Extract all rows for which the 'Year' is between 1952 & 1988: during_cold_war
during_cold_war = (medals.Year >= 1952) & (medals.Year <= 1988)

# Extract rows for which 'Country' is either 'USA' or 'URS': is_usa_urs
is_usa_urs = medals.Country.isin(['USA', 'URS'])

# Use during_cold_war and is_usa_urs to create the DataFrame: cold_war_medals
cold_war_medals = medals.loc[during_cold_war & is_usa_urs]

# Group cold_war_medals by 'Country'
country_grouped = cold_war_medals.groupby('Country')

# Create Nsports
Nsports = country_grouped['Sport'].nunique().sort_values(ascending=False)

Nsports = Nsports.rename('Unique Sports Won')

# Print Nsports
print(Nsports)


# Create the pivot table: medals_won_by_country
medals_won_by_country = medals.pivot_table(index='Year',columns='Country',values='Athlete',aggfunc='count')

# Slice medals_won_by_country: cold_war_usa_usr_medals
cold_war_usa_usr_medals = medals_won_by_country.loc[1952:1988, ['USA','URS']]

# Create most_medals 
most_medals = cold_war_usa_usr_medals.idxmax(axis='columns')
most_medals = most_medals.rename('Country with most medals per year')

# Print most_medals & most_medals.value_counts()
print(most_medals)
print(most_medals.value_counts())
