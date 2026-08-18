import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['text.usetex'] = True 

latex_title = r"$y = \frac{\sin(x)}{x}$"

x = np.linspace(0.001, 10 * np.pi, 400)
y = np.sin(x)/x

plt.plot(x, y)
plt.title(latex_title)
plt.xlabel(r"$\theta$")
plt.show()

