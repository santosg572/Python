import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

import funciones_curso as fun

print(dir(fun))


file = 'EXA_C01_S04_01.csv'

datos = pd.read_csv(file)

edad = datos['AGE']

print(edad)

print('longitud edad:', len(edad))

edad = np.array(edad)

print(edad)

edadU = np.unique(edad)

print(edadU)

frec = []

edadl = list(edad)

for nn in edadU:
  ff = edadl.count(nn)
  frec.append(ff)

print(frec)

print('len frec: ', sum(frec))

frec_relativa = np.array(frec)/sum(frec)

fig, axs = plt.subplots(3, 1, figsize=(8, 6))

print(type(edadU))
print(type(frec))

axs[0].bar(edadU, frec)

axs[1].bar(edadU, frec_relativa)

frec_acum = np.cumsum(frec_relativa)

axs[2].bar(edadU, frec_acum)

edadU = list(edadU)

ix = edadU.index(40)
print(ix)
print(sum(frec_relativa[:(ix+1)]))
print(frec_acum[ix])

plt.show()



