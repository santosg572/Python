import tkinter
window = tkinter.Tk()

window.title('CALCULADORA')
window.geometry('400x200+100+200')

#foreground

b1 = tkinter.Button(window,text='hola',foreground='red', background='red')
b1.pack()

tkinter.mainloop()

'''


dd = dir(tkinter)

print(dd)

ss=help(tkinter.Button)

print(ss)

ss=help(tkinter.Pack)

print(ss)


print(help(window.config))
print(window.geometry())


for ss in dd:
   if ss[0] != '_':
     print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&& ' + ss + ' &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&')
     print(help(eval('tkinter.'+ss)))
'''


