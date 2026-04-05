""" Indexing Data using the [] Operator """

""" Selecting a Single Column """

import pandas as pd

data = pd.read_csv("C:/Users/lenovo/Downloads/nba (1).csv", index_col="Name")
print("Dataset")

# print(data.head(5))

# first = data["Age"]
# print("\nSingle Column selected from Dataset")
# print(first.head(5))

# ______________________________________________________

""" Selecting Multiple Columns """

# first = data[["Age", "College", "Salary"]]
# print("\nNultiple Columns selected from Dataset")
# print(first.head(5))

# _______________________________________________________
""" Selecting a Single Row by Label """

# row = data.loc["Avery Bradley"]
# print(row)

#_________________________________________________________

""" Selecting Multiple Rows by Label """
# rows = data.loc[["Avery Bradley", "R.J. Hunter"]]
# print(rows)

# __________________________________________________________

""" Selecting Specific Rows and Columns """

''' 
Dataframe.loc[["row1", "row2"], ["column1", "column2", "column3"]]
'''
# selection = data.loc[["Avery Bradley", "R.J. Hunter"], ["Team", "Number", "Position"]]

# print(selection)

# __________________________________________________________

""" Selecting All Rows and Specific Columns """

# ''' Dataframe.loc[:, ["column1", "column2", "column3"]] '''
# all_rows_specific_columns = data.loc[:, ["Team", "Position", "Salary"]]
# print(all_rows_specific_columns)

#! ===============================================================

""" Indexing with .iloc[] """

""" Selecting a Single Row by Position """

# row = data.iloc[3]
# print(row)

# _________________________________________________________________
""" Selecting Multiple Rows by Position """

# rows = data.iloc[[3, 5, 7]]
# print(rows)

# ______________________________________________________________-_

""" Selecting Specific Rows and Columns by Position """

# selection = data.iloc[[3, 4], [1, 2]]
# print(selection)

# ______________________________________________________________

""" Selecting All Rows and Specific Columns by position """

# selection = data.iloc[:, [1, 2]]
# print(selection)

# __________________________________________________________
""" Other Useful Indexing Methods """

''' .head(): Returns the first n rows of a DataFrames '''
# print(data.head(5))

# _____________________________________________________

""" .tail(): Returns the last n rows of a DataFrame """
# print(data.tail(5))


# __________________________________________________________
""" .at[]: Access a single value for a row/column label pair """

# value = data.at["Avery Bradley", "Age"]
# print(value)

# ____________________________________________________________

""" .query(): Query the DataFrame using a boolean expression """

result = data.query("Age > 25 and College == 'Duke'")
print(result)