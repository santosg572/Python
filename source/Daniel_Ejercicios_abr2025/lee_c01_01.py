import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file = 'c01/EXA_C01_S04_01.csv'

datos = pd.read_csv(file)

print(datos.shape)

print(dir(datos))

print(datos.columns)

edad = datos['AGE']

print(type(datos))
print(type(edad))

print('kurtosis: ', edad.kurtosis())
print('media:    ', edad.mean())
print('mediana:    ', edad.median())
print('varianza:    ', edad.var())
print('desviacion estandar:   ', edad.std())

#sns.scatterplot(edad.to_numpy(), x="sujeto", y="EDAD")

plt.figure(figsize=(8, 4))

plt.subplot(1, 2, 1)
plt.plot(edad, 'o')

plt.subplot(1, 2, 2)
plt.boxplot(edad)

plt.show()

