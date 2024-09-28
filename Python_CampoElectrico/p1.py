import numpy as np
import math

q = np.array([2,-5])
px = np.array([0, 2])
py = np.array([1, 0])

Q = -3
pq = (0,0)

k = 8.99 * 10**9
dx = 2*10**(-7)
qq = 1.602 * 10**(-19)

xt = 0
yt = 0
for i in range(2):
 x = dx*(pq[0] - px[i])
 y = dx*(pq[1] - py[i])
 r = x*x + y*y
 teta = math.atan(y/x)
 xt = xt + qq*qq*q[i]*Q*math.cos(teta) / r
 yt = yt + qq*qq*q[i]*Q * math.sin(teta) / r


xt = k*xt
yt = k*yt


print(xt, yt)
