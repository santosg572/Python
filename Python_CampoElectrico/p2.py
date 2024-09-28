import numpy as np
import math

k = 8.99 * 10**9
dx = 2*10**(-7)
culomb = 1.602 * 10**(-19)

def Fuerza(q1,p1, q2, p2):
 k = 8.99 * 10**9
 r2 = math.dist(p1, p2)
 qt = q1*q2
 if p1[0] == p2[0]:
  v = [1,0]
 elif p1[1] == p2[1]:
  v = [0,1]
 else:
  teta = math.atan((p2[1]-p1[1])/(p2[0]-p1[0]))
  v = [math.cos(teta), math.sin(teta)]
 
 v.append(qt*k/r2)
 return v

q1 = 1
p1 = [5.29*10**(-11),0]
q2 = 1
p2 = [0,0]

ff = Fuerza(q1, p1, q2, p2)

print(ff)

