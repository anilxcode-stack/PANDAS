""" Merge DataFrame in Pandas """

'''
Merging means combining two or more DataFrames based 
on a common column or index.
'''
'''
Main Function Used
pd.merge(left, right, how='inner', on=None)
Parameters:
left → First DataFrame
right → Second DataFrame
how → Type of join
on → Common column
left_on, right_on → Different column names
left_index, right_index → Merge using index
'''

# Types of Merge 

""" Inner JOIN """
# Keeps only matching values from bothh DataFrames

# import pandas as pd

# df1 = pd.DataFrame({
#     'ID' : [1, 2, 3],
#     'Name' : ['A', 'B', 'C']
# })

# df2 = pd.DataFrame({
#     'ID' : [2, 3, 4],
#     'Salary' : [200, 300, 400]
# })

# result = pd.merge(df1, df2, on="ID", how="inner")
# print(result)


# __________________________________________________________________

""" LEFT JOIN """
# Keeps all rows from left DataFrame

# import pandas as pd

# df1 = pd.DataFrame({
#     'ID' : [1, 2, 3],
#     'Name' : ['A', 'B', 'C']
# })

# df2 = pd.DataFrame({
#     'ID' : [2, 3, 4],
#     'Salary' : [200, 300, 400]
# })

# result = pd.merge(df1, df2, on='ID', how='left')
# print(result)

# ______________________________________________________
""" RIGHT JOIN """
# Keeps all rows from right DataFrame

import pandas as pd

df1 = pd.DataFrame({
    'ID' : [1, 2, 3],
    'Name' : ['A', 'B', 'C']
})

df2 = pd.DataFrame({
    'ID' : [2, 3, 4],
    'Salary' : [200, 300, 400]
})


result = pd.merge(df1, df2, on="ID", how='right')
print(result)