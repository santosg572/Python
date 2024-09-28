from tkinter import *
 
def salida(event):
     print(nombre.get())
 
root = Tk()
nombre = StringVar()
 
txt = Entry(root, textvariable=nombre)
txt.pack(expand=YES, fill=X)
txt.bind('<Key-Return>', salida)
 
root.mainloop()

