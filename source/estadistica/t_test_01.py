# Prueba t de una muestra (ttest_1samp)

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

# Datos de ejemplo

datos = [20.5, 21.0, 19.8, 20.2, 21.5]

media_hipotesis = 20.0

# Realizar la prueba t de una muestra
resultado = stats.ttest_1samp(datos, media_hipotesis)

print(f"Estadístico t: {resultado.statistic:.4f}")

print(f"Valor p (p-value): {resultado.pvalue:.4f}")

fig, ax = plt.subplots(1, 1)
ax.boxplot([datos])
ax.set_xticklabels(["datos"]) 
ax.set_ylabel("mean") 
plt.show()

