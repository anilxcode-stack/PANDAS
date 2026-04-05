""" transform() method in grouping """

'''
transform() is used when you want to apply a function to each 
group but keep the original DataFrame shape (same number of rows).

also learn from : https://chatgpt.com/c/69ce5aae-47dc-8322-8df6-ec73dcd47e7b
'''

import pandas as pd

data = {
    'Name': ['A', 'B', 'C', 'D', 'E'],
    'Dept' : ['IT', 'IT', 'HR', 'HR', 'IT'],
    'Salary': [50000, 60000, 40000, 45000, 70000]
    
}

df = pd.DataFrame(data)
# print(df)


# _________________________________________________

""" Using agg() (for Comparison)"""
# print(df.groupby('Dept')['Salary'].mean()) # we lost original rows

# _____________________________________________________

""" Using transform() """

# df['Avg_Salary'] = df.groupby('Dept')['Salary'].transform('mean')
# print(df) # Each row gets group average, shape is same as original

# _______________________________________________________

""" Find Salary Difference from Group Mean """

# df['Diff']  = df['Salary'] - df.groupby('Dept')['Salary'].transform('mean')
# print(df)

# ________________________________________________________

""" Normalize Data Group-wise """

df['Normalized'] = df.groupby('Dept')['Salary'].transform(
    lambda x: (x - x.mean()) / x.std()
)
print(df)