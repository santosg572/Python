#Import tkinter library

from tkinter import *

#Create an instance of tkinter frame or window

def termino():
  win.destroy()

win= Tk()

#Set the geometry of tkinter frame

win.geometry("750x250")

def callback(e):
   x= e.x
   y= e.y
   print("Pointer is currently at %d, %d" %(x,y))
   if x > 750 or y > 250:
     termino()

win.bind('<Motion>',callback)
win.mainloop()


