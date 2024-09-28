from tkinter import *
def Ver(value):
  print(value)
root = Tk()
scl = Scale(root, from_=-100, to=100, tickinterval=50,
length=400, resolution=10, showvalue=NO,
orient='horizontal', command=Ver,

label="Scale o Slider - Tutor de Programacion")

scl.pack(expand=YES, fill=Y)


def VerValor():

  print('Valor actual:', scl.get())


btn = Button(root, text="Valor del Slider", command=VerValor)

btn.pack()


root.mainloop()

