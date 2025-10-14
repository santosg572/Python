Design
We'll create a simple GUI tool to convert a distance in feet to the equivalent distance in meters. If we were to sketch 
this out, it might look something like this:

screen shot
A sketch of our feet to meters conversion program.

So it looks like we have a short text entry widget that will let us type in the number of feet. A "Calculate" button will 
get the value out of that entry, perform the calculation, and put the result in a label below the entry. We've also got 
three static labels ("feet," "is equivalent to," and "meters"), which help our user figure out how to work the application.

The next thing we need to do is look at the layout. The widgets we've included seem to be naturally divided into a grid 
with three columns and three rows, as illustrated below:

screen shot
The layout of our user interface, which follows a 3 x 3 grid.

Code
Now here is the Python code needed to create this entire application using Tkinter.

from tkinter import *
from tkinter import ttk

def calculate(*args):
    try:
        value = float(feet.get())
        meters.set(round(0.3048 * value, 4))
    except ValueError:
        pass

root = Tk()
root.title("Feet to Meters")

mainframe = ttk.Frame(root, padding=(3, 3, 12, 12))
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

feet = StringVar()
feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=(W, E))

meters = StringVar()
ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))

ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
mainframe.columnconfigure(2, weight=1)
for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

feet_entry.focus()
root.bind("<Return>", calculate)

root.mainloop()
Now here is the Tcl/Tk code needed to create this entire application.

package require Tk

wm title . "Feet to Meters"
grid [ttk::frame .c -padding "3 3 12 12"] -column 0 -row 0 -sticky nwes
grid columnconfigure . 0 -weight 1; grid rowconfigure . 0 -weight 1

grid [ttk::entry .c.feet -width 7 -textvariable feet] -column 2 -row 1 -sticky we
grid [ttk::label .c.meters -textvariable meters] -column 2 -row 2 -sticky we
grid [ttk::button .c.calc -text "Calculate" -command calculate] -column 3 -row 3 -sticky w

grid [ttk::label .c.flbl -text "feet"] -column 3 -row 1 -sticky w
grid [ttk::label .c.islbl -text "is equivalent to"] -column 1 -row 2 -sticky e
grid [ttk::label .c.mlbl -text "meters"] -column 3 -row 2 -sticky w

grid columnconfigure . 0 -weight 1; grid rowconfigure . 0 -weight 1
grid columnconfigure .c 2 -weight 1
foreach w [winfo children .c] {grid configure $w -padx 5 -pady 5}
focus .c.feet
bind . <Return> {calculate}

proc calculate {} {  
   if {[catch {
       set ::meters [expr {round($::feet*0.3048*10000.0)/10000.0}]
   }]!=0} {
       set ::meters ""
   }
}

vwait forever
Now here is the Ruby/Tk code needed to create this entire application.

require 'tk'
require 'tkextlib/tile'

root = TkRoot.new {title "Feet to Meters"}
content = Tk::Tile::Frame.new(root) {padding "3 3 12 12"}.grid( :sticky => 'nsew')

$feet = TkVariable.new; $meters = TkVariable.new
f = Tk::Tile::Entry.new(content) {width 7; textvariable $feet}.grid( :column => 2, :row => 1, :sticky => 'we' )
Tk::Tile::Label.new(content) {textvariable $meters}.grid( :column => 2, :row => 2, :sticky => 'we');
Tk::Tile::Button.new(content) {text 'Calculate'; command {calculate}}.grid( :column => 3, :row => 3, :sticky => 'w')

Tk::Tile::Label.new(content) {text 'feet'}.grid( :column => 3, :row => 1, :sticky => 'w')
Tk::Tile::Label.new(content) {text 'is equivalent to'}.grid( :column => 1, :row => 2, :sticky => 'e')
Tk::Tile::Label.new(content) {text 'meters'}.grid( :column => 3, :row => 2, :sticky => 'w')

TkGrid.columnconfigure root, 0, :weight => 1; TkGrid.rowconfigure root, 0, :weight => 1
TkGrid.columnconfigure content, 2, :weight => 1
TkWinfo.children(content).each {|w| TkGrid.configure w, :padx => 5, :pady => 5}
f.focus
root.bind("Return") {calculate}

def calculate
  begin
     $meters.value = (0.3048*$feet*10000.0).round()/10000.0
  rescue
     $meters.value = ''
  end
end

Tk.mainloop
Now here is the Perl/Tkx code needed to create this entire application.

use Tkx;

Tkx::wm_title(".", "Feet to Meters");
Tkx::ttk__frame(".c",  -padding => "3 3 12 12");
Tkx::grid( ".c", -column => 0, -row => 0, -sticky => "nwes");

Tkx::ttk__entry(".c.feet", -width => 7, -textvariable => \$feet);
Tkx::grid(".c.feet", -column => 2, -row => 1, -sticky => "we");
Tkx::ttk__label(".c.meters", -textvariable => \$meters);
Tkx::grid(".c.meters", -column => 2, -row => 2, -sticky => "we");
Tkx::ttk__button(".c.calc", -text => "Calculate", -command => sub {calculate();});
Tkx::grid(".c.calc", -column => 3, -row => 3, -sticky => "w");

Tkx::grid( Tkx::ttk__label(".c.flbl", -text => "feet"), -column => 3, -row => 1, -sticky => "w");
Tkx::grid( Tkx::ttk__label(".c.islbl", -text => "is equivalent to"), -column => 1, -row => 2, -sticky => "e");
Tkx::grid( Tkx::ttk__label(".c.mlbl", -text => "meters"), -column => 3, -row => 2, -sticky => "w");

Tkx::grid_columnconfigure( ".", 0, -weight => 1); 
Tkx::grid_rowconfigure(".", 0, -weight => 1);
Tkx::grid_columnconfigure(".c", 2, -weight => 1);
foreach (Tkx::SplitList(Tkx::winfo_children(".c"))) {
    Tkx::grid_configure($_, -padx => 5, -pady => 5);
}
Tkx::focus(".c.feet");
Tkx::bind(".", "<Return>", sub {calculate();});

sub calculate {
   $meters = int(0.3048*$feet*10000.0+.5)/10000.0 || '';
}

Tkx::MainLoop();
As we'll see in the next chapter, there's another, more object-oriented way to do exactly the same thing. Are we surprised?

And the resulting user interface:

screen shot
Screenshot of our completed feet to meters user interface.

A note on coding style
Each of the languages included in this tutorial has a variety of coding styles and conventions available to choose from, 
which help determine conventions for variable and function naming, procedural, functional or object-oriented styles, and so 
on.

Because the focus on this tutorial is Tk, this tutorial will keep things as simple as possible, generally using a very 
direct coding style, rather than wrapping up most of our code in procedures, modules, objects, classes and so on. As much 
as possible, you'll also see the same names for objects, variables, etc. used across the languages for each example.

Step-by-step walkthrough
Let's take a closer look at that code, piece by piece. For now, all we're trying to do is get a basic understanding of the 
types of things we need to do to create a user interface in Tk and roughly what those things look like. We'll go into 
details later.

Incorporating Tk
Our program starts by incorporating Tk.

from tkinter import *
from tkinter import ttk
These two lines tell Python that our program needs two modules. The first, tkinter, is the standard binding to Tk. When 
imported, it loads the Tk library on your system. The second, ttk, is a submodule of tkinter. It implements Python's 
binding to the newer "themed widgets" that were added to Tk in 8.5.

Notice that we've imported everything (*) from the tkinter module. That way, we can call tkinter functions without 
prefixing them with the module name. This is common Tkinter practice.

However, because we've imported just ttk itself, we'll need to prefix anything inside that submodule. For example, calling 
Entry(...) would refer to the Entry class inside the tkinter module (classic widgets). We'd need ttk.Entry(...) to use the 
Entry class inside ttk (themed widgets).

As you'll see, several classes with the same name are defined in both modules. Sometimes you will need one or the other, 
depending on the context. Explicitly requiring the ttk prefix facilitates this and will be the style used in this tutorial.

package require Tk
First thing we do is tell Tcl that our program needs Tk. Though not strictly necessary, it's considered good form to 
include this line. It can also be used to specify exactly what version of Tk is needed.

require 'tk'
require 'tkextlib/tile'
These two lines tell Ruby that our program needs two packages. The first, tk, is the Ruby binding to Tk, which, when 
loaded, also causes the existing Tk library on your system to be loaded. The second, tkextlib/tile, is Ruby Tk's binding to 
the newer "themed widgets" that were added to Tk in 8.5.

The themed widget set evolved out of an earlier Tk add-on called Tile, hence the nomenclature. Despite that, the 
Tk::Tile::* calls you'll see in the programs are actually using the proper ttk versions in 8.5. Expect this to get better 
rationalized in the future.

use Tkx;
The first thing that we need to do is tell Perl to load the "Tkx" module, which provides the Perl interface to Tk that we 
are using.

As mentioned here, there are other Perl bindings to Tk. However, we very strongly recommend using Tkx for development, and 
that will be the only binding we will be describing here. Tkx has the advantage of being a very thin layer above Tk's 
native Tcl API, which means that in almost all cases it automatically tracks the latest changes to Tk (something which 
became a considerable issue with Perl/Tk, which was extremely popular in earlier years, but has not been recently updated). 
As well, by avoiding introducing another layer of code, API errors are reduced, and we can also take advantage of available 
reference documentation for Tk (which is usually Tcl oriented).

If you set the global variable $Tkx::TRACE to any true value, Tkx will print to stderr all calls into Tcl of the translated 
Tkx commands. This is very useful for debugging.

Setting up the main application window
Next, the following code sets up the main application window, giving it the title "Feet to Meters."

root = Tk()
root.title("Feet to Meters")
Yes, the calculate function appeared before this. We'll describe it below but need to include it near the start because we 
reference it in other parts of the program.

wm title . "Feet to Meters"
root = TkRoot.new {title "Feet to Meters"}
Tkx::wm_title(".", "Feet to Meters");
Creating a content frame
Next, we create a frame widget, which will hold the contents of our user interface.

When we create a widget, we need to specify its parent. That is the widget that the new widget will be placed inside. In 
this case, our content frame's parent is the main application window.In Tcl and Perl, the widget name is used to specify 
the parent-child relationship, i.e. .c.feet is a child of .c. In Python and Ruby, the parent is passed as the first 
parameter when instantiating a widget object.

When creating widgets, we can optionally pass additional parameters to override the defaults of the widget's configuration 
options. Here, we're changing the padding inside the content frame widget (three pixels at the left and top, 12 pixels at 
the right and bottom).

mainframe = ttk.Frame(root, padding=(3, 3, 12, 12))
ttk::frame .c -padding "3 3 12 12"
content = Tk::Tile::Frame.new(root) {padding "3 3 12 12"}
Tkx::ttk__frame(".c",  -padding => "3 3 12 12");
Inserting the frame into the user interface
After the frame is created, grid places it directly inside our main application window. We'll discuss its parameters 
shortly.

mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
grid .c -column 0 -row 0 -sticky nwes
content.grid(:sticky => 'nsew')
Tkx::grid( ".c", -column => 0, -row => 0, -sticky => "nwes");
Why do we put a frame inside the main window? Strictly speaking, we could just put the other widgets in our interface 
directly into the main application window without the intervening content frame. That's what you'll see in older Tk 
programs.

However, the main window isn't itself part of the newer "themed" widgets. Its background color may not match the themed 
widgets we will put inside it. Using a "themed" frame widget to hold the content ensures that the background is correct. 
This is illustrated below.

screen shot
Placing a themed frame inside a window.

While the visual discrepancy is no longer as pronounced as indicated in the screenshot (taken with an older version of Tk 
on macOS), it's still good practice to use this inner frame rather than inserting widgets directly into the toplevel 
application window.

Creating the entry widget
The first functional widget we'll create is the entry. This is where the user can type in the number of feet to convert to 
meters.

feet = StringVar()
feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=(W, E))
grid [ttk::entry .c.feet -width 7 -textvariable feet] -column 2 -row 1 -sticky we
$feet = TkVariable.new; 
f = Tk::Tile::Entry.new(content) {width 7; textvariable $feet}.grid( :column => 2, :row => 1, :sticky => 'we' )
Tkx::ttk__entry(".c.feet", -width => 7, -textvariable => \$feet);
Tkx::grid(".c.feet", -column => 2, -row => 1, -sticky => "we");
We need to do two things: create the widget itself and then place it onscreen.

As before, when we create a widget, we need to specify its parent. In this case, we want our entry placed inside the 
content frame and not the main application window. Our entry, and other widgets we'll create shortly, are said to be 
children of the content frame.

When we create a widget, we may override the defaults for certain configuration options. Here, we specify how wide we want 
the entry to appear, i.e., 7 characters. We also assign it a mysterious textvariable; we'll see what that does shortly.

When widgets are created, they don't automatically appear on the screen; Tk doesn't know where you want them placed 
relative to other widgets. That's what the grid part does. Remember the 3x3 layout grid when we sketched out our 
application? Widgets are placed in the appropriate column (1, 2, or 3) and row (also 1, 2, or 3).

Column numbers increase from left to right. Row numbers increase from top to bottom. You can choose arbitrary row or column 
numbers (0, 1, 2, ...) and they don't have to be contiguous. Here we chose to use row (and column) 1, 2, 3 but we could 
have equally used, e.g., 0, 10, 99.

The sticky option to grid describes how the widget should line up within the grid cell, using compass directions. So w 
(west) means to anchor the widget to the left side of the cell, we (west-east) means to attach it to both the left and 
right sides, and so on.

Python defines constants for these directional strings, i.e., N, S, W, E, as well as for common combinations: NW, SW, NE, 
SE, NS, EW, and NSEW, as well as center. You can also specify them as tuples, e.g., (W, E) or as lists, e.g., [W, E]. Your 
program can choose to use literal strings, constants, or lists and tuples of either, in any combination.
Creating the remaining widgets
We then do exactly the same thing for the remaining widgets. We have one label that will display the resulting number of 
meters that we calculate. We have a "Calculate" button that is pressed to perform the calculation. Finally, we have three 
static text labels to make it clear how to use the application. For each of these widgets, we first create it and then 
place it onscreen in the appropriate cell in the grid.

meters = StringVar()
ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))

ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)
grid [ttk::label .c.meters -textvariable meters] -column 2 -row 2 -sticky we
grid [ttk::button .c.calc -text "Calculate" -command calculate] -column 3 -row 3 -sticky w

grid [ttk::label .c.flbl -text "feet"] -column 3 -row 1 -sticky w
grid [ttk::label .c.islbl -text "is equivalent to"] -column 1 -row 2 -sticky e
grid [ttk::label .c.mlbl -text "meters"] -column 3 -row 2 -sticky w
$meters = TkVariable.new
Tk::Tile::Label.new(content) {textvariable $meters}.grid( :column => 2, :row => 2, :sticky => 'we');
Tk::Tile::Button.new(content) {text 'Calculate'; command {calculate}}.grid( :column => 3, :row => 3, :sticky => 'w')

Tk::Tile::Label.new(content) {text 'feet'}.grid( :column => 3, :row => 1, :sticky => 'w')
Tk::Tile::Label.new(content) {text 'is equivalent to'}.grid( :column => 1, :row => 2, :sticky => 'e')
Tk::Tile::Label.new(content) {text 'meters'}.grid( :column => 3, :row => 2, :sticky => 'w')
Tkx::ttk__label(".c.meters", -textvariable => \$meters);
Tkx::grid(".c.meters", -column => 2, -row => 2, -sticky => "we");
Tkx::ttk__button(".c.calc", -text => "Calculate", -command => sub {calculate();});
Tkx::grid(".c.calc", -column => 3, -row => 3, -sticky => "w");

Tkx::grid( Tkx::ttk__label(".c.flbl", -text => "feet"), -column => 3, -row => 1, -sticky => "w");
Tkx::grid( Tkx::ttk__label(".c.islbl", -text => "is equivalent to"), -column => 1, -row => 2, -sticky => "e");
Tkx::grid( Tkx::ttk__label(".c.mlbl", -text => "meters"), -column => 3, -row => 2, -sticky => "w");
Adding some polish
We then put a few finishing touches on our user interface.

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)	
mainframe.columnconfigure(2, weight=1)
for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)
feet_entry.focus()
root.bind("<Return>", calculate)
grid columnconfigure . 0 -weight 1; grid rowconfigure . 0 -weight 1
grid columnconfigure .c -weight 1
foreach w [winfo children .c] {grid configure $w -padx 5 -pady 5}
focus .c.feet
bind . <Return> {calculate}
TkGrid.columnconfigure root, 0, :weight => 1; TkGrid.rowconfigure root, 0, :weight => 1
TkGrid.columnconfigure content, 2, :weight => 1
TkWinfo.children(content).each {|w| TkGrid.configure w, :padx => 5, :pady => 5}
f.focus
root.bind("Return") {calculate}
Tkx::grid_columnconfigure( ".", 0, -weight => 1); 
Tkx::grid_rowconfigure(".", 0, -weight => 1);
Tkx::grid_columnconfigure(".c", 2, -weight => 1);
foreach (Tkx::SplitList(Tkx::winfo_children(".c"))) { Tkx::grid_configure($_, -padx => 5, -pady => 5); }
Tkx::focus(".c.feet");
Tkx::bind(".", "<Return>", sub {calculate();});
The columnconfigure/rowconfigure bits tell Tk that the content frame should expand to fill any extra space if the window is 
resized and that the column in the content frame containing the entry should expand horizontally to fill any extra space.

The next part walks through all of the widgets contained within our content frame and adds a little bit of padding around 
each so they aren't so scrunched together. (We could have added these options to each grid call when we first put the 
widgets onscreen, but this is a nice shortcut.)

The third part tells Tk to put the focus on our entry widget. That way, the cursor will start in that field, so users don't 
have to click on it before starting to type.

The final line tells Tk that if a user presses the Return key (Enter on Windows), it should call our calculate routine, the 
same as if they pressed the Calculate button.

Performing the calculation
Speaking of which, here we define our calculate procedure. It's called when a user presses the Calculate button or hits the 
Return key. It performs the feet to meters calculation.

def calculate(*args):
    try:
        value = float(feet.get())
        meters.set(round(0.3048 * value, 4))
    except ValueError:
        pass
proc calculate {} {  
   if {[catch {
       set ::meters [expr {round($::feet*0.3048*10000.0)/10000.0}]
   }]!=0} {
       set ::meters ""
   }
}
def calculate
  begin
     $meters.value = (0.3048*$feet*10000.0).round()/10000.0
  rescue
     $meters.value = ''
  end
end
sub calculate {
   $meters = int(0.3048*$feet*10000.0+.5)/10000.0 || '';
}
As you can clearly see, this routine takes the number of feet from our entry widget, does the calculation, and places the 
result in our label widget.

Say what? It doesn't look like we're doing anything with those widgets! Here's where the magic textvariable options we 
specified when creating the widgets come into play. We specified the global variable feet as the textvariable for the 
entry. Whenever the entry changes, Tk will automatically update the global variable feet. Similarly, if we explicitly 
change the value of a textvariable associated with a widget (as we're doing for meters which is attached to our label), the 
widget will automatically be updated with the current contents of the variable. Slick.

For Python, the only caveat is that these variables must be an instance of the StringVar class. They can't be a regular 
Python variable.

The multiplying and dividing by 10000.0 in the Tcl, Ruby, and Perl code is to avoid the rounding problems inherent in 
floating-point math. A simple calculation, e.g., 0.3048*1.5, could result in a number like 0.45720000000000005, which would 
neither be correct or visually appealing when displayed. There are other ways to do this, of course, such as the optional 
precision parameter of the round function we used in the Python code.

Start the event loop
Finally, we need to tell Tk to enter its event loop, which is necessary for everything to appear onscreen and allow users 
to interact with it.

The event loop will run for the duration of our application. It handles making sure all our widgets appear, respond to 
changes, and allows the user to interact with them. No matter how many widgets you create and grid, nothing will show u on 
the screen until the event loop starts. When you're typing commands interactively into an interpreter, there's some 
trickery going on behind the scenes so that an event loop starts running immediately.

root.mainloop()
vwait forever
We actually don't need to explicitly provide this (most of the time), as wish will automatically enter the event loop after 
it's read your script.

Tk.mainloop
Tkx::MainLoop();
What's missing?
We've now seen how to create widgets, put them onscreen, and respond to users interacting with them. It's certainly not 
fancy, could probably do with some error checking, but it's a fully functional GUI application.

It's also worth examining what we didn't have to include in our Tk program to make it work. For example:

we didn't have to worry about redrawing the screen as things changed
we didn't have to worry about parsing and dispatching events, hit detection, or handling events on each widget
we didn't have to provide a lot of options when we created widgets; the defaults seemed to take care of most things, and so 
we only had to change things like the text the button displayed
we didn't have to write complex code to get and set the values of simple widgets; we just attached them to variables
we didn't have to worry about what happens when users close the window or resizes it
we didn't need to write extra code to get this all to work cross-platform
One more thing...
As this tutorial emphasizes Tkinter, our examples use standalone script code, global variables, and simple functions. In 
practice, you'll likely organize anything beyond the simplest scripts in functions or classes. There are different ways to 
do this: using modules, creating classes for different parts of the user interface, inheriting from Tkinter classes, etc.

Often though, you just want to do something simple to encapsulate your data rather than putting everything into the global 
variable space. Here is the feet to meters example, rewritten to encapsulate the main code into a class. Note the use of 
self on callbacks (which execute at the global scope) and StringVar's.

from tkinter import *
from tkinter import ttk

class FeetToMeters:

    def __init__(self, root):

        root.title("Feet to Meters")

        mainframe = ttk.Frame(root, padding=(3, 3, 12, 12))
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
       
        self.feet = StringVar()
        feet_entry = ttk.Entry(mainframe, width=7, textvariable=self.feet)
        feet_entry.grid(column=2, row=1, sticky=(W, E))
        self.meters = StringVar()

        ttk.Label(mainframe, textvariable=self.meters).grid(column=2, row=2, sticky=(W, E))
        ttk.Button(mainframe, text="Calculate", command=self.calculate).grid(column=3, row=3, sticky=W)

        ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
        ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
        ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        mainframe.columnconfigure(2, weight=1)
        for child in mainframe.winfo_children(): 
            child.grid_configure(padx=5, pady=5)

        feet_entry.focus()
        root.bind("<Return>", self.calculate)
        
    def calculate(self, *args):
        try:
            value = float(self.feet.get())
            self.meters.set(round(0.3048 * value, 4))
        except ValueError:
            pass

root = Tk()
FeetToMeters(root)
root.mainloop()


