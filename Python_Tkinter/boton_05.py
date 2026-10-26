from tkinter import *

root = Tk()

root.columnconfigure(0, weight=0)
root.columnconfigure(1, weight=1)
root.rowconfigure(2, weight=1)

Label(root, text="Nombre:").grid(row=0, column=0)
Label(root, text="Apellido:").grid(row=1, column=0)

Entry(root).grid(row=0, column=1, sticky=E+W)
Entry(root).grid(row=1, column=1, sticky=E+W)

Button(root, text="Aceptar").grid(pady=10,
                                  padx=10,
                                  row=2,
                                  column=0,
                                  columnspan=2,
                                  sticky=S+N+E+W)

root.mainloop()

