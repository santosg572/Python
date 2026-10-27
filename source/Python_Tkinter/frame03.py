import tkinter as tk

root = tk.Tk()
root.title("Nested Frames")

outer_frame = tk.Frame(root, bd=5, bg="green", relief=tk.SOLID)
outer_frame.pack(padx=20, pady=20)

inner_frame = tk.Frame(outer_frame, bg="white", bd=3, relief=tk.GROOVE)
inner_frame.pack(padx=10, pady=10)

tk.Label(inner_frame, text="This is the inner frame").pack(padx=15, pady=15)

root.mainloop()
