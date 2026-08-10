import matplotlib.pyplot as plt
import numpy as np

def rota(x=0, teta=0):
  rota = np.array([[np.cos(teta), -np.sin(teta)], [np.sin(teta), np.cos(teta)]])
  prod = np.dot(rota,x)
  return prod
 
t = np.arange(-6, 6, .01)

x = 2.5 * (np.sin(-5*t))**2 * 2**(np.cos(np.cos(4.28*2.3*t)))
y = 2.5 * np.sin(np.sin(-5*t)) * (np.cos(4.28*2.3*t))**2

xy = np.array([x, y]).transpose()

nn = xy.shape
print(nn)

rr = xy[0,:]

rrn = rota(rr, np.pi/2)
xyn = np.array([rrn])
print(xyn.shape)

for i in np.arange(1,nn[0]):
  rr = np.array(xy[i,:])
  rrn = rota(rr, np.pi/2)
#  print(rrn.shape)
  xyn = np.append(xyn, [rrn], axis=0)

#  print(rrn)

print(xyn.shape)

plt.plot(x,y)
plt.plot(xyn[:,0], xyn[:,1])

#nom = 'file'+str(k)+'.png'
#plt.savefig(nom)
plt.show()
plt.close()

plt.show()


