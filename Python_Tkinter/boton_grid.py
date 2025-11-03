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

k = 1

for m in range(3):
  for n in range(3):
    i = k % 2
    print(k)
    ss = datos[k-1]
    label = tkinter.Label(window, text = ss,font=("Helvetica", 20),  bd=5, bg=color[i], fg="red")
    label.grid(row=m, column=n, padx = 5)
    k = k+1

window.mainloop()
