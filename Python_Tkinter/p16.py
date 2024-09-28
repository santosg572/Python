from tkinter import *

root = Tk()

var1 = StringVar()
var1.set('Php')

opt1 = OptionMenu(root, var1, 'Php', 'Java').pack(fill=X)

def state(): print(var1.get()) 

Button(root, command=state, text='Ver Lenguaje').pack()

root.mainloop()

