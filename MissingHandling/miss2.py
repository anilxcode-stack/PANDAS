""" Handling Missing Data - replace method """

"""
Missing values are stored as custom placeholders like "NA", "null", "?", -1, etc.
You want to convert them into proper missing values (NaN) or replace them with meaningful values.
"""

'''
Syntax
df.replace(to_replace, value, inplace=False)
'''

import pandas as pd
import numpy as np

# Setp 1 : Create a sample DataFrame with missing-like values
data = {
    "Name":["Anil", "Rahul", "Priya", "Sita", "Karan"],
    "Marks":[85, "NA", 90, -1, 75],
    "City":["Indore", "null", "Bhopal", "Indore", "?"]
}

df = pd.DataFrame(data)

# print("Original DataFrame:")
# print(df)
# print("\n")


# _______________________________________________________________
""" Replace multiple values at once """

# res = df.replace(['NA', "?"], np.nan)
# print(res)

# _____________________________________________________________
""" Replace using dictionary """

# res1 = df.replace({
#     "Marks" : {"NA": np.nan, -1: np.nan},
#     "City": {"null":"Unknown"}
# }, inplace=True)

# print(res1)

# __________________________________________________________
""" Replace entire column values """

df['City'] = df['City'].replace("Indore", "Mumbai")
print(df)