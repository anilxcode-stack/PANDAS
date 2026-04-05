""" Column Selection """

# import pandas as pd

# data = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'],
#         'Age':[27, 24, 22, 32],
#         'Address':['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'],
#         'Qualification':['Msc', 'MA', 'MCA', 'Phd']}

# df = pd.DataFrame(data)
# #print(df)

# print(df[['Name', 'Qualification']])

# _________________________________________________

import pandas as pd

data = pd.read_csv("C:/Users/lenovo/Downloads/nba.csv", index_col = "Name")

first = data.loc["Avery Bradley"]
second = data.loc["R.J. Hunter"]

print(first, "\n\n\n", second)