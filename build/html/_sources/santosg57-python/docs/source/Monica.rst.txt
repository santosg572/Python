Monica
===========

.. code:: Python

   #n es el número de observaciones
   #x barra es el promedio

   x=[1.00, 2.00, 3.00, 4.00, 5.00, 6.00, 7.00, 8.00, 9.00, 10.00, 11.00, 12.00]
   y=[1.23, 2.13, 1.42, -0.69, 4.29, 3.64, 9.30, 10.62, 7.42, 8.40, 12.30, 10.30]
   print('Dados: ')
   print('x= '+ str(x))
   print('y= '+str(y))

   np1=len(x)

   sumxy=0

   for i in range(np1):
    sumxy= sumxy+x[i]*y[i]

   sumx=0
   for i in range(np1):
    sumx=sumx+x[i]

   mx=sumx/np1

   sumy=0
   for i in range(np1):
    sumy=sumy+y[i]

   my=sumy/np1

   nxy=np1*mx*my

   sumx2=0
   for i in range(np1):
    sumx2=sumx2+x[i]**2

   den2=(sumx**2)/np1

   print('Calculamos: ')

   b1=(sumxy-nxy)/(sumx2-den2)
   print('b1: '+ str(b1))

   b0=my-b1*mx
   print('b0: ' + str(b0))

   print('Entonces: \n y = '+ str(b0)+ ' + '+ str(b1)+'x')






