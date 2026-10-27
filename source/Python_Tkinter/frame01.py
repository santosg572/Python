import tkinter as tk

def say_hello():
    print("Hello from the frame!")

root = tk.Tk()
root.title("Frame Example")

# Create a Frame
my_frame = tk.Frame(root, bg="lightblue", bd=2, relief=tk.GROOVE)
my_frame.pack(padx=10, pady=10)

# Add a Label to the Frame
label = tk.Label(my_frame, text="This is inside a Frame", font=("Arial", 12))
label.pack(pady=5)

# Add a Button to the Frame
button = tk.Button(my_frame, text="Click Me", command=say_hello)
button.pack(pady=5)

root.mainloop()


