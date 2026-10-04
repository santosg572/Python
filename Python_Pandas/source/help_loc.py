import pandas as pd

x = [1,2,3,4,5]
y = [6,7,8,9,10]
z = range(100,105)

dd = pd.DataFrame({'x':x,'y':y})

print(help(dd.loc))



