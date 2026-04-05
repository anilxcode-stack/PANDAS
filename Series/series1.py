""" Creating Series in Pandas """

import pandas as pd

# data = [1, 2, 3, 4]

# ser = pd.Series(data)
# print(ser)

#! ____________________________________________________

#? Creating an Empty Pandas Series

# ser = pd.Series()

# print(ser)

#! ____________________________________________________

#? Creating a Series from a NumPy Array

# import numpy as np

# data = np.array(['g', 'e', 'e', 'k', 's'])

# ser = pd.Series(data)
# print(ser)

#! _______________________________________________________

#? Creating a Series from a List

# data_list = ['g', 'e', 'e', 'k', 's']

# ser = pd.Series(data_list)
# print(ser)

#! _______________________________________________________

#? Creating a Series from a Dictionary

# data_dict = {'Geeks':10, 'for':20, 'geeks':30}

# ser = pd.Series(data_dict)
# print(ser)

#! ________________________________________________________

#? Creating a Series Using NumPy Functions

# import numpy as np

# ser = pd.Series(np.linspace(1, 10, 5))
# print(ser)

#! ________________________________________________________

#? Creating a Series Using range()

# ser = pd.Series(range(5, 15))
# print(ser)

#! ___________________________________________________________

#? Creating a Series Using a List

ser = pd.Series(range(1, 20, 3), index = [x for x in 'abcdefg'])
print(ser)