import numpy as np
import matplotlib.pyplot as plt

mu = 55
sd = 10

x = np.linspace(mu-4*sd, mu+4*sd, 100)

exp = (x - mu)**2/(2*sd**2)

y = np.exp(-1*exp) / np.sqrt(2*np.pi*sd**2)

plt.plot(x,y)
plt.show()


