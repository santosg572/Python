from tkinter import *

Main_window = Tk()

my_text = "GeeksforGeeks updated !!!"

def counter():
    global my_text
    
    my_label.config(text = my_text)

my_button = Button(Main_window,
                   text = "Please update",
                   command = counter)

my_label = Label(Main_window,
                 text = "geeksforgeeks")

my_label.pack()
my_button.pack()

Main_window.mainloop()



