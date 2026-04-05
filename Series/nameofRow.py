""" give the name of the column """

# import pandas as pd

# fruit_protien = {
#     "Avocado": 2.0, # grams of protein
#     "Guava":2.6,
#    "Blackberries": 2.0,
#     "Oranges": 0.9,
#     "Banana": 1.1,
#     "Apples": 0.3,
#     "Kiwi": 1.1,
#     "Pomegranate": 1.7,
#     "Mango": 0.8,
#     "Cherries": 1.0
# }

# s2 = pd.Series(fruit_protien, name = "Protein")
# print(s2)


# _____________________________________________

# Conditional Selection

# print(s2[s2>1])

# ____________________________________________

# Logical Operators: and, or, not

# print(s2[(s2>0.5) | (s2 <= 2)])

# ___________________________________________

# not operation:

# print(~(s2>1))

# ___________________________________________

""" Modifying the series: """

# s2['Mango'] = 2.8

# print(s2)


# _________________________________________________

import pandas as pd
import numpy as np

ser = pd.Series(['a', np.nan, 1, np.nan, 2])
print(ser.notnull().sum())