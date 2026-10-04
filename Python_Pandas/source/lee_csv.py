import matplotlib.pyplot as plt
import pandas as pd

datos = pd.read_csv('datos.csv')


print(datos)

print(datos.describe())

datos.boxplot()

plt.show()


