import pandas as pd

datos = pd.DataFrame({'nombres':['juan1', 'Juan2']})

dd = dir(datos)


for ss in dd:
  if ss[0] != '_':
    print('&&&&&&&&&&&&&&&&&&&&&&&&&&& ' + ss + ' &&&&&&&&&&&&&&&&&&&&&&&&&&&')
    print(help(eval('datos.'+ss)))


 
