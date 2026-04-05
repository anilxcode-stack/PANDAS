""" Basic GroupBy (No Aggregation) """

# import pandas as pd

# data = {
#     'Name' : ['A', 'B', 'C', 'D'],
#     'Team' : ['X', 'X', 'Y', "y"],
#     'Salary' : [100, 200, 300, 400]
# }

# df = pd.DataFrame(data)

# grouped = df.groupby('Team')
# print(grouped)

# _____________________________________________________________

""" Simple Aggregation (Single Function) """

# import pandas as pd

# df = pd.DataFrame({
#     'Team': ['X', 'X', 'Y', 'Y'],
#     'Salary' : [100, 200, 300, 400]
# })

# result = df.groupby('Team')['Salary'].sum()
# print(result)


# ________________________________________________________

""" Multiple Aggregations """

# import pandas as pd

# df = pd.DataFrame({
#     'Team': ['X', 'X', 'Y', 'Y'],
#     'Salary':[100, 200, 300, 400]

# })

# result = df.groupby('Team')['Salary'].agg(['sum', 'mean', 'max'])
# print(result)


# ____________________________________________________________

""" Named Aggregation (Important) """

# import pandas as pd

# df = pd.DataFrame({
#     'Name': ['A', 'B', 'C', 'D'],
#     'Team': ['X', 'X', 'Y', 'Y'],
#     'Salary' : [100, 200, 300, 400]
# })

#result = df.groupby('Team').agg(
#     total_salary = ('Salary', sum),
#     avg_salary=('Salary', 'mean'),
#     player_count = ('Name', 'count')
# )

# print(result)

# __________________________________________________________

""" Multi-Level Grouping """

# import pandas as pd

## df = pd.DataFrame({
#     'Name' : ['A', 'B', 'C', 'D'],
#     'Team': ['X', 'X', 'Y', 'Y'],
#     'Position':['PG', 'SG', 'PG', 'SG'],
#     'Salary' : [100, 200, 300, 400]
# }) 

# result = df.groupby(['Team', 'Position']).sum()
# print(result)

# ____________________________________________________

""" Reset Index (Convert to Normal Table) """

# import pandas as pd

# df = pd.DataFrame({
#     'Name' : ['A', 'B', 'C', 'D'],
#     'Team': ['X', 'X', 'Y', 'Y'],
#     'Position':['PG', 'SG', 'PG', 'SG'],
#     'Salary' : [100, 200, 300, 400]
# }) 

# result = df.groupby(['Team', 'Position']).sum().reset_index()
# print(result)

# _________________________________________________________________
""" Transform (Same Size Output) """

# import pandas as pd

# df = pd.DataFrame({
#     'Team':['X', 'X', 'Y', 'Y'],
#     'Salary' : [100, 200, 300, 400]
# })

# df['avg_salary'] = df.groupby('Team')['Salary'].transform('mean')

# print(df)

# ______________________________________________________________

""" Apply (Custom Function) """

# import pandas as pd

# df = pd.DataFrame({
#     'Team':['X', 'X', 'Y', 'Y'],
#     'Salary':[100, 200, 300, 400]
# })

# result = df.groupby('Team').apply(lambda x: x.head(1))
# print(result)


# ____________________________________________________________________________

""" Filter Groups """

import pandas as pd

df = pd.DataFrame({
    'Team' : ['X', 'X', 'Y', 'Y'],
    'Salary' : [100, 200, 300, 400]
})

result = df.groupby('Team').filter(lambda x: x['Salary'].mean() > 150)
print(result)