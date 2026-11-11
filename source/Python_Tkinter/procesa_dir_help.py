import tkinter

file = "tkinter_dir.txt"

fil = open(file, 'r')

datos = fil.read()

datos = datos.replace("[" , '')
datos = datos.replace("]" , '')
datos = datos.replace(' ', '')
datos = datos.replace("'" , '')

datos = datos.split(',')

for ss in datos:
  print('=============================== '+ ss)
  print(help(eval('tkinter.'+ss)))






