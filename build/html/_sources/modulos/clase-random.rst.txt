Clase random
============

.. code:: Python

   import random

**Algunos métodos:**

``'betavariate', 'binomialvariate', 'choice', 'choices', 'expovariate', 'gammavariate', 'gauss', 'getrandbits', 'getstate', 'lognormvariate', 'main', 'normalvariate', 'paretovariate', 'randbytes', 'randint', 'random', 'randrange', 'sample', 'seed', 'setstate', 'shuffle', 'triangular', 'uniform', 'vonmisesvariate', 'weibullvariate'``


**Ayuda**

.. code:: Bash

   choice(seq) method of random.Random instance
	       Choose a random element from a non-empty sequence.

   choices(population, weights=None, *, cum_weights=None, k=1) method of random.Random instance
       Return a k sized list of population elements chosen with replacement.
       If the relative weights or cumulative weights are not specified,
          the selections are made with equal probability.

   gauss(mu=0.0, sigma=1.0) method of random.Random instance
       Gaussian distribution.
       mu is the mean, and sigma is the standard deviation.  This is
       slightly faster than the normalvariate() function.

   randint(a, b) method of random.Random instance
       Return random integer in range [a, b], including both end points.

   randint(a, b) method of random.Random instance
       Return random integer in range [a, b], including both end points.

   sample(population, k, *, counts=None) method of random.Random instance
       Chooses k unique random elements from a population sequence.
       Returns a new list containing elements from the population while
       leaving the original population unchanged.  The resulting list is
       in selection order so that all sub-slices will also be valid random
       samples.  This allows raffle winners (the sample) to be partitioned
       into grand prize and second place winners (the subslices).
       Members of the population need not be hashable or unique.  If the
       population contains repeats, then each occurrence is a possible
       selection in the sample.

       Repeated elements can be specified one at a time or with the optional
       counts parameter.  For example:

           sample(['red', 'blue'], counts=[4, 2], k=5)

   uniform(a, b) method of random.Random instance
       Get a random number in the range [a, b) or [a, b] depending on rounding.



**Algunos métodos y ejemplos:**

.. code:: Python

   import random

   random.gauss()

   round(random.gauss(),2)

   random.randint(1,100)

   random.random()

   ss = random.sample(['red', 'blue'], counts=[4, 2], k=5)
   print(ss)
   type(ss)

   random.uniform(1,10)


    


