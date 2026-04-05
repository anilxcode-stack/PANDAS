""" Conversion Operation on Series """

import pandas as pd

ser = pd.Series([1, 2, 3, 4])
ser = ser.astype(float)
print(ser)