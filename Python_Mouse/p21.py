#Import tkinter library

import tkinter as tk

#Create an instance of tkinter frame or window

def termino():
  win.destroy()

win= tk.Tk()

#Set the geometry of tkinter frame

win.geometry("750x250")

l1 = tk.Label(win, image='brain_lobes_anatomy.jpg')
l1.pack()

def callback(e):
   x= e.x
   y= e.y
    
   if x < 750 and y < 250:
     print("Pointer is currently at %d, %d" %(x,y))

win.bind('<Motion>',callback)
win.mainloop()


