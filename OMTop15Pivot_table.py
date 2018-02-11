import pandas as pd 

medals = pd.read_csv('Summer.csv')

# Construct the pivot table: counted
counted = medals.pivot_table(index="Country",columns='Medal',values='Athlete',aggfunc='count')

# Group medals by 'Country': country_grouped
country_grouped = medals.groupby('Country')

# Compute the number of distinct sports in which each country won medals: Nsports
Nsports = country_grouped['Sport'].nunique()

# Create the new column: counted['Unique']
counted['Unique'] = Nsports

# Create the new column: counted['Totals']
counted['Totals'] = counted[['Gold', 'Silver', 'Bronze']].sum(axis='columns')

# Sort counted by the 'totals' column
counted = counted.sort_values('Totals', ascending=False)

# Print the top 15 rows of counted
print(counted.head(15))


