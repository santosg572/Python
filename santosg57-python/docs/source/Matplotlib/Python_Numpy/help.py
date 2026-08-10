import numpy as np

dd = dir(np)

for d in dd:
  if  not( d[0] == '_'):
    print('=========================== ' + d + ' ===========================')
    help(eval('np.'+d))



