""" Filtering Columns and Rows in Pandas """

import pandas as pd

df = pd.read_csv(r"C:\Users\lenovo\Downloads\world_population (1).csv")

# print(df)

# __________________________________________________________________

# result = df[df['Rank'] <= 10]
# print(result)

# ____________________________________________________________

# specific_countries = ['Bangladesh', 'Brazil']
# result2 = df[df['Country'].isin(specific_countries)]
# print(result2)

# ________________________________________________________

# result3 = df[df['Country'].str.contains('United')]
# print(result3)

# _________________________________________________________
df2 = df.set_index('Country')


# _____________________________________________________________

# result = df2.filter(items= ['Continent', 'CCA3'], axis = 1)
# print(result)

# __________________________________________________________

# result2 = df2.filter(items= ['Zimbabwe'], axis = 0)
# print(result2)

# ______________________________________________________________

# result3 = df2.filter(like= 'United', axis = 0)
# print(result3)

# ____________________________________________________________

# result4 = df2.loc['United States']
# print(result4)

# ____________________________________________________________

# result5 = df2.iloc[3]
# print(result5)

# _____________________________________________________________

result6 = df[df['Rank'] < 10].sort_values(by=['Continent', 'Country'], ascending=[False, True])
print(result6)