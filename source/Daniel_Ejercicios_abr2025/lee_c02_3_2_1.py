import pandas as pd
import matplotlib.pyplot as plt

file = 'c02/EXR_C02_S03_01.csv'

datos = pd.read_csv(file)

print(datos)
print(datos.shape)
print(type(datos.shape))

plt.figure(figsize=(8, 4))

plt.subplot(1, 2, 1)
plt.plot(datos, 'o')

plt.subplot(1, 2, 2)
plt.boxplot(datos)

plt.show()

