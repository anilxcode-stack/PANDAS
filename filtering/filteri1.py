""" Filtering in Pandas """

"""
Filtering means:

Selecting specific rows based on conditions
Selecting specific columns based on names
"""

# import pandas as pd

# data = {
#     'Name' : ['Anil', 'Rahul', 'Priya', 'Sneha', 'Amit', 'Naha'],
#     'Age' : [20, 21, 19, 22, 23, 20],
#     'Department' : ['CSE', 'IT', 'CSE', 'ECE', 'IT', 'CSE'],
#     'Marks' : [85, 78, 92, 70, 88, 95],
#     'City' : ['Indore', 'Delhi', 'Mumbai', 'Indore', 'Delhi', 'Mumbai']
# }

# df = pd.DataFrame(data)
# print(df)

# ___________________________________________________________
""" Filtering Rows """

# result = df[df['Marks'] > 80]
# print(result)

# _____________________________________________________________

""" Multiple Condition Filtering """

# result = df[(df['Marks'] > 80) & (df['Department'] == 'CSE')]
# print(result)

# ____________________________________________________________

""" Using .isin() (Multiple Values) """

# cities = ['Indore', 'Delhi']
# result = df[df['City'].isin(cities)]
# print(result)

# ____________________________________________________________

""" Using .str.contains() """

# result = df[df['Name'].str.contains('a')]
# print(result)

'''
Returns names containing letter 'a'
Case-sensitive by default
'''

# ________________________________________________________________

""" Setting Index """

# df2 = df.set_index('Name')
# print(df2)

# ___________________________________________________________________

""" Filter Columns """

# result = df2.filter(items=['Age', 'Marks'], axis = 1)
# print(result)

# _________________________________________________________________

# result = df2.filter(items=['Anil', 'Naha'], axis=0)
# print(result)

# ______________________________________________________________

""" Using like """

# result = df2.filter(like='a', axis=0) #Select names containing 'a'
# print(result)

# _______________________________________________________________

""" Using .loc[] """

# result = df2.loc['Anil']
# print(result)

# _____________________________________________________________

""" Using .iloc[] """

# result = df2.iloc[2] # Access 3rd row
# print(result)


# __________________________________________________________________

""" Filtering + Sorting """

# result = df[df['Marks'] > 75].sort_values(
#     by=['Department', 'Marks'],
#     ascending=[True, False]
# )
# print(result)


# _____________________________________________________________
""" Filtering Part """

# result = df[df['Marks'] > 75]
# print(result)

# ______________________________________________________________

# Another code example

import pandas as pd

# Step 1: Create DataFrame
data = {
    'Name' :['Anil', 'Rahul', 'Priya', 'Sneha', 'Amit', 'Neha'],
    'Department' : ['CSE', 'IT', 'CSE', 'ECE', 'IT', 'CSE'],
    'Marks': [85, 78, 92, 70, 88, 95]
}

df = pd.DataFrame(data)

print("Original DataFrame:\n")
print(df)

# Step 2 : Filter + Sort
result = df[df['Marks'] > 75].sort_values(
    by=['Department', 'Marks'],
    ascending=[True, False]
)

# Step 3: Print Result
print("\nFiltered and Sorted Data:\n")
print(result)