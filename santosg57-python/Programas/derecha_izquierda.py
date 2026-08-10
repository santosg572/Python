from tkinter import *

datos = ['1.- Tirar una pelota',
'2.- Sacar punta a un lapicero',
'3.- Clavar un clavo',
'4.- Cepillarse los dientes']


Main_window = Tk()

my_text = datos[0]

k = 0
def derecha():
    global my_text
    global k

    k = k+1
    my_label.config(text = datos[k])

my_derecha = Button(Main_window,
                   text = 'DERECHA',
                   command = derecha)

my_label = Label(Main_window,
                 text = datos[0])

my_label.pack()
my_derecha.pack()

Main_window.mainloop()



