import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp

file = 'EXA_C01_S04_01.csv'

pat = '../../Desktop/Daniel_Datos_nov1625/ch01_all/'

file =pat+file

fil = open(file,'r')

datos = pd.read_csv(file)

#print(datos.head())

#print(datos)


print(datos.keys())

edad = np.array(datos['AGE'])

print(edad)

print('-------------------------------------------------')
print('minimo: '+ str(np.min(edad)))
print('maximo: '+ str(np.max(edad)))
print('media: '+ str(np.mean(edad)))
print('mediana: '+ str(np.median(edad)))
print('varianza: '+ str(np.var(edad)))
print('desviacion estandard: '+ str(np.std(edad)))
print('kurtosis: '+ str(sp.stats.kurtosis(edad)))
print('-------------------------------------------------')

me = np.mean(edad)
sd = np.std(edad)
np1 = len(edad)

plt.subplot(2,2,1)
plt.plot(edad, 'o')
plt.plot([0,np1], [me, me], linewidth=4)

plt.xlabel("Sujetos")
plt.ylabel("Edad")

plt.subplot(2,2,2)

bins = np.arange(20,91,5)
print(bins)
hh = plt.hist(edad, bins=bins)

print(hh)

cc = hh[0]

print(cc)

ccd = np.cumsum(cc)

print(len(bins))
bins=bins[:len(bins)-1]

print(len(ccd))

plt.subplot(2,2,3)
plt.plot(bins, ccd/ccd[len(ccd)-1])
plt.plot([60,60],[0,.8])

#https://www-geeksforgeeks-org.translate.goog/python/increase-the-thickness-of-a-line-with-matplotlib/?_x_tr_sl=en&_x_tr_tl=es&_x_tr_hl=es&_x_tr_pto=tc


plt.show()



'''
import pandas as pd

# Read a CSV file
df = pd.read_csv('nombre_del_archivo.csv')

# Display the first few rows of the DataFrame
print(df.head())
'''

