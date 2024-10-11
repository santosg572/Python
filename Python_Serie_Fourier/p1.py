import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0, 10*np.pi, .1)

y1 = np.cos(t/(2*np.pi))

plt.plot(t, y1)

plt.show()

