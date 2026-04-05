""" Indexing in Pandas DataFrame """

""" DataFrame.iat[] """

''' Access a single scalar value using integer position (row, column).'''

'''
Syntax
df.iat[row_index, col_index]
'''

# import pandas as pd

# df = pd.DataFrame({
#     'Name' : ['Anil', 'Rahul', 'Priya'],
#     'Age':[20, 22, 21]
# })

# print(df.iat[1, 0])  # Row 1, Column 0

# __________________________________________________________

""" DataFrame.pop() """

""" Removes a column and returns it """

'''
Syntax
df.pop('column_name')
'''

# import pandas as pd

# df = pd.DataFrame({
#     'Name':['Anil', 'Rahul'],
#     'Age':[20, 22]
# })

# age_col = df.pop('Age')
# print(age_col)
# print(df)

# __________________________________________________
""" DataFrame.xs() (Cross Section) """

''' Extract data at a particular level from Multiindex '''

"""
Syntax
df.xs(key, axis=0, level=None)
"""

# import pandas as pd

# df = pd.DataFrame({
#     'City':['Indore', 'Indore', 'Delhi', 'Delhi'],
#     'Year':[2023, 2024, 2023, 2024],
#     'Sales' : [100, 150, 200, 250]
# })

# df = df.set_index(['City', 'Year'])

# print(df.xs('Indore', level = 'City'))

# ____________________________________________________________

""" DataFrame.get() """

""" Safely get a column (no error if not found) """

"""
Syntax
df.get('column_name', default_value)
"""

# import pandas as pd

# df = pd.DataFrame({
#     'Name': ['Anil', 'Rahul']
# })

# print(df.get('Name'))
# print(df.get('Age', 'Not Found'))

# ____________________________________________________________

""" DataFrame.isin() """

''' Check if values exist in DataFrame 
Returns Boolean DataFrame
 '''
"""
Syntax
df.isin(values)
"""

# import pandas as pd

# df = pd.DataFrame({
#     'Name':['Anil', 'Rahul', 'Priya'],
#     'Age':[20, 22, 21]
# })

# print(df.isin(['Anil', 21]))


# ______________________________________________________

""" DataFrame.where() """

"""
Keeps values where condition is True, replace others
Syntax
df.isin(values)
"""

# import pandas as pd

# df = pd.DataFrame({
#     'Marks':[40, 60, 80]
# })

# print(df.where(df['Marks'] > 50, 'Fail'))

# ________________________________________________________

""" DataFrame.mask() """

''' Oposite of where() '''

''' Replace values where condition is True '''

# import pandas as pd

# df = pd.DataFrame({
#     'Marks':[40, 60, 80]
# })

# print(df.mask(df['Marks'] > 50, 'High'))


# ________________________________________________________

""" DataFrame.insert() """

"""
Insert a column at a specific position
"""

''''
Syntax:

df.insert(loc, column_name, value)
🔹 Parameters
loc → index position
column_name → new column name
value → data
'''
import pandas as pd

df = pd.DataFrame({
    'Name':['Anil', 'Rahul']
})
df.insert(1, 'Age', [20, 22])

print(df)