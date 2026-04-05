""" Apply keyword in Pandas """

'''
apply() is used to apply a function to:

each row
each column
or each element

Think of it as:

“Run this function on my data”

2. Syntax
DataFrame.apply(function, axis=0)
'''

""" Apply on Columns (axis = 0) column by column """

# import pandas as pd

# df = pd.DataFrame({
#     'A':[1, 2, 3],
#     'B' : [4, 5, 6]
# })

# # Sum of each column
# result = df.apply(sum)
# print(result)

# _____________________________________________________________
""" Apply on Rows (axis = 1) """

# Sum of each row
# result = df.apply(sum, axis=1)
# print(result) # Each column is passed to sum()

# _____________________________________________________________
""" Apply with Custom Function """

# def square(x):
#     return x * x

# df = pd.DataFrame({
#     'A' : [1, 2, 3]
# })

# result = df['A'].apply(square)
# print(result)


# ____________________________________________________________

""" Using Lambda Function (Shortcut) """

# import pandas as pd

# df = pd.DataFrame({
#     'A':[1, 2, 3],
#     'B' : [4, 5, 6]
# })

# df['A_squared'] = df['A'].apply(lambda x: x*x)
# print(df)

# ________________________________________________________________

""" Apply on Multiple Columns (Row-wise logic)"""
# import pandas as pd
# df = pd.DataFrame({
#     'Name':['A', 'B', 'C'],
#     'Math':[80, 70, 90],
#     'Science':[85, 75, 95]
# })

# #Total marks
# df['Total'] = df.apply(lambda row: row['Math'] + row['Science'], axis=1)

# print(df)

# ____________________________________________________________

""" Apply with Conditional Logic """


# import pandas as pd
# df = pd.DataFrame({
#     'Name':['A', 'B', 'C'],
#     'Math':[80, 70, 90],
#     'Science':[85, 75, 95]
# })

# def grade(marks):
#     if marks >= 80:
#         return "A"
#     else:
#         return 'B'

# df['Grade'] = df['Math'].apply(grade)
# print(df)

# ______________________________________________


""" Apply on Entire DataFrame (Element-wise)"""
# import pandas as pd

# df = pd.DataFrame({
#     'A': [1, 2],
#     'B': [3, 4]
# })

# result = df.applymap(lambda x: x * 10)
# print(result)

#_____________________________________________________________

""" Apply in GroupBy """

# import pandas as pd

# df = pd.DataFrame({
#     'Dept' : ['IT', 'IT', 'HR'],
#     'Salary' : [50000, 60000, 40000]
# })

# result = df.groupby('Dept')['Salary'].apply(lambda x: x.mean())
# print(result)

#___________________________________________________________

""" Real-world Example (ML Style) """

import pandas as pd

df = pd.DataFrame({
    'Age':[18, 25, 40]
})

# Feature engineering
df['Age_Group'] = df['Age'].apply(lambda x: 'Young' if x < 30 else 'Adult')
print(df)