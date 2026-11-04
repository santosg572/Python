BIOSTATISTICS-DANIEL
====================

* Vaviarbles Cualitativas
* Variable Cuantitativas
* Variables Aleatorias
* Variables Aleatorias Discretas
* Variables Aleatorias Continuas
* Población
* Muestra

**Escalas de Medición**

* Escala Nominal
* Escala Ordinal
* La escala de intervalos
* La escala de razón

**Muestreo**

.. code:: Bash

   48, 35, 46, 44, 43, 42, 39, 44, 49, 49, 44, 39, 38, 49, 49, 53, 56, 57, 51, 61, 53, 66, 71, 75, 72, 65, 67, 38, 37, 46, 44, 44, 48, 49, 30, 45, 47, 45, 48, 47, 47, 44, 48, 43, 45, 40, 48, 49, 38, 44, 43, 47, 46, 57, 52, 54, 56, 53, 64, 53, 58, 54, 59, 56, 62, 50, 64, 53, 61, 53, 62, 57, 52, 54, 61, 59, 57, 52, 54, 53, 62, 52, 62, 57, 59, 59, 56, 57, 53, 59, 61, 55, 61, 56, 52, 54, 51, 50, 50, 55, 63, 50, 59, 54, 60, 50, 56, 68, 66, 71, 82, 68, 78, 66, 70, 66, 78, 69, 71, 69, 78, 66, 68, 71, 69, 77, 76, 71, 43, 47, 48, 37, 40, 42, 38, 49, 43, 46, 34, 46, 46, 48, 47, 43, 52, 53, 61, 60, 53, 53, 50, 53, 54, 61, 61, 61, 64, 53, 53, 54, 61, 60, 51, 50, 53, 64, 64, 53, 60, 54, 55, 58, 62, 62, 54, 53, 61, 54, 51, 62, 57, 50, 64, 63, 65, 71, 71, 73, 66

**Ejemplo**

.. code:: Python

   import numpy as np

   elementos = ['A', 'B', 'C', 'D', 'E']

   muestra_np = np.random.choice(elementos, size=3, replace=True)

   print(muestra_np)  # Ejemplo de salida: ['C', 'E', 'C']


**C02. Estadística Descriptiva**

**Ordenar**

.. code:: Python

    import numpy as np
    x=np.array([3,4,5,2,3,7,4])
    print(x)
    x.sort()
    print(x) 

    mx = x.mean()
    sx = x.std()
    vx = x.var()
    x1 = x.min()
    x1 = x.max()

**Ejemplo**

.. code:: Python

   import numpy as np

   x =
   print(x)

   bin = np.linspace(30,90,7)

   print(bin)

   h = np.digitize(x, bin)

   print(h)

   his = np.bincount(h)

   print(his)

**tabla de frecuencias, frecuencias acumulativa, frecuencia relativa y frecuencia relativa acumulatica**

**Poligono de frecuencias**

**Simetría de una Distribución de Frecuencias**

**C03. Algunos Conceptos de Probabilidad**

**C04. Distribuciones de Probabilidad**

* Binomial

**Ejemplo 1**

.. code:: Python

   from scipy.stats import binom

   # Parámetros: n = 10 ensayos, p = 0.5 (ej. lanzar una moneda 10 veces)
   n = 10
   p = 0.5

   # 1. Probabilidad de obtener exactamente k = 6 éxitos (PMF)
   prob_exacta = binom.pmf(k=6, n=n, p=p)
   print(f"Probabilidad de exactamente 6 éxitos: {prob_exacta:.4f}")

   # 2. Probabilidad de obtener 6 o menos éxitos (CDF)
   prob_acumulada = binom.cdf(k=6, n=n, p=p)
   print(f"Probabilidad de 6 o menos éxitos: {prob_acumulada:.4f}")
         
**Ejemplo 2**

.. code:: Python

   import numpy as np

   # Simular 1000 experimentos donde se lanza una moneda 10 veces (n=10, p=0.5)
   muestras = np.random.binomial(n=10, p=0.5, size=1000)

   print("Primeras 10 muestras:", muestras[:10])
   print("Media de las muestras:", np.mean(muestras))

* Poisson

**Ejemplo 1**

.. code:: Python

   from scipy.stats import poisson

   # Parámetro λ (tasa promedio de eventos, por ejemplo, 3 llamadas por hora)
   lam = 3

   # 1. Probabilidad de que ocurran exactamente k = 5 eventos: P(X = 5)
   k = 5
   prob_exacta = poisson.pmf(k, mu=lam)
   print(f'Probabilidad exacta de {k} eventos: {prob_exacta:.4f}')

   # 2. Probabilidad de que ocurran 5 o menos eventos: P(X <= 5)
   prob_acumulada = poisson.cdf(k, mu=lam)
   print(f'Probabilidad acumulada (<= {k} eventos): {prob_acumulada:.4f}')

   # 3. Probabilidad de que ocurran más de 5 eventos: P(X > 5)
   prob_mayor = 1 - poisson.cdf(k, mu=lam)
   print(f'Probabilidad mayor a {k} eventos: {prob_mayor:.4f}')

**Ejemplo 2**

.. code:: Python

   import numpy as np

   # Generar 10 números aleatorios con una media λ = 3
   muestras = np.random.poisson(lam=3, size=10)
   print('Muestras generadas:', muestras)

   # Generar una matriz de 2x3 con λ = 5
   matriz = np.random.poisson(lam=5, size=(2, 3))
   print('Matriz generada:\n', matriz)


* Normal

.. code:: Python

   from scipy.stats import norm

   # Definir una distribución normal con media (loc) = 10 y desviación estándar (scale) = 2
   mu, sigma = 10, 2
   distribucion = norm(loc=mu, scale=sigma)
   
   # 1. Función de densidad de probabilidad (PDF) en x = 11
   print("PDF:", distribucion.pdf(11))

   # 2. Función de distribución acumulada (CDF) hasta x = 12
   print("CDF:", distribucion.cdf(12))

   # 3. Generar 5 números aleatorios con esta distribución
   print("Aleatorios:", distribucion.rvs(size=5))




