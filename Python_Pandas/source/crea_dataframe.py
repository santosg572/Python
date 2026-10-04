import pandas as pd
import numpy as np

# Constructing DataFrame from a dictionary.

d = {'col1': [1, 2, 3], 'col2': [3, 4, 5]}

df = pd.DataFrame(data=d)

print(df)

# Notice that the inferred dtype is int64.

print(df.dtypes)

# To enforce a single dtype:

df1 = pd.DataFrame(data=d, dtype=np.int8)

print(df1)
print(df1.dtypes)




