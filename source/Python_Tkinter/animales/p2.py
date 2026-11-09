import tkinter as tk

k = 1

def boton():
  global k
  print('hola')
  k = k+1
  file = "img00"+str(k)+".jpg"
  l3.config(bitmap=file)

win = tk.Tk()

file = "img00"+str(k)+".jpg"

l3 = tk.Label(win, bitmap=file)
l3.pack(padx = 10, pady=10)

b1 = tk.Button(win, text="CONTINUAR", command=boton)
b1.pack(padx = 10, pady=10)


print(win. grid_size())

#win.destroy()

win.mainloop()


