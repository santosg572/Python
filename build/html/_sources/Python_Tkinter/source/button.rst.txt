Button
======

The Tkinter Button widget is a fundamental element in Python's Tkinter library for creating graphical user interfaces (GUIs). It allows users to trigger actions or events 
by clicking it. 

**Creating a Tkinter Button:**

* Import Tkinter: Begin by importing the Tkinter module.

.. code:: Python

    import tkinter as tk

Create a root window: Instantiate a Tk object, which represents the main application window.

.. code:: Python

    root = tk.Tk()

Define a callback function (optional): If the button is intended to perform an action, define a Python function or method that will be executed when the button is clicked.

.. code:: Python

    def on_button_click():
        print("Button clicked!")

Create the Button widget: Instantiate a tk.Button object, passing the parent widget (usually root) and configuring its properties.

.. code:: Python

    button = tk.Button(root, text="Click Me", command=on_button_click)

* **text**: Sets the label displayed on the button.
* **command**: Specifies the function or method to be called when the button is pressed. 
* **Pack or place the button**: Use a layout manager (like pack, grid, or place) to position the button within the parent window.

.. code:: Python

    button.pack() # or button.grid(row=0, column=0) or button.place(x=50, y=50)

Start the main event loop: Call root.mainloop() to run the Tkinter event loop, which listens for user interactions and updates the GUI.

.. code:: Python

    root.mainloop()

**Common Button Options:**

* text: The text displayed on the button.
* command: The function to call when the button is clicked.
* bg (background): The normal background color of the button.
* fg (foreground): The normal foreground (text) color.
* cactivebackground: Background color when the button is hovered over.
* activeforeground: Foreground color when the button is hovered over.
* font: The font used for the button's text.
* image: An image to display on the button instead of text.
* state: Sets the button's state (e.g., tk.NORMAL, tk.DISABLED). 

**Example:**

.. code:: Python

   import tkinter as tk

   def greet():
       print("Hello from the button!")

   root = tk.Tk()
   root.title("Button Example")

   my_button = tk.Button(root, text="Say Hello", command=greet, bg="lightblue", fg="darkblue")
   my_button.pack(pady=20)

   root.mainloop()

-----------------------------------------------------------------------------------------------------

Python Tkinter - Create Button Widget

The Tkinter Button widget is a graphical control element used in Python's Tkinter library to create clickable buttons in a graphical user interface (GUI). It provides a 
way for users to trigger actions or events when clicked.

**Tkinter Button Widget Syntax**

The syntax to use the button widget is given below.

.. code:: Python

   Button(parent, options) 

**Parameters**

* parent: This parameter is used to represents the parent window.
* options:There are many options which are available and they can be used as key-value pairs separated by commas.

**Tkinter Button Options**

* activebackground: Background color when the button is under the cursor.
* activeforeground: Foreground color when the button is under the cursor.
* anchor: Specifies the position of the content (text or image) inside the button.
* bd or borderwidth: Width of the border around the outside of the button
* bg or background: Normal background color.
* command: Function or method to be called when the button is clicked.
* cursor: Selects the cursor to be shown when the mouse is over the button.
* text: Text displayed on the button.
* disabledforeground: Foreground color is used when the button is disabled.
* fg or foreground: Normal foreground (text) color.
* font: Text font to be used for the button's label.
* height: Height of the button in text lines
* highlightbackground: Color of the focus highlight when the widget does not have focus.
* highlightcolor: The color of the focus highlight when the widget has focus.
* highlightthickness: Thickness of the focus highlight.
* image: Image to be displayed on the button (instead of text).
* justify: tk.LEFT to left-justify each line; tk.CENTER to center them; or tk.RIGHT to right-justify.
* overrelief: The relief style to be used while the mouse is on the button; default relief is tk.RAISED.
* padx, pady: padding left and right of the text. / padding above and below the text.
* width: Width of the button in letters (if displaying text) or pixels (if displaying an image).
* underline: Default is -1, underline=1 would underline the second character of the button's text.
* width: Width of the button in letters
* wraplength: If this value is set to a positive number, the text lines will be wrapped to fit within this length.

**Methods**

1. flash(): Causes the button to flash several times between active and normal colors. Leaves the button in the state it was in originally. Ignored if the button is 
disabled.

2. invoke(): Calls the button's command callback, and returns what that function returns. Has no effect if the button is disabled or there is no callback.

**Creating a Button using Tkinter**

In this example, below code uses the tkinter library to create a graphical user interface. It defines a function, button_clicked(), which prints a message when called. 
Then, it creates a tkinter window (root) and a button within it, configured with various options like text, color, font, and behavior.

.. code:: Python

   import tkinter as tk

   def button_clicked():
       print("Button clicked!")

   root = tk.Tk()

   # Creating a button with specified options
   button = tk.Button(root, 
                   text="Click Me", 
                   command=button_clicked,
                   activebackground="blue", 
                   activeforeground="white",
                   anchor="center",
                   bd=3,
                   bg="lightgray",
                   cursor="hand2",
                   disabledforeground="gray",
                   fg="black",
                   font=("Arial", 12),
                   height=2,
                   highlightbackground="black",
                   highlightcolor="green",
                   highlightthickness=2,
                   justify="center",
                   overrelief="raised",
                   padx=10,
                   pady=5,
                   width=15,
                   wraplength=100)

   button.pack(padx=20, pady=20)

   root.mainloop()

**Creation of Button without using TK Themed Widget**

Creation of Button using tk themed widget (tkinter.ttk). This will give you the effects of modern graphics. Effects will change from one OS to another because it is 
basically for the appearance.

As you can observe that BORDER is not present in 2nd output because tkinter.ttk does not support border. Also, when you hover the mouse over both the buttons ttk.Button 
will change its color and become light blue (effects may change from one OS to another) because it supports modern graphics while in the case of a simple Button it won't 
change color as it does not support modern graphics.

.. code:: Python

   # import tkinter module 
   from tkinter import *        

   # Following will import tkinter.ttk module and 
   # automatically override all the widgets 
   # which are present in tkinter module. 
   from tkinter.ttk import *

   # Create Object
   root = Tk() 

   # Initialize tkinter window with dimensions 100x100             
   root.geometry('100x100')     

   btn = Button(root, text = 'Click me !', 
                command = root.destroy) 

   # Set the position of button on the top of window 
   btn.pack(side = 'top')     

   root.mainloop() 


**Note:** The tkinter.ttk module provides access to the Tk-themed widget set, introduced in Tk 8.5. If Python has not been compiled against Tk 8.5, this module can still 
be 
accessed if Tile has been installed. The former method using Tk 8.5 provides additional benefits including anti-aliased font rendering under X11 and window transparency.
The basic idea for tkinter.ttk is to separate, to the extent possible, the code implementing a widget’s behavior from the code implementing its appearance. tkinter.ttk is 
used to create modern GUI (Graphical User Interface) applications that cannot be achieved by tkinter itself.

**Note:** For more reference, you can read our article:

1. What is Widgets

2. Python Tkinter Overview

3. Python Tkinter Tutorial


