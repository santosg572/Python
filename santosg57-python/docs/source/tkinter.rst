tkinter
=======

**Ejemplo: ventana**

.. code:: Python

   import tkinter
   window = tkinter.Tk()

   window.title("GUI")
   window.geometry('800x600+100+50')
   window.mainloop()

**Ejemplo: label**

.. code:: Python

   import tkinter
   window = tkinter.Tk()

   window.title("GUI")

   label1 = tkinter.Label(window, text = "Hola como estas?").pack()

   label2 = tkinter.Label(window, text = "Te estraño!").pack()

   label3 = tkinter.Label(window, bitmap = "bebe.jpg").pack()

   label4 = tkinter.Label(window, text = "Te estraño mucho!",font=("Arial", 24))
   label4.pack(pady=50)

   window.mainloop()

**Ejemplo boton**

.. code:: Python

   import tkinter
   window = tkinter.Tk()

   def botones(x = ""):
     print('presiono bel boton')
     print(x)


   def fun():
     print('presiono bel boton')

   window.title("Button GUI")


   boton1 = tkinter.Button(window,text="este es un boton")
   boton1.pack()

   boton2 = tkinter.Button(window,text="boton2 con respuesta", command=fun)
   boton2.pack()

   boton3 = tkinter.Button(window,text="boton3", command=lambda:botones("3"))
   boton3.pack()

   boton4 = tkinter.Button(window,text="boton4", command=lambda:botones("4"))
   boton4.pack()

   tkinter.mainloop()

**Ejemplo texto**

.. code:: Python

   import tkinter
   window = tkinter.Tk()

   def obten():
     print('presiono bel boton')
     xx  = ent1.get()
     print(xx)

   bot1 = tkinter.Button(text="obten el texto", command=lambda: obten())
   bot1.pack()

   ent1 = tkinter.Entry()
   ent1.pack()

   tkinter.mainloop()

**Ejemplo RadioBoton**

.. code:: Python

   import tkinter 

   def sel():
      selection = "You selected the option " + str(var.get())
      print(selection)
      label.config(text = selection)

   root = tkinter.Tk()
   root.geometry('200x100+200+100')

   var = tkinter.IntVar()

   R1 = tkinter.Radiobutton(root, text="Option 1", variable=var, value=1, command=sel)
   R1.pack()

   R2 = tkinter.Radiobutton(root, text="Option 2", variable=var, value=2, command=sel)
   R2.pack()

   R3 = tkinter.Radiobutton(root, text="Option 3", variable=var, value=3, command=sel)
   R3.pack()

   label = tkinter.Label(root)
   label.pack()

   root.mainloop()






