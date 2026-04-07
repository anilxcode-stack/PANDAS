""" Read Write Excel csv file """

import pandas as pd

# df = pd.read_csv(r"C:\Users\lenovo\Downloads\Book 1(Sheet1).csv")
# print(df)

# _________________________________________________________

""" Skiprows -> Ignore first N rows because they are not actual data """
# df = pd.read_csv(r"C:\Users\lenovo\Downloads\Book 1(Sheet1).csv", skiprows = 2)
# print(df)

# _____________________________________________________________

""" header -> Row Containing column names """

# df = pd.read_csv(r"C:\Users\lenovo\Downloads\Book 1(Sheet1).csv", header=2)
# print(df)

# _____________________________________________________________

""" header = None  """
# if in case the file has no column names then pandas assigns number (0, 1, 2...)
# you override using names

# df = pd.read_csv(r"C:\Users\lenovo\Downloads\Book 1(Sheet1).csv", header=None)
# print(df)

""" header = None + names """
''' Also add specific column names '''
# df = pd.read_csv(r"C:\Users\lenovo\Downloads\Book 1(Sheet1).csv", header=None, names=["A", "B", "C"])
# print(df)

# ________________________________________________________________________

""" nrows -> Load only first N rows to save memory and time """

# df = pd.read_csv(r"C:\Users\lenovo\Downloads\Book 1(Sheet1).csv", nrows=1)
# print(df)

# __________________________________________________________________

""" np_values -> maps custom values → NaN """

# df = pd.read_csv(r"C:\Users\lenovo\Downloads\Book 1(Sheet1).csv", na_values={"Salary": ["n.a."]})
# print(df)

# __________________________________________________________________

""" sep -> Comma Separated Values """

# df = pd.read_csv(r"C:\Users\lenovo\Downloads\Book 1(Sheet1).csv", sep="|")
# print(df)

#____________________________________________________________________

""" usecols -> Instead of loading full dataset Load only required columns  """

# df = pd.read_csv(r"C:\Users\lenovo\Downloads\Book 1(Sheet1).csv", usecols=["Name", "Salary"])
# print(df)


# ______________________________________________________________________

""" dtype -> Correct data type """

# df = pd.read_csv(r"C:\Users\lenovo\Downloads\Book 1(Sheet1).csv", dtype={"Age": int})
# print(df)

# ____________________________________________________________

""" parse_dates -> Dates are read as strings by default """
''' It works only if your CSV has a column named exactly:

Date '''

# df = pd.read_csv(r"C:\Users\lenovo\Downloads\Book 1(Sheet1).csv", parse_dates=["Date"])
# print(df)

# ____________________________________________________________________

# df.to_csv("C:\Users\lenovo\Downloads\Book 1(Sheet1).csv")


