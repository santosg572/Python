import numpy as np
import math
import matplotlib.pyplot as plt

dd =['atan', 'ceil', 'comb', 'cos', 'degrees', 'dist', 'e', 'exp', 'fabs', 'factorial', 'floor', 'fma', 'fmod', 'frexp', 'fsum', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'lcm', 'ldexp', 'log', 'log10', 'modf', 'nan', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sqrt', 'tan', 'tau', 'trunc']

for ss in dd:
  print(help('math.'+ss))


