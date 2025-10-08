import matplotlib.pyplot as plt
import numpy as np

te = np.arange(0, 10*np.pi, .01)

r = np.exp(np.sin(te)) - 2 * np.cos(4*te)  + (np.sin((2*te - np.pi)/24))**5

x = r*np.cos(te)
y = r*np.sin(te)

plt.plot(x,y)
plt.show()



