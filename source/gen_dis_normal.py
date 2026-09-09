import random
import numpy as np
import matplotlib.pyplot as plt

pob = list(range(100))

mm = list()

for i in range(1000):
  x = random.sample(pob,10)
  mm.append(int(np.mean(x)))

print(mm)

plt.hist(mm)
plt.show()

