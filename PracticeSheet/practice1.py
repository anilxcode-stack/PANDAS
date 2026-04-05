""" Practice sheet """

import pandas as pd
import numpy as np

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Alice'],
    'Age' : [25, 30, 35, np.nan, 29, 25],
    'Dept' : ['HR', 'IT', 'Finance', 'IT', 'HR', 'HR'],
    'Salary' : [55000, 65000, 75000, 67000, np.nan, 55000],
    'Promoted Salary' : [550000, 650000, 750000, 670000, np.nan, 550000]
}

df = pd.DataFrame(data)
# print(df)

# print(df.isnull().sum()) # to check how many non values in a row

# __________________________________________________________________

result = df.dropna(how='any') # any row that had any null value
# print(result)

result2 = df.dropna(how = "all") # if all the values in any row are null then we drop that row

# print(result2)

# ____________________________________________________
result3 = df['Age'].fillna(df['Age'].mean())
# print(result3)

# ___________________________________________________________
result4 = df['Salary'].fillna(df['Salary'].median())
# print(result4)

# _________________________________________________________

df["Name"] = df["Name"].replace("Charlie", "Rose")
# print(df)

# ______________________________________________________

# Duplicates:

df_dup = df[df.duplicated(keep = "last")]
print(df_dup)