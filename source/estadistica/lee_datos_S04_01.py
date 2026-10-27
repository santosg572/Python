import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#import funciones_curso as fun

pat = '../Daniel_Ejercicios_abr2025/c01/'

file = pat+'EXA_C01_S04_01.csv'

datos = pd.read_csv(file)

edad = datos['AGE']

print(edad)

print('longitud edad:', len(edad))

edad = np.array(edad)

print(edad)

