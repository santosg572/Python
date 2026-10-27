import tkinter
from tkinter import ttk

def fun(ss=''):
  global tt
  global kk
  
  kk = kk+1
  if kk == 4:
    window.destroy()
  
  print(datos[kk])

  label.config(text = datos[kk])
  print(ss)


datos = ['1.- Tirar una pelota',
'2.- Sacar punta a un lapicero',
'3.- Clavar un clavo',
'4.- Cepillarse los dientes']

window = tkinter.Tk()

# to rename the title of the window

window.title("TEST DE HARRIS")

# pack is used to show the object in the window
kk = 0

label = tkinter.Label(window, text = datos[kk], font=("Helvetica", 30), bg="black",  bd=20,)

izq = tkinter.Button(window, text = 'IZQUIERDA',font=("Helvetica", 15), command=lambda:fun('1'), bd=10)
der = tkinter.Button(window, text = 'DERECHA',font=("Helvetica", 15), bd=10, command=lambda:fun('2'))

label.pack(side='top')
izq.pack(side='left')
der.pack(side='right')

window.mainloop()

