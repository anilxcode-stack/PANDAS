
""" Indexing a Series using .loc[]  (Label-Based) """

import pandas as pd

s = pd.Series([10, 20, 30], index = ['a', 'b', 'c'])

# # Labels (index): 'a', 'b', 'c'

# print(s.loc['a'])

# ______________________________________

# #TODO  multpile labels
# print(s.loc[['a', 'c']])

# ________________________________________

#HACK Slicing 

# print(s.loc['a':'c'])

# __________________________________________

# #? Boolean Flitering

# print(s.loc[s > 15])

# ____________________________________________

""" Modifying Values """

# s.loc['b'] = 99
# print(s)

# ___________________________________________

""" Add New Label """

s.loc['d'] = 40
print(s)

# _________________________________________
""" Non-Sequential Lables """

# s2 = pd.Series([100, 200, 300], index=[10, 20, 30])

# s2.loc[20] # label = 20
