import numpy as np
import matplotlib.pyplot as plt

a = np.random.randint(12, size=(3,4))

print a

b = a.reshape(12)
print b

ma = b.max()

print ma

print '-----------------'
plt.hist(b, bins=ma-1)  # arguments are passed to np.histogram
plt.title("Histogram with 'auto' bins")
plt.show()



