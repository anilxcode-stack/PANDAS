""" Pivot funcion in Pandas """

"""
Pivot = Data reshaping technique
In real data:

Data is stored in rows (repeated values)
But for analysis, we want:
One row per entity
Multiple columns for categories

👉 Pivot helps in:

Data analysis
Report generation
Machine learning preprocessing

"""

# Example 

# import pandas as pd

# df = pd.DataFrame({
#     "Name" : ["Anil", "Anil", "Rahul", "Rahul"],
#     "Subject" : ["Math", "Sci","Math", "Sci"],
#     "Marks" : [80, 85, 70, 75]
# })

# pivot_df = df.pivot(index="Name", columns="Subject", values="Marks")
# print(pivot_df)

# _____________________________________________
""" pivot()  Only works when data is unique """

# import pandas as pd

# df = pd.DataFrame({
#     "Name" : ["Anil", "Anil"],
#     "Subject" : ["Math", "Math"],
#     "Marks" : [80, 90]
# })

# df = df.pivot(index="Name", columns="Subject", values="Marks")
# print(df)  #! gives Error reshaping cannot be happen

''' Same (Name, Subject) pair appears twice
👉 Pivot doesn't know which value to pick'''

# ___________________________________________________________

