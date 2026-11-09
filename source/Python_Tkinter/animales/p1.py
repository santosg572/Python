import tkinter as tk

win = tk.Tk()

l1 = tk.Label(win, text="hola", background='red', borderwidth=4, foreground='green', font=("Helvetica", 20))

l1.pack(padx = 100, pady=100)
l2 = tk.Label(win, text="hola")
l2.pack(padx = 10, pady=10)

#l3 = tk.Label(win, bitmap="tortuga01.jpg")
#l3.pack(padx = 10, pady=10)

print(win. grid_size())

#win.destroy()

win.mainloop()


