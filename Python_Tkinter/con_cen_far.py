from tkinter import *

root = Tk()
root.geometry("150x200")
 
w = Label(root, text ='GeeksForGeeks',
          font = "50") 

w.pack()
 
scroll_bar = Scrollbar(root)

mylist = Listbox(root, 
                 yscrollcommand = scroll_bar.set )
 
for line in range(0, 100):
    mylist.insert(END, str(line))

mylist.pack( side = LEFT, fill = BOTH )

scroll_bar.config( command = mylist.yview )
scroll_bar.set(0, 100)
scroll_bar.pack( side = RIGHT,
                fill = Y )

root.mainloop()

