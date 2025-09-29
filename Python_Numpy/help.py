import numpy as np

#dd = dir(np)

dd = ['abs', 'amax', 'append', 'apply_along_axis', 'apply_over_axes', 'arange', 'around', 'array', 'concatenate', 'cos', 
'cumsum', 'delete',
'exp', 'eye', 'fmax', 'histogram', 'histogram2d', 'inf', 'insert', 'linspace', 'log10', 'matrix', 'max', 'mean', 'median', 
'ones', 'percentile',
'pi', 'reshape', 'resize', 'round', 'shape', 'sin', 'size', 'sort', 'sqrt', 'sum', 'transpose', 'zeros']

for ss in dd:
  ss.replace('\n','')
  if ss[0] != '_':
    print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&' + ss + ' &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&')
    print(help(eval('np.'+ss)))

