Algunas distribuciones de Probabilidad
======================================

**Continuas**

* Distribución Normal

En estadística y probabilidad se llama distribución normal, distribución de Gauss, distribución gaussiana a una gráfica de 
función de densidad con forma acampanada y simétrica respecto de un determinado parámetro estadístico. Esta curva se conoce como 
campana de Gauss y es el gráfico de una función gaussiana. Su forma general es:

.. math::

   f(x)={\frac {1}{\sqrt {2\pi \sigma ^{2}}}}e^{-{\frac {(x-\mu )^{2}}{2\sigma ^{2}}}}

Algunas graficas de la distribución son:

**Función de densidad de probabilidad**

.. image:: Normal_distribution_pdf.png
   :scale: 50%

**Función de distribución de probabilidad**

.. image:: Normal_distribution_cdf.png
   :scale: 50%

**Discretas** 

* Distribución binomial

En teoría de la probabilidad y estadística, la distribución binomial o distribución binómica es una distribución de probabilidad 
discreta que cuenta el número de éxitos en una secuencia de :math:`n` ensayos de Bernoulli independientes entre sí con una probabilidad fija 
:math:`p` de ocurrencia de éxito entre los ensayos. Un experimento de Bernoulli se caracteriza por ser dicotómico, esto 
es, solo dos resultados son posibles; a uno de estos se le denomina “éxito” y tiene una probabilidad de ocurrencia 
:math:`p`, y al otro se le denomina “fracaso” y tiene una probabilidad :math:`q = 1-p`.

Es posible entonces obtener la probabilidad de k éxitos en una repetición de n experimentos:

.. math::

   \mathbb {P} (X=k)={n \choose k}\,p^{k}(1-p)^{n-k}

Algunas graficas de la ditribución binomial:

**Función de probabilidad**

.. image:: Binomial_distribution_pmf.svg.webp
   :scale: 50%

**Función de distribución acumulada**

.. image:: Binomial_distribution_cdf.svg.webp	
   :scale: 50%

**EJEMPLOS**

* EXAMPLE 4.3.2

Los datos del Centro Estatal de Estadísticas de Salud de Carolina del 
Norte (A-3) indican que el 14 por ciento de las madres admitió fumar uno o más cigarrillos al día durante el embarazo. Si se 
selecciona una muestra aleatoria de tamaño 10 de esta población, ¿cuál es la probabilidad de que contenga exactamente cuatro 
madres que admitieron haber fumado durante el embarazo?

**Solución**

Tomamos la probabilidad de que una madre admita fumar como 0.14. Usando la ecuación 4.3.2 encontramos

.. image:: img_4_3_2.png

* EXAMPLE 4.3.3

Suponga que se sabe que el 10 % de una determinada población padece daltonismo. Si se extrae una muestra aleatoria de 25 
personas de esta población, utilice la Tabla B del apéndice para hallar la probabilidad de que:

a) Cinco o menos serán daltónicos.

Solución P(X <= 5) = .9666

b) Seis o más serán daltónicos.

Solución: P(X >= 6) = .0334

c) Entre seis y nueve, inclusive, serán daltónicos.

Solución: P(6 <= X <= 9) = .0333

d) Dos, tres o cuatro serán daltónicos.

Solución: P(2 <= X <= 4) = .6308


