import pandas as pd

dd = dir(pd.DataFrame)

for ss in dd:
  if not ss[0].isupper():
    if ss[0] != '_':
      print('&&&&&&&&&&&&&&&&&&&&&&&&&&& ' + ss + ' &&&&&&&&&&&&&&&&&&&&&&&&&&&')
      print(help(eval('pd.DataFrame.'+ss)))


 
