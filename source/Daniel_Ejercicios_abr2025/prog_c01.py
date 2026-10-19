import pandas as pd
import numpy as np

pat='c01/'

file = pat+'EXA_C01_S04_01.csv'

datos = pd.read_csv(file)

edad = datos['AGE']

edad = np.array(edad)

muestras_medias = []

for i in range(20):
  muestra = np.random.choice(edad, size=10, replace=True)
  muestras_medias.append(np.mean(muestra))

print(muestras_medias)






