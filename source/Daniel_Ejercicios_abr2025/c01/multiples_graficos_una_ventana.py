import matplotlib.pyplot as plt
import numpy as np

# Datos de ejemplo
x = np.linspace(-10, 10, 100)
y1 = x
y2 = x**2
y3 = x**3
y4 = x**4

# Crear una figura y una cuadrícula de 2 filas por 2 columnas
fig, axs = plt.subplots(2, 2, figsize=(8, 6))

# Primer gráfico (arriba a la izquierda)
axs[0, 0].plot(x, y1, color='blue')
axs[0, 0].set_title('y = x')

# Segundo gráfico (arriba a la derecha)
axs[0, 1].plot(x, y2, color='red')
axs[0, 1].set_title('y = x²')

# Tercer gráfico (abajo a la izquierda)
axs[1, 0].plot(x, y3, color='green')
axs[1, 0].set_title('y = x³')

# Cuarto gráfico (abajo a la derecha)
axs[1, 1].plot(x, y4, color='purple')
axs[1, 1].set_title('y = x⁴')

# Ajustar automáticamente los espacios entre gráficos
fig.tight_layout()

# Mostrar la ventana
plt.show()


