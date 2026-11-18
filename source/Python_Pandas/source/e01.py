import pandas as pd
import numpy as np
import random 

nombres = list()
peso = list()

for i in range(10):
  nombres.append('juan'+str(i))
  peso.append(random.randint(50,70))

dd = pd.DataFrame({'nombres':nombres,'peso':peso})

print(dd)

print(dd.loc[3:5])

print(dd.loc['peso'])
