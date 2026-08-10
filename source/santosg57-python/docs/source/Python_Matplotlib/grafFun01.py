import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['text.usetex'] = True 

latex_title = r"This is a plot of $y = \sin(x)$"
latex_label = r"$\int_0^1 x^2 dx = \frac{1}{3}$"

x = np.linspace(0, 2 * np.pi, 400)
y = np.sin(x)

plt.plot(x, y)
plt.title(latex_title)
plt.xlabel(r"Angle $\theta$")
plt.ylabel(latex_label)
plt.text(2, 0.8, r"Max value at $x = \frac{\pi}{2}$", fontsize=12)
plt.show()

