import numpy as np

#dd = dir(np)

dd = ['amax', 'amin', 'angle', 
'append', 'apply_along_axis', 
'argmax', 'argmin',
'around', 'array', 
'c_',
'choose',
'concatenate', 
'copy', 
'corrcoef', 
'cos',
'cumsum', 
'degrees',
'e', 
'exp', 
'fft', 
'fix', 
'fmax', 'fmin', 
'histogram',
'inf',
'infty', 
'isnan',
'log', 'log10',
'max', 
'mean', 'median', 
'min',
'ndim', 'ndindex', 
'ones', 
'pi', 
'quantile',
'radians',
'random',
'remainder',
'reshape',
'round', 
'save', 'savetxt', 
'shape',
'sin', 
'size',
'sort', 
'sqrt', 
'std', 
'sum',
'tan',
'transpose', 
'unique', 
'var', 
'zeros']


#dd = ['ndarray', 'ndim','ones','random', 'linspace']

for ss in dd:
  print('&&&&&&&&&&&&&&&&&&&&&& ' + ss + ' &&&&&&&&&&&&&&&&&&&&&&&&&&&&&')
  print(help(eval('np.'+ss)))


