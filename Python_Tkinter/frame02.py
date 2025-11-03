import tkinter as tk

root = tk.Tk()
root.title("Multiple Frames")

# Top Frame
top_frame = tk.Frame(root, bg="lightgreen", bd=2, relief=tk.RAISED)
top_frame.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)

tk.Label(top_frame, text="Header Section", font=("Arial", 14)).pack(pady=5)

# Left Frame
left_frame = tk.Frame(root, bg="lightcoral", bd=2, relief=tk.SUNKEN)
left_frame.pack()

#left_frame.pack(side=tk.LEFT, fill=tk.Y, padx=5, pady=5)

tk.Label(left_frame, text="Navigation").pack(padx=10, pady=10)
tk.Button(left_frame, text="Option 1").pack(pady=5)
tk.Button(left_frame, text="Option 2").pack(pady=5)

# Right Frame (Content Area)
right_frame = tk.Frame(root, bg="lightyellow", bd=2, relief=tk.RIDGE)
right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=5, pady=5)

tk.Label(right_frame, text="Main Content Area", font=("Arial", 12)).pack(padx=20, pady=20)
tk.Text(right_frame, height=5, width=30).pack(padx=10, pady=10)

root.mainloop()


