import tkinter as tk

def on_mouse_motion(event):
    """
    This function is called whenever the mouse moves within the window.
    It prints the x and y coordinates of the mouse relative to the widget.
    """
    x = event.x
    y = event.y
    print(f"Mouse position: x={x}, y={y}")

def on_mouse_click(event):
    """
    This function is called whenever a mouse button is clicked within the window.
    It prints the x and y coordinates of the click relative to the widget.
    """
    x = event.x
    y = event.y
    print(f"Mouse clicked at: x={x}, y={y}")

# Create the main Tkinter window

root = tk.Tk()
root.title("Mouse Position Detector")
root.geometry("400x300")

# Bind the <Motion> event to the on_mouse_motion function
# This will trigger the function whenever the mouse moves within the root window

root.bind("<Motion>", on_mouse_motion)

# Bind the <Button-1> event (left mouse button click) to the on_mouse_click function

root.bind("<Button-1>", on_mouse_click)

# Start the Tkinter event loop
root.mainloop()


