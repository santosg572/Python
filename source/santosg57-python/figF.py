import matplotlib.pyplot as plt
import numpy as np

def Rota(teta=0):
  mat= np.array([[np.cos(teta), -np.sin(teta)],[np.sin(teta), np.cos(teta)]])
  return mat

t = np.linspace(-3, 3, 100)

x = 7*np.cos(.56*t) * np.sin(0.56*t)/(1+2**(np.cos(2.02*t)**2))

y = 7*np.sin(0.56*t)/(1 + (np.sin(2.02*t))**2)

xy = np.array([x,y])
xy = np.transpose(xy)

nn = xy.shape

xyN = np.zeros(nn)

for i in range(nn[0]):
  xx = xy[i,:]
  xxn = np.dot(Rota(45),xx)
  print(xxn)
  xyN[i,:] = xxn



print(xy.shape)

plt.plot(x,y)
plt.plot(y,x)
plt.plot(xyN[:,0], xyN[:,1])
plt.show()

