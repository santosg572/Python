import tkinter
window = tkinter.Tk()
# to rename the title of the window

dd = dir(tkinter)

for ss in dd:
   if ss[0] != '_':
     print(help(eval('tkinter.'+ss)))



'''
window.title("GUI")
b1 = tkinter.Button(window,text="Hola buenos días")
b1.pack()
b2 = tkinter.Button(window,text="Como estas")
b2.pack()
e1 = tkinter.Entry()
l1 = tkinter.Label()
print(help(window.grid))

'''
