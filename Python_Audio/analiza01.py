import scipy.io.wavfile as wavfile
import numpy as np
import matplotlib.pyplot as plt

sample_rate, data = wavfile.read("output.wav")

print(sample_rate)

print(data.shape)

x = data[:,0]
print(x.shape)
nx = len(x)
print(nx)

tiempo = len(x)/sample_rate

print(tiempo)

print('minimo, maximo')

min_amplitude = np.min(x)
max_amplitude = np.max(x)


print(min_amplitude, max_amplitude)

plt.plot(x)
plt.show()





