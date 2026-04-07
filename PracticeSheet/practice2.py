# import pandas as pd

# data = {
#     "Name" : ["Anil", "Rahul", "Priya", "Sita", "Karan"],
#     "Age" : [20, 21, 19, 22, 20],
#     "Marks" : [85, 90, 78, 92, 88]
# }

# df = pd.DataFrame(data)

# # Filtering (stored in res, but doesn't affect df)
# res = df[(df['Marks'] > 85) & (df['Age'] == 20)]

# # Apply Grade logic
# df['Grade'] = df['Marks'].apply(lambda x: "A" if x > 85 else "B")

# # FIX: Use direct mean calculation
# df['Average_Marks'] = df['Marks'].mean()

# print(df)

# ______________________________________________________________________
""" Level 2: Intermediate """

# import pandas as pd
# import numpy as np

# data = {
#     "Name" : ["Anil", "Rahul", "Priya", "Sita", "Karan"],
#     "Marks" : [85, "NA", 92, -1, np.nan],
#     "Attendance" : [90, 85, "?", 88, 92]
# }

# df = pd.DataFrame(data)

# # replace NA and ? with NaN
# df = df.replace(["NA", "?"], np.nan)


# df['Marks'] = df['Marks'].apply(lambda x: np.nan if x < 0 else x)
# df['Marks'] = pd.to_numeric(df["Marks"])

# df['Marks'] = df['Marks'].fillna(df["Marks"].mean())
# df['Attendance'] = df['Attendance'].fillna(df['Attendance'].mean())
# print(df)

# ___________________________________________________________________

"""  Task 5: GroupBy """
# import pandas as pd

# data = {
#     "Department" : ["IT", "IT", "HR", "HR", "Finance"],
#     "Salary" : [50000, 60000, 45000, 48000, 70000]
# }
# df = pd.DataFrame(data)

# res1 = df.groupby('Department')['Salary'].agg('mean')
# # print(res1)

# res2 = df.groupby('Department')['Salary'].agg('max')
# # print(res2)

# res3 = df.sort_values(by="Salary", ascending=False)
# # print(res3)

# df["Rank"] = df["Salary"].apply(lambda x: "1st" if x >=70000 else ( "2nd" if x >= 60000 else ( "3rd" if x >= 50000 else "4th")))

# print(df)

# _____________________________________________________________

# import pandas as pd

# data = {
#     "Name" : ["A", "A", "B", "B", "C"],
#     "Month" : ["Jan", "Feb", "Jan", "Feb", "Jan"],
#     "Sales" : [200, 250, 300, 350, 400]
# }

# df = pd.DataFrame(data)

# res = pd.pivot_table(df, index="Name",
#                      columns="Month",
#                      values="Sales")
# # print(res)

# ________________________________________________________

import pandas as pd

df1 = pd.DataFrame({
    "ID" : [1, 2, 3],
    "Name" : ["Anil", "Rahul", "Priya"]
})

df2 = pd.DataFrame({
    "ID" : [1, 2, 3],
    "Marks" : [85, 90, 75]
})

res1 = pd.merge(df1, df2, how="inner")
# print(res1)

df = pd.merge(df1, df2, how="left")
# print(df)

df['Category'] = df['Marks'].apply(lambda x: "Excellent" if x > 90 else ( "Good" if x >= 80 | x <= 90 else "Average"))
print(df)