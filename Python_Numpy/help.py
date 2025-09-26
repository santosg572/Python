import numpy as np

dd = dir(np)

for ss in dd:
  ss.replace('\n','')
  if ss[0] != '_':
    print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&' + ss + ' &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&')
    print(help(eval('np.'+ss)))

