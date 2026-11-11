Algunas curvas hermosas
=====================

**1. La Curva de la Mariposa (Fay's Butterfly Curve)**

Descubierta por Temple H. Fay en 1989, es una de las funciones paramétricas más famosas por replicar con increíble fidelidad la silueta de 
una mariposa orgánica.

* Ecuaciones (:math:`t \in [0, 12\pi]`):

.. math::

   x(t) = \sin(t) \cdot \left( e^{\cos(t)} - 2\cos(4t) - \sin^5\left(\frac{t}{12}\right) \right)

   y(t) = \cos(t) \cdot \left( e^{\cos(t)} - 2\cos(4t) - \sin^5\left(\frac{t}{12}\right) \right)


**2. Espirógrafos / Hipotrocoides y Epitrocoides**

Son las curvas generadas por el movimiento de un punto en un círculo que rueda dentro o fuera de otro círculo (como el clásico juguete 
Spirograph).

* Ecuaciones (Hipotrocoide general):

.. math::

   x(t) = (R - r)\cos(t) + d\cos\left(\frac{R - r}{r} t\right)

   y(t) = (R - r)\sin(t) - d\sin\left(\frac{R - r}{r} t\right)$$

* Ejemplos notables:

  - La Astroide (:math:`R=4, r=1, d=1`): Una estrella de 4 puntas cóncavas perfecta.
  - Rosetas de N pétalos: Dependiendo de la proporción racional entre los radios $R$ y $r$, produce mandalas e intrincados encajes simétricos.

**3. Las Figuras de Lissajous**

Surgen de la superposición de dos movimientos armónicos simples en direcciones perpendiculares a distintas frecuencias y desfases. Son muy 
utilizadas en física y osciloscopios.

* Ecuaciones:

.. math::

   x(t) = A \sin(a t + \delta)

   y(t) = B \sin(b t)$$

**4. La Espiral Parmétrica Cónica y de Fermat (3D / 2D)**

Las espirales paramétricas trascienden el plano :math:`2\D` cuando se añade un componente :math:`z(t)`.

* Espirál Cónica / Toroidal 3D:

.. math::

   x(t) = t \cdot \cos(t), 
 
   y(t) = t \cdot \sin(t), 

    z(t) = t$$

