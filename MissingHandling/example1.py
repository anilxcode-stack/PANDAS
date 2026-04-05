# import pandas as pd
# import numpy as np
# pd.options.future.infer_string = False  # Suppress downcasting warning if needed

# data = {
#     "Marks": [80, "NA", 90, np.nan, 70]
# }

# df = pd.DataFrame(data)
# df1 = df.replace("NA", np.nan).astype(float)  # Force numeric dtype

# df2 = df1.fillna(df1["Marks"].mean())
# df3 = df1.interpolate()  # Now works

# print("\nAfter replace():")
# print(df1)
# print("\nAfter fillna():")
# print(df2)
# print("\nAfter interpolate():")
# print(df3)


# ________________________________________________________________________________________________

# import pandas as pd
# import numpy as np

# # Realistic datasets
# data ={
#     "Name": ["Anil", "Rahul", "Priya", "Sita", "Karan"],
#     "Marks":[85, "NA", 92, -1, np.nan],
#     "Attendance":[90, 85, "?", 88, 92],
#     "City":["Indore", "null", "Bhopal", "Indore", "?"]
# }

# df = pd.DataFrame(data)

# print("Original Data:")
# print(df)
# print("\n")

# # Step 1: Replace wrong values -> NaN
# df.replace(["NA", "null", "?"], np.nan, inplace=True)
# df.replace(-1, np.nan, inplace=True)

# # Step 2: Convert numeric columns properly
# df["Marks"] = pd.to_numeric(df["Marks"], errors='coerce')
# df["Attendance"] = pd.to_numeric(df["Attendance"], errors='coerce')

# # Step 3: Fill missing values
# df["Marks"] = df['Marks'].fillna(df["Marks"].mean())
# df["Attendance"] = df['Attendance'].fillna(df["Attendance"].median())
# df["City"] = df['City'].fillna("Unknown")

# print("Final Cleaned Data: ")
# print(df) 



#! =================================================================

""" Use of inplace() """

''' inplace is used to directly update tue dataframe at condition 
 is true and give copy if condition is false in inplace 
'''

import pandas as pd

data = {
    "Marks" : [80, "NA", 90]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)
print("\n")

# Case 1; Without inplace
df.replace("NA", 0)

print("After replace WITHOUT inplace:")
print(df) # No change
print("\n")

# Case 2: With inplace
df.replace("NA", 0, inplace=True)

print("After replace WITH inplace")
print(df) # Changed

