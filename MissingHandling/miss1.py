""" Handling Missing Data - fillna, interploate , dropna """

""" fillna() -> used to replace NaN(missing values) with a specific value or method """
"""
✔️ Syntax
df.fillna(value, inplace=False)
"""

# import pandas as pd
# import numpy as np

# data = {
#     'Name':['Aman', 'Riya', 'Raj', 'Neha'],
#     'Marks': [80, np.nan, 75, np.nan]
# }

# df = pd.DataFrame(data)

# Fill missing values with 0
# df['Marks'] = df['Marks'].fillna(0)
# _______________________________________________________________


# Other Uses
# res1 = df.fillna(df['Marks'].mean())  # Fill with average
# print(res1)

#_________________________________________________________________

# res2 = df.fillna(method='ffill') # forward fill
# print(res2)
# __________________________________________________________________


# Proper example

# import pandas as pd
# import numpy as np

# data = {
#     'Name': ['Aman', 'Riya', 'Raj', 'Neha'],
#     'Marks': [80, np.nan, 75, np.nan]
# }

# df = pd.DataFrame(data)

# # Apply backward fill
# res4 = df.bfill()

# print(res4)

# _____________________________________________________________________

# import pandas as pd
# import numpy as np

# data = {
#     'Name': ['Aman', 'Riya', 'Raj', 'Neha'],
#     'Marks': [80, np.nan, 75, np.nan]
# }

# df = pd.DataFrame(data)

# # Correct way (Pandas 2.x+)
# res4 = df.ffill()  # Forward fill

# print(res4)


#! ==============================================================

""" interpolate() - Fill with estimated values """

'''
interpolate() fills missing values using mathematical estimation
(linear interploation) based on surrounding values.

✔️ Syntax
df.interpolate(method='linear')

'''
# import pandas as pd
# import numpy as np

# data = {
#     'Marks' : [70, np.nan, np.nan, 100]
# }

# df = pd.DataFrame(data)

# df['Marks'] = df['Marks'].interpolate()

# print(df)

"""
Missing values are filled based on trend between 70 → 100
So values become: 80, 90

"""

#! ====================================================================

""" dropna() - Remove Missing Values """

""" dropna is used to delete rows or columns that contain NaN values """

"""
✔️ Syntax
df.dropna(axis=0, inpla
"""

# import pandas as pd
# import numpy as np

# data = {
#     'Name' : ['Aman', 'Riya', 'Raj', 'Neha'],
#     'Marks':[80, np.nan, 75, np.nan]
# }

# df = pd.DataFrame(data)

# # Drop rows with missing values
# df = df.dropna()

# print(df)

# _____________________________________________________________

import pandas as pd
import numpy as np

data = {
    'Name': ['Aman', 'Riya', 'Raj', 'Neha'],
    'Age' : [25, np.nan, 22, np.nan],
    'Marks': [80, np.nan, 75, np.nan],
    'City':[np.nan, np.nan, np.nan, np.nan]
}

df = pd.DataFrame(data)
# print(df)

df1 = df.dropna(axis=1) # Drop columns that contain ANY NaN value
# print(df1)

df2 = df.dropna(how='all') # Drop rows where All values are NaN
# print(df2)

df3 = df.dropna(thresh=2) # Keep row with at least 2 NON-NaN values
print(df3)