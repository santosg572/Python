import tkinter

datos= '''1
2
3
4 '''

datos = datos.split('\n')

print(len(datos))



window = tkinter.Tk()
# to rename the title of the window

window.title("GUI")
# pack is used to show the object in the window

color = ['green', 'yellow']
posicion = ['top', 'left', 'bottom',  'right'] 
k = 1

for ss in datos:
  i = k % 2
  print(k)
  print(posicion[k-1])
  label = tkinter.Label(window, text = ss,font=("Helvetica", 20),  bd=5, bg=color[i], fg="red").pack(side=posicion[k-1])
  k = k+1

window.mainloop()
