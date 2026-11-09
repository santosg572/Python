 help(tkinter)
==============

Help on package tkinter:

* NAME
*    tkinter - Wrapper functions for Tcl/Tk.

* MODULE REFERENCE
*    https://docs.python.org/3.9/library/tkinter
    
    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.


**DESCRIPTION**

    Tkinter provides classes which allow the display, positioning and
    control of widgets. Toplevel widgets are Tk and Toplevel. Other
    widgets are Frame, Label, Entry, Text, Canvas, Button, Radiobutton,
    Checkbutton, Scale, Listbox, Scrollbar, OptionMenu, Spinbox
    LabelFrame and PanedWindow.
    
    Properties of the widgets are specified with keyword arguments.
    Keyword arguments have the same name as the corresponding resource
    under Tk.
    
    Widgets are positioned with one of the geometry managers Place, Pack
    or Grid. These managers can be called with methods place, pack, grid
    available in every Widget.
    
    Actions are bound to events by resources (e.g. keyword argument
    command) or with the method bind.

    Example (Hello, World):

.. code:: Python

    import tkinter
    from tkinter.constants import *
    tk = tkinter.Tk()
    frame = tkinter.Frame(tk, relief=RIDGE, borderwidth=2)
    frame.pack(fill=BOTH,expand=1)
    label = tkinter.Label(frame, text="Hello, World")
    label.pack(fill=X, expand=1)
    button = tkinter.Button(frame,text="Exit",command=tk.destroy)
    button.pack(side=BOTTOM)
    tk.mainloop()


**PACKAGE CONTENTS**

*    __main__
*    colorchooser
*    commondialog
*    constants
*    dialog
*    dnd
*    filedialog
*    font
*    messagebox
*    scrolledtext
*    simpledialog
*    tix
*    ttk


**CLASSES**

*    builtins.Exception(builtins.BaseException)
*        _tkinter.TclError
*    builtins.object
*        builtins.float
*        builtins.int
*        CallWrapper
*        Event
*        Grid
*        Image
*            BitmapImage
*            PhotoImage
*        Misc
*            BaseWidget
*                Toplevel(BaseWidget, Wm)
*                Widget(BaseWidget, Pack, Place, Grid)
*                    Button
*                    Canvas(Widget, XView, YView)
*                    Checkbutton
*                    Entry(Widget, XView)
*                    Frame
*                    Label
*                    LabelFrame
*                    Listbox(Widget, XView, YView)
*                    Menu
*                    Menubutton
*                        OptionMenu
*                    Message
*                    PanedWindow
*                    Radiobutton
*                    Scale
*                    Scrollbar
*                    Spinbox(Widget, XView)
*                    Text(Widget, XView, YView)
*            Tk(Misc, Wm)
*        Pack
*        Place
*        Variable
*            BooleanVar
*            DoubleVar
*            IntVar
*            StringVar
*        Wm
*        XView
*        YView
*    builtins.str(builtins.object)
*        EventType(builtins.str, enum.Enum)
*    enum.Enum(builtins.object)
*        EventType(builtins.str, enum.Enum)
    


