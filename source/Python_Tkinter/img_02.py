from tkinter import *

ventana = Tk()
ventana.config(bg="red")
ventana.geometry("400x200")
ventana.resizable(width=FALSE, height=FALSE)
ventana.title("Tutor de Programacion")
widget = Label(ventana, text='Hola GUI tkinter', fg = 'skyblue', font=('Ravie', 24))
widget.pack()
ventana.mainloop()

