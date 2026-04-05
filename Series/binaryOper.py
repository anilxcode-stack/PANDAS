""" Binary Operations on Pandas """


#! Addition
# import pandas as pd

# ser1 = pd.Series([1, 2, 3], index=['A', 'B', 'C'])
# ser2 = pd.Series([4, 5, 6], index=['A', 'B', 'C'])

# df_sum = ser1.add(ser2)
# print(df_sum)

# __________________________________________________________

#! Subtraction

# import pandas as pd

# ser1 = pd.Series([1, 2, 3], index=['A', 'B', 'C'])
# ser2 = pd.Series([4, 5, 6], index=['A', 'B', 'C'])
# print(ser1.sub(ser2))

# _________________________________________________________

#! Multiplication

# import pandas as pd

# ser1 = pd.Series([1, 2, 3], index=['A', 'B', 'C'])
# ser2 = pd.Series([4, 5, 6], index=['A', 'B', 'C'])
# print(ser1.mul(ser2))

# ____________________________________________________________

#! Division

# import pandas as pd

# ser1 = pd.Series([1, 2, 3], index=['A', 'B', 'C'])
# ser2 = pd.Series([4, 5, 6], index=['A', 'B', 'C'])

# print(ser1.div(ser2))


# ________________________________________________________

#! Power

# import pandas as pd

# ser1 = pd.Series([1, 2, 3], index=['A', 'B', 'C'])
# ser2 = pd.Series([4, 5, 6], index=['A', 'B', 'C'])

# print(ser1.pow(ser2))

# ___________________________________________________________

#! Total Sum

# import pandas as pd

# ser1 = pd.Series([1, 2, 3], index=['A', 'B', 'C'])
# ser2 = pd.Series([4, 5, 6], index=['A', 'B', 'C'])
# print(ser1.sum())
# print(ser2.sum())


# ______________________________________________________

#! prod() -> Product

# import pandas as pd

# ser1 = pd.Series([1, 2, 3], index=['A', 'B', 'C'])
# ser2 = pd.Series([4, 5, 6], index=['A', 'B', 'C'])

# print(ser1.prod())
# print(ser2.prod())


# ______________________________________________________

#! mean() -> Average

# import pandas as pd

# ser1 = pd.Series([1, 2, 3], index=['A', 'B', 'C'])
# ser2 = pd.Series([4, 5, 6], index=['A', 'B', 'C'])

# print(ser1.mean())
# print(ser2.mean())

# ____________________________________________________________

#! abs() -> Absolute Value

# import pandas as pd

# s3 = pd.Series([-10, -20, 30])
# print(s3.abs())

# _______________________________________________________________

#! cov() -> Covariance


# import pandas as pd

# s1 = pd.Series([10, 20, 30], index = [0, 1, 2])
# s2 = pd.Series([1, 2, 3], index = [0, 1, 2])

# print(s1.cov(s2))

# ________________________________________________________________

#! Alignmnet by Index (Not Position)

import pandas as pd

s1 = pd.Series([10, 20, 30], index = ['a', 'b', 'c'])
s2 = pd.Series([1, 2, 3], index = ['b', 'c', 'd'])

print(s1.add(s2))


# __________________________________________________________

#?  Why?
# NOTE: Operations happen based on labels (index)
# Missing labels → NaN