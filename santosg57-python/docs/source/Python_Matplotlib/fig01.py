import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0, 2*np.pi, .01)

a = 1
b = 1
c = 16

x = np.cos(a*t) + np.cos(b*t)/2 + np.sin(c*t)/3
y = np.sin(a*t) + np.sin(b*t)/2 + np.cos(c*t)/3

aa = np.arange(0, 50)

k = 1
for a in aa:
  x = np.cos(a*t) + np.cos(b*t)/2 + np.sin(c*t)/3
  y = np.sin(a*t) + np.sin(b*t)/2 + np.cos(c*t)/3
  plt.plot(x,y)
  nom = 'file'+str(k)+'.png'
  plt.savefig(nom)
  plt.show()
  plt.close()
  k = k+1

plt.show()


