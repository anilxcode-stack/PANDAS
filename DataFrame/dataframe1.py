""" Pandas DataFrame """

# import pandas as pd

# df = pd.DataFrame()
# print(df)
# lst = ['Geeks', 'For', 'Geeks', 'is', 'portal', 'for', 'Geeks']

# df = pd.DataFrame(lst)
# print(df)


# _______________________________________________________

#NOTE: Data Sets from Kaggle

import pandas as pd

df = pd.read_csv(r"C:/Users/lenovo/Downloads/archive.zip")
# print(df.head())

# ___________________________________________________________

""" Viewing and Exploring Data """

# print(df.info())

# _________________________________________________________

""" Handling Missing Data """

# print(df.isnull().sum())
# df = df.fillna(0)

# ________________________________________________________

""" Selecting and Filtering Data """

# salary = df[df['salary'] > 100000]
# print(salary)


# ________________________________________________________________

""" Adding and Removing Columns """

# df['total'] = df['experience_years'] + df['salary']
# print(df.head())

# __________________________________________________________

# """ Grouping Data (GroupBy) """

# res = df.groupby('job_title')['experience_years'].sum()
# print(res)




#! ================================ intellipaat ================================


#? Drop the column

# dat = df.drop("skills_count", axis=1)
# print(dat)

#? Shape
# print(df.shape)

#? information about dataframe
# print(df.info())

#? describe()
# print(df.describe())


# ___________________________________________________________

#? Broadcasting 

# df['skills_count'] = df['skills_count'] + 5000
# print(df['skills_count'])

# _______________________________________________________________

#? Renaming columns:

# df.rename(columns= {"skills_count": "Total_Skills"}, inplace = True)

# print(df)

# _________________________________________________________________

# Value count

# print(df['skills_count'].value_counts())

# ____________________________________________________________

# df["Promoted Salary"] = df["salary"] * 10

# print(df)

# _________________________________________________________________
print(df.dropna(how = "any")) # any row that had any null value
print(df.dropna(how = "all")) # if the values in any row are null
