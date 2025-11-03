import tkinter

datos= '''
Por una mirada, un mundo,
por una sonrisa, un cielo,
por un beso… ¡yo no sé
qué te diera por un beso!
'''

datos = datos.split('\n')

print(type(datos))



window = tkinter.Tk()
# to rename the title of the window

window.title("GUI")
# pack is used to show the object in the window

color = ['green', 'yellow']

k = 1
for ss in datos:
  i = k % 2
  print(i)
  label = tkinter.Label(window, text = ss, bd=200, bg=color[i]).pack()
  k = k+1

window.mainloop()
