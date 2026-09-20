import numpy as np

#dd = dir(np)

dd = ['ndarray', 'ndim','ones','random', 'linspace']

for ss in dd:
  print('&&&&&&&&&&&&&&&&&&&&&& ' + ss + ' &&&&&&&&&&&&&&&&&&&&&&&&&&&&&')
  print(help(eval('np.'+ss)))


