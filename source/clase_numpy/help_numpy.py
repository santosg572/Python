import numpy as np

dd = dir(np)

for ss in dd:
  ss1 = ss[0]
  if not ss1.isupper():
    if not (ss1[0] == '_'):
      print('&&&&&&&&&&&&&&&&&&&&&& ' + ss )
      print(help(eval('np.'+ss)))


