""" Creating a Pandas DataFrame """

#** Creating DataFrame using a List

# import pandas as pd

# lst = ['Geeks', 'For', 'Geeks', 'is', 'portal', 'for', 'Geeks']

# df = pd.DataFrame(lst)
# print(df)

# ________________________________________________________

#? Creating DataFrame from dict of ndarray/lists

import pandas as pd

data = {'Name':['Tom', 'nick', 'krish', 'jack'],
        'Age':[20, 21, 19, 18]}

df = pd.DataFrame(data)

print(df)