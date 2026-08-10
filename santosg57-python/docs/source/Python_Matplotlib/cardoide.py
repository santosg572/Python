import matplotlib.pyplot as plt
import numpy as np

teta = np.arange(0, 2*np.pi, .01)

alfa = 1

r = alfa * (1 + np.cos(teta))

x = r * np.cos(teta)
y = r * np.sin(teta)

plt.plot(x,y)
plt.show()


