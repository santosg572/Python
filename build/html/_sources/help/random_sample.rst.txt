Help on method sample in module random:
=======================================

sample(population, k, *, counts=None) method of random.Random instance
    Chooses k unique random elements from a population sequence or set.

    Selecciona k elementos aleatorios únicos de una secuencia o conjunto poblacional.
    
    Returns a new list containing elements from the population while
    leaving the original population unchanged.  The resulting list is
    in selection order so that all sub-slices will also be valid random
    samples.  This allows raffle winners (the sample) to be partitioned
    into grand prize and second place winners (the subslices).
    
    Devuelve una nueva lista que contiene elementos de la población, dejando intacta la población original. La lista resultante sigue el orden de selección, de modo que todos sus subsegmentos constituyen, a su vez, muestras aleatorias válidas. Esto permite dividir a los ganadores de un sorteo (la muestra) en grupos, como los ganadores del gran premio y los del segundo lugar (los subsegmentos).

    Members of the population need not be hashable or unique.  If the
    population contains repeats, then each occurrence is a possible
    selection in the sample.

    Los elementos de la población no necesitan ser «hashables» ni únicos. Si la población contiene elementos repetidos, cada una de esas apariciones constituye una posible selección dentro de la muestra.
    
    Repeated elements can be specified one at a time or with the optional
    counts parameter.  For example:

    Los elementos repetidos pueden especificarse uno a uno o mediante el parámetro opcional de recuento. Por ejemplo:
    
        sample(['red', 'blue'], counts=[4, 2], k=5)
    
    is equivalent to:
    
        sample(['red', 'red', 'red', 'red', 'blue', 'blue'], k=5)
    
    To choose a sample from a range of integers, use range() for the
    population argument.  This is especially fast and space efficient
    for sampling from a large population:
    
        sample(range(10000000), 60)

