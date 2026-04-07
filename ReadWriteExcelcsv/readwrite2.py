""" Read Write in DataFame """

import pandas as pd

data = {
    "Name" : ["Anil", "Rahul", "Priya", "Sneha"],
    "Age" : [20, 21, 19, 22],
    "Salary" : [50000, None, 45000, None]
}

df = pd.DataFrame(data)
# res = df.to_csv("employees.csv")
# print(res)

# _____________________________________________________________

""" index=False -> if you does't want to index in file """
# df.to_csv("employees_no_index.csv", index=False)

# _____________________________________________________________

""" columns -> to obtain columns that you want to access """

# df.to_csv("selected_columns.csv", columns=["Name", "Salary"], index=False)

# _____________________________________________________________

# """ header=False -> without header """
# df.to_csv("no_header.csv", header=False, index=False)

# ______________________________________________________________

""" sep -> seperation between files """

# df.to_csv("pipe_format.csv", sep="|", index=False)

# ____________________________________________________________

""" na_rep  -> Replace NaN with readable value  """

# df.to_csv("no_nan.csv", na_rep="Missing", index=False)

# _____________________________________________________________

""" mode="a" -> Add data instead of overwriting  """

# df.to_csv("output.csv", mode="a", header=False)

# ____________________________________________________________

