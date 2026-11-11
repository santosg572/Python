Prueba de Lateralidad (Edinburgh)
=================================

.. code:: Python

   import tkinter as tk

   k = 0

   def boton(bb=0):
     global k
     print('hola')
     print(bb)
     k = k+1
     label.config(text=tt[k])

   tt = ['1. Escribir', '2. Dibujar', '3. Lanzar un objeto', '4. Cepillarse los dientes'
	'5. Usar un cuchillo (sin tenedor)', '6. Cortar con tijeras', '7. Usar una cuchara'
	'8. Barrer (con una escoba)', '9. Encender una cerilla (fósforo)'
	'10. Abrir la tapa de una caja']

   win = tk.Tk()

   labelt = tk.Label(win, text='Cual mano utiliazas para hacer la siguiente actividad [izquierda, derecha o cualquiera de las dos' )
   labelt.pack()

   label = tk.Label(win, text=tt[0])
   label.pack()

   b1 = tk.Button(win, text='IZQUIERDA', command=lambda: boton('0'))
   b1.pack()

   b2 = tk.Button(win, text='DERECHA', command=lambda: boton('1'))
   b2.pack()

   b3 = tk.Button(win, text='AMBAS', command=lambda: boton('2'))
   b3.pack()

   win.mainloop()



