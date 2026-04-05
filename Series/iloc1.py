""" iloc[] on Series (Position-Based) """

''' Access elements using index position (0-based) '''

import pandas as pd

# s = pd.Series([100, 200, 300])

# print(s.iloc[0])

# ______________________________________________________

# Multiple Positions

# print(s.iloc[[0,2]])

# _________________________________________________________

# Slicing

# print(s.iloc[0:2])

# ________________________________________________________

# Reverse
# print(s.iloc[::-1])

# _____________________________________________________
# print(s.iloc[-1])

# __________________________________________________

# Step Slicing
# print(s.iloc[::2])

# __________________________________________________
# Modify Values

# s.iloc[1] = 55
# print(s)

# ___________________________________________________
# Works Same Even with Custom index

# s2 = pd.Series([100, 200, 300], index = [10, 20, 30])

# print(s2.iloc[1]) # position = 1 -> 200



"""__________________________________________________________________ """

#? Diffference between loc and iloc 

#NOTE: 1). loc is focuses on label suppose if you pass the index
# value explicitly it will conside given index as lablel but 
# by default is takes 0 as index label

# 2). But iloc does't focus on the index that explicitly you passed 
# it only focuses on index from 0 

#? Let's understand with an example

s = pd.Series([100, 202, 30], index=[10, 20, 30])

print(s.loc[10]) # give value of location which is 100
print(s.iloc[0]) # according to index gives 100

# edge case 
print(s.iloc[10]) #! gives an error because 10 is level not index
