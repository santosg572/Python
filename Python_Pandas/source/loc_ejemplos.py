import pandas as pd

# Getting values

df = pd.DataFrame([[1, 2], [4, 5], [7, 8]],
                  index=['cobra', 'viper', 'sidewinder'],
                  columns=['max_speed', 'shield'])

print(df)

# Single label. Note this returns the row as a Series.

print(df.loc['viper'])

# List of labels. Note using [[]] returns a DataFrame.

print(df.loc[['viper', 'sidewinder']])

# Single label for row and column

print(df.loc['cobra', 'shield'])

# Slice with labels for row and single label for column. As mentioned above, note that both the start and stop of the slice are included.

print(df.loc['cobra':'viper', 'max_speed'])





