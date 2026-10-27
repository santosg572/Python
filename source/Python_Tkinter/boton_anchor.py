import tkinter

datos= '''1
2
3
4
5
6
7
8
9  '''

datos = datos.split('\n')

print(len(datos))



window = tkinter.Tk()
window.geometry("400x400")

# to rename the title of the window

window.title("GUI")
# pack is used to show the object in the window

color = ['green', 'yellow']
posicion = ['n', 'ne', 'e', 'center', 'se', 's', 'sw', 'w', 'nw'] 
k = 1

for ss in datos:
  i = k % 2
  print(k)
  print(posicion[k-1])
  label = tkinter.Label(window, text = ss,font=("Helvetica", 20),  bd=5, bg=color[i], fg="red").pack(anchor=posicion[k-1])
  k = k+1

window.mainloop()
