""" Creating Pandas DataFrame from Lists """

#HACK Using Dictionary of Lists

# import pandas as pd

# names = ["Aparna", "Pankaj", "Sudhir", "Garvit"]
# degrees = ["MBA", "BCA", "MTech", "MBA"]
# scores = [90, 40, 80, 98]

# df = pd.DataFrame({'Name':names, 'Degree':degrees, 'Score':scores})
# print(df)

# ______________________________________________________

#HACK Using zip() Function

# import pandas as pd

# names = ["Aparna", "Pamkaj", "Sudhir", "Geeku"]
# values = [11, 22, 33, 44]
# df = pd.DataFrame(list(zip(names, values)), columns=['Name', 'Value'])
# print(df)

# ___________________________________________________

#* Using Multi-Dimensional List

# import pandas as pd

# data = [['Tom', 25], ['Krish', 30], ['Nick', 26], ['Juli', 22]]
# df = pd.DataFrame(data, columns=['Name', 'Age'])
# print(df)

# ________________________________________________________________

""" Creating Data Type After Creating DataFrame """

# import pandas as pd

# data = [['Tom', 'Reacher', 25], ['Krish', 'Pete', 30], ['Nick', 'Wilson', 26], ['Juli', 'Williams', 22]]
# df = pd.DataFrame(data, columns=['FName', 'LName', 'Age'])
# df['Age'] = df['Age'].astype(float)
# print(df)

# ________________________________________________________________

""" Using index and Column Names """

# import pandas as pd

# data = ["Aparna", "Pankaj", "Sudhir", "Gravit"]
# df = pd.DataFrame(data, index=['a', 'b', 'c', 'd'], columns=['Names'])
# print(df)

# ______________________________________________________________

import pandas as pd
data = [1, 2, 3, 4, 5]
df = pd.DataFrame(data, columns=['Numbers'])
print(df)