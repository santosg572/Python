import pandas as pd

# selection by position

mydict = [{'a': 1, 'b': 2, 'c': 3, 'd': 4},
          {'a': 100, 'b': 200, 'c': 300, 'd': 400},
          {'a': 1000, 'b': 2000, 'c': 3000, 'd': 4000}]
df = pd.DataFrame(mydict)
df

# Indexing just the rows

# With a scalar integer.

print(type(df.iloc[0]))

print(df.iloc[0])

# With a list of integers.

print(df.iloc[[0]])

print(type(df.iloc[[0]]))

# With a slice object.




