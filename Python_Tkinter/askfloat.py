from tkinter import *
from tkinter.simpledialog import *
root = Tk()
print(askfloat('Entry', 'Enter float'))
print(askinteger('Entry', 'Enter integer'))
print(askstring('Entry', 'Enter string'))
root.mainloop()


