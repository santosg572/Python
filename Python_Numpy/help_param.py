import numpy as np
import sys

param = sys.argv[1]


#dd = dir(np)

#dd = ['abs', 'amax', 'append', 'apply_along_axis', 'apply_over_axes', 'arange', 'around', 'array', 'concatenate', 'cos', 
#'cumsum', 'delete',
#'exp', 'eye', 'fmax', 'histogram', 'histogram2d', 'inf', 'insert', 'linspace', 'log10', 'matrix', 'max', 'mean', 'median', 
#'ones', 'percentile',
#'pi', 'reshape', 'resize', 'round', 'shape', 'sin', 'size', 'sort', 'sqrt', 'sum', 'transpose', 'zeros']

print('======================= ' + param + ' ===============================')

print(help(eval('np.'+param)))
