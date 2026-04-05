""" Grouping by a Single Column """ """ By GFG's """

import pandas as pd

df = pd.read_csv("C:/Users/lenovo/Downloads/nba (2).csv")

# team = df.groupby('Team')
# print(team.first()) # Let's print the first entries in all the groups formed.


# _______________________________________________________________________

""" Grouping by Multiple Columns """

# grouping = df.groupby(['Team', 'Position'])
# print(grouping.first())

# ________________________________________________________________

""" Apply Aggregation with GroupBy """

# aggregated_data = df.groupby(['Team', 'Position']).agg(
#     total_salary = ('Salary', 'sum'),
#     avg_salary = ('Salary', 'mean'),
#     player_count = ('Name', 'count')
# )

# print(aggregated_data)


# ________________________________________________________________

""" Apply Transformation Methods """

# Rank players within each team by salary
# df['Rank within Team'] = df.groupby('Team')['Salary'].transform(lambda x: x.rank(ascending = False))
# print(df)

# ______________________________________________________________

# Filter groups where the average Salary is >= 5 million
filtered_df = df.groupby('Team').filter(lambda x: x['Salary'].mean() >= 1000000)
print(filtered_df)