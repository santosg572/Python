import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0, np.pi*4, .01)
y1 = np.sin(t)
y2 = 2*y1

pas = np.arange(100)

for tt in pas:
  plt.plot(t, y1+tt)

plt.show()


