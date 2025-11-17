import numpy as np
import matplotlib.pyplot as plt


def genera_distribucion_normal(x1=0, x2=0, media=0, des_est=0):
  np1 = 100
  x = np.linspace(x1, x2, np1)  
  mu = media
  de = des_est

  ex = (x - mu)**2/(2 * de**2)
  normal = np.exp(-1 * ex) / (de * np.sqrt(2 * np.pi))

  base = x[1]-x[0]
  area =  base * sum(normal[:np1-1])
  print('area = ' + str(area))
  return (x, normal)

normal = genera_distribucion_normal(30, 80, 55, 7)

x = normal[0]
y = normal[1]
dy = np.cumsum(y)

plt.subplot(2,2,1)
plt.plot(x,y)
plt.title("funcionn de Densidad Normal")
plt.text(30, 0.045, "$\mu = 55$")
plt.text(30, 0.04, "$\sigma = 7$")

plt.text(30, 0.02, r'$\varphi_{\mu ,\sigma^{2}}(x) = \frac{1}{\sigma \sqrt {2\pi}} e^{-\frac {(x-\mu )^{2}}{2\sigma ^{2}}},\quad x\in \mathbb {R}$')


plt.subplot(2,2,2)
plt.plot(x,dy/dy[len(dy)-1])


plt.show()


#https://www.geeksforgeeks.org/python/python-random-sample-function/


