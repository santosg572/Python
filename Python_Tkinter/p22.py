from tkinter import *

canvas = Canvas(width=400, height=300, bg='white')
canvas.pack(expand=YES, fill=BOTH)
canvas.create_line(10, 10, 80, 80)
canvas.create_line(10, 80, 80, 10)
canvas.create_oval(100, 10, 180, 80, width=2, fill='blue')
canvas.create_arc(200, 10, 280, 100)
canvas.create_rectangle(10, 100, 200, 200, width=5, fill='red')
canvas.create_text(100, 280, text='tkinter canvas', fill='green')
mainloop()


