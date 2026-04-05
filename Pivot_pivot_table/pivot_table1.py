""" Piivot Table in Pandas """

# import packages
import pandas as pd

# create data
df = pd.DataFrame({'ID': {0: 23, 1: 43, 2: 12, 
                          3: 13, 4: 67, 5: 89,
                          6: 90, 7: 56, 8: 34},
                   
                 'Name': {0: 'Ram', 1: 'Deep', 2: 'Yash',
                          3: 'Aman', 4: 'Arjun', 5: 'Aditya',
                          6: 'Akash', 7: 'Chalsea',
                          8: 'Divya'},
                   
                 'Marks': {0: 89, 1: 97, 2: 45,
                           3: 78, 4: 56, 5: 76,
                           6: 81, 7: 87, 8: 100},
                   
                 'Grade': {0: 'B', 1: 'A', 2: 'F',
                           3: 'C', 4: 'E', 5: 'C',
                           6: 'B', 7: 'B', 8: 'A'}})

# Ex1: Average markks per Grade

pivot1 = pd.pivot_table(df, 
                        index = 'Grade',
                        values='Marks',
                        aggfunc='mean')

# print("Average Marks per Grade:\n", pivot1)

# Ex2: Count of students per Grade

pivot2 = pd.pivot_table(df,
                        index='Grade',
                        values='Marks',
                        aggfunc='count')

# print("\nCount of Students per Grade:\n", pivot2)

# Ex 3: Multiple aggregations
pivot3 = pd.pivot_table(df,
                        index='Grade',
                        values='Marks',
                        aggfunc=['mean', 'max', 'min'])

# print("\nMultiple Aggregation:\n", pivot3)

# Ex 4: Pivot with columns (real pivoting)

pivot4 = pd.pivot_table(df,
                        index='Grade',
                        columns='Name',
                        values='Marks')
# print("\nPivot with Grade vs name:\n", pivot4)

# Ex 5: Fill missing values

pivot5 = pd.pivot_table(df,
                        index='Grade',
                        columns='Name',
                        values='Marks',
                        fill_value=0)
print("\nPivot with Missing Values filled:\n", pivot5)