Distribución binomial
=====================

En teoría de la probabilidad y estadística, la distribución binomial o distribución binómica es una distribución de probabilidad discreta que 
cuenta el número de éxitos en una secuencia de :math:`n`
ensayos de Bernoulli independientes entre sí con una probabilidad fija 
:math:`p``de ocurrencia de éxito entre los ensayos. Un experimento de Bernoulli se caracteriza por ser dicotómico, esto es, solo dos 
resultados son posibles; a uno de estos se le denomina “éxito” y tiene una probabilidad de ocurrencia 
:math:`p`, y al otro se le denomina “fracaso” y tiene una probabilidad :math:`q=1-p`. 

La distribución binomial se utiliza con frecuencia para modelizar el número de aciertos en una muestra de tamaño n extraída con reemplazo de 
una población de tamaño N. Si el muestreo se realiza sin reemplazo, las extracciones no son independientes, por lo que la distribución 
resultante es una distribución hipergeométrica, no una distribución binomial. Sin embargo, para N mucho mayores que n, la distribución 
binomial sigue siendo una buena aproximación, y se utiliza ampliamente.

Es posible entonces obtener la probabilidad de k éxitos en una repetición de n experimentos:

.. math::

   P(X = k) = \begin{pmatrix} n \\
   k \end{pmatrix} p^k (1-p)^{n-k}



