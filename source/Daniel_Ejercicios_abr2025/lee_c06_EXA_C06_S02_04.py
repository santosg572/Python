import numpy as np
from scipy import stats
import pandas as pd
import matplotlib.pyplot as plt

file = 'c06/EXA_C06_S02_04.csv'

datos = pd.read_csv(file)

print(datos)

print(len(datos))

sigma = np.sqrt(.36)


error_estandar_z = sigma / (n ** 0.5)

ic_z = stats.norm.interval(confidence=0.95, loc=media, scale=error_estandar_z)

