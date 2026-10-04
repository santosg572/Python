import pandas as pd

#datos = pd.DataFrame({'nombres':['juan1', 'Juan2']})

dd = dir(pd.DataFrame)

#print(dd)

for ss in dd:
  if not ss[0].isupper():
    if ss[0] != '_':
      print('&&&&&&&&&&&&&&&&&&&&&&&&&&& ' + ss + ' &&&&&&&&&&&&&&&&&&&&&&&&&&&')
      print(help(eval('pd.DataFrame.'+ss)))


 
