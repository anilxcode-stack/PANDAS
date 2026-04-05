""" Pandas Concatenate DataFrames """

# import pandas as pd

# india_weather = pd.DataFrame({
#     "city" : ["mumbai", "delhi", "banglore"],
#     "temperature" : [32, 45, 30],
#     "humidity" : [80, 60, 78]
# })

# us_weather = pd.DataFrame({
#     "city" : ["new york", "chicago", "orlando"],
#     "temperature":[21, 14, 35],
#     "humidity" : [68, 65, 75]
# })

# df = pd.concat([india_weather, us_weather])

# ______________________________________________________________
""" Ignore Index """

# df = pd.concat([india_weather, us_weather], ignore_index=True)

# print(df)

# _________________________________________________________

""" Concatenation And Keys """
# df = pd.concat([india_weather, us_weather], keys = ["india", "us"])
# print(df)

# print(df.loc["us"])
# print(df.loc["india"])

# _________________________________________________________________

""" Concatenation Using Index """

# temperature_df = pd.DataFrame({
#     "city" : ["mumbai", "delhi", "banglore"],
#     "temperature" : [32, 45, 30]
# }, index=[0, 1, 2])
# print(temperature_df)

# windspeed_df = pd.DataFrame({
#     "city" : ["delhi", "mumbai"],
#     "windspeed" : [7, 12]
# }, index=[1, 0])

# df = pd.concat([temperature_df, windspeed_df], axis = 1)
# print(df)

# __________________________________________________________________

""" Concatenate dataframe with series """

import pandas as pd

temperature_df = pd.DataFrame({
    "city" : ["mumbai", "delhi", "banglore"],
    "temperture" : [32, 45, 30]
}, index=[0, 1, 2])
print(temperature_df)

s = pd.Series(["Humid", "Dry", "Rain"], name = "event")

df = pd.concat([temperature_df, s], axis = 1)
print(df)