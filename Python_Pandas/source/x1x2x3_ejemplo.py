import matplotlib.pyplot as plt
import pandas as pd

def Graf_boxplot(dd1 = 0):
  dd.boxplot(column=dd.iloc(1))
  plt.show()

def saca_columnas(dd=0):
  dd1 = dd[['x1','x3']]
  return dd1

def saca_filas(dd=0):
  dd1 = dd.iloc[1]
  return dd1

dd = pd.read_csv('x1x2x3.csv')

dd1 = dd.iloc[,[1]]

print(dd1)






