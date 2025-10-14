Tk Concepts
===========

With your first example behind you, you now have a basic idea of what a Tk program looks like and the type of code you need 
to write to make it work. This chapter will step back and look at three broad concepts required to understand Tk: widgets, 
geometry management, and event handling.


Widgets
Widgets are all the things that you see onscreen. Our example had a button, an entry, a few labels, and a frame. 
Checkboxes, tree views, scrollbars, and text areas are examples of other widgets. Widgets are often referred to as 
"controls." You'll also sometimes see them referred to as "windows," particularly in Tk's documentation. This is a holdover 
from its X11 roots (under that terminology, both your toplevel application window and a button would be called windows).

Here are just a few of Tk's widgets, which we'll cover individually shortly.

screen shot
Several Tk Widgets.

Widget classes
In Tk, individual widgets are objects, instances of classes that represent buttons, frames, and so on. To create a widget, 
you first need to identify the specific class of the widget you'd like to instantiate. We'll explore these in the coming 
chapters.

Widget hierarchy
Besides the widget class, you need one other piece of information before you can create a widget: its parent. Widgets don't 
float off in space. Instead, they're contained within something else, like a window. In Tk, all widgets are part of a 
widget (or window) hierarchy, with a single root at the top of the hierarchy.

In our metric conversion example, we created a single frame as a child of the root window, and that frame contained all the 
other widgets as children. The root window was a container for the frame and was, therefore, the frame's parent. The 
complete hierarchy for the example looked like this:

screen shot
The widget hierarchy of the metric conversion example.

Widget hierarchies can be arbitrarily deep. For example, you might have a button in a frame in another frame within the 
root window. Even a new window in your application (a special widget called a toplevel) is part of that same hierarchy. 
That window and all its contents form a subtree of the overall widget hierarchy.

screen shot
Hierarchy of a more substantial application. Leaf nodes (buttons, labels, etc.) omitted.

Creating widgets
Each separate widget is a Python object. When instantiating a widget, you pass its parent as the first parameter to the 
widget class. The only exception is the "root" window. That toplevel window is automatically created when you instantiate 
Tk. It does not have a parent. For example:

root = Tk()
content = ttk.Frame(root)
button = ttk.Button(content)
Whether or not you save the widget object in a variable is entirely up to you, depending on whether you'll need to refer to 
it later. Because the widget object is inserted into the widget hierarchy, it won't be garbage collected even if you don't 
keep your own reference to it.

Tkinter is a wrapper around the Tcl language interface to Tk. When you create a widget object in Tkinter, you're running a 
small bit of Tcl code. Sometimes when you're trying to figure out exactly how to make Tkinter do what you want, you may 
need to look at Tk's reference documentation, which is Tcl-based.

In Tcl, rather than widget objects, every widget is uniquely identified with a hierarchical path name. For example, '.' (a 
single dot) is the path name of the root window, '.content' is a widget that is a child of the root window, '.content.feet' 
might be an entry widget within that, and so on. You'll see this pathname referred to in Tk reference documentation. 
Tkinter chooses and manages all these pathnames for you behind the scenes, so you should never have to worry about them. If 
you do, you can get the pathname from a widget by calling str(widget).

In Tcl, each widget is given an explicit pathname, which both differentiates it from other widgets, and also indicates its 
place in the window hierarchy. The root of the hierarchy, the toplevel widget that Tk automatically creates, is named 
simply . (dot).

The frame, which was a child of the root, was named .c. We could have put pretty much anything in place of the "c", naming 
it for example .content. This name is purely for use by your program, so it's best to choose something meaningful. The 
controls that were children of the frame were given names like .c.feet, .c.meters, .c.flbl, and so on. If there were any 
widgets at a deeper level of the hierarchy, we'd add another . and then a unique identifier.

So to create a widget, we need to provide the widget class, and the pathname. The pathname is used to indicate the widget's 
parent (which must of course exist also), and hence its position in the window hierarchy. For example:

ttk::button .b
ttk::frame .f
ttk::entry .f.entry
This also creates a new object command with the same name as the widget's pathname, which will let us communicate with the 
widget. So the above code would produce new Tcl commands named .b, .f, .f.entry, and so on. You can then use that object 
command to communicate further with the widget, calling e.g. .b invoke, or .f.entry state disabled. Because of the obvious 
parallels with many object-oriented systems, we'll often refer to the object commands as objects, and calls on those 
objects (like the invoke) as method calls. For example, we'll see below the use of the configure and cget methods.

Speaking of which, Tcl uses a more shell-like syntax than the other languages covered in this tutorial, with spaces 
separating parameters rather than commas or other delimeters. Some procedure or method names that are written as multiple 
words in Tcl (e.g., selection clear) are implemented as a single identifier in most other Tk language bindings (e.g. 
selection_clear). We'll generally use the latter notation when referring to these methods in the text, while 
language-specific notation is used in accompanying code snippets.

Each separate widget is a Ruby object. When creating a widget, you must pass its parent as a parameter to the widget class' 
new method. The only exception is the "root" window, which is the toplevel window that will contain everything else. That 
is instantiated from the TkRoot class, and it does not have a parent. For example:

root = TkRoot.new 
content = Tk::Tile::Frame.new(root)
Tk::Tile::Button.new(content)
Whether or not you save the widget object in a variable is entirely up to you, and depends of course whether you'll need to 
refer to it later. Because the object is inserted into the widget hierarchy, it won't be garbage collected even if you 
don't keep your own reference to it.

If you sneak a peek at how Tcl manages widgets, you'll see each widget has a specific pathname; you'll also see this 
pathname referred to in Tk reference documentation. Ruby/Tk chooses and manages all these pathnames for you behind the 
scenes, so you should never have to worry about them. If you do though, you can get the pathname from a widget with its 
path method.

In Perl, each widget is given an explicit pathname, which both differentiates it from other widgets, and also indicates its 
place in the window hierarchy. The root of the hierarchy, the toplevel widget that Tk automatically creates, is named 
simply . (dot).

The frame, which was a child of the root, was named .c. We could have put pretty much anything in place of the "c", naming 
it for example .content. This name is purely for use by your program, so it's best to choose something meaningful. The 
controls that were children of the frame were given names like .c.feet, .c.meters, .c.flbl, and so on. If there were any 
widgets at a deeper level of the hierarchy, we'd add another . and then a unique identifier.

So to create a widget, we need to provide the widget class, and the pathname. The pathname is used to indicate the widget's 
parent (which must of course exist also), and hence its position in the window hierarchy. For example:

Tkx::ttk__button(".b", -text => "hello");
Tkx::ttk__frame(".f");
Tkx::ttk__entry(".f.entry");
Widget Objects
Many widgets have operations that you can call on them, such as to disable a widget, invoke a button's command, and so on. 
If we were doing this in Tcl, we'd write something like .b invoke or .f.entry state disabled. Essentially you'd think of 
".b" or ".f.entry" as objects, and "invoke" and "state" as methods, the latter having a single parameter "disabled". In 
Perl, you can call the exact Tcl command like this:

Tkx::i::call(".b", "invoke");
Tkx::i::call(".f.entry", "state", "disabled");
Admittedly, that's pretty lame. Ideally, we'd want to have these widgets behave just like Perl objects. Luckily, Tkx lets 
us do exactly that.

The first thing we need to do is get a reference to an object for these widgets. We can do that like this, passing the 
widget pathname to Tkx::widget->new:

my $b = Tkx::widget->new(".b");
my $e = Tkx::widget->new(".f.entry");
Then we can invoke methods on these objects just how you'd expect:

$b->invoke;
$e->state("disabled");
Creating each widget and then getting a reference to it as a separate step is a bit much. So there's another way to create 
widgets. If you have an object reference to the parent widget in the widget hierarchy, you can ask it to create a child.

my $mw = Tkx::widget->new(".");
my $b = $mw->new_ttk__button(-text => "hello");
my $f = $mw->new_ttk__frame;
my $e = $f->new_ttk__entry;
In this case, Tkx will choose the widget pathname for you (it'll look something like ".b", ".f.e", ".f.e2", etc.).

You can get this path by calling the object's "_mpath" method (e.g. $b->_mpath). If you stringify the object itself (e.g. 
trying to print it out), it will also be the widget pathname.

You also saw in our earlier example that some Tkx commands (like "grid") take the widget pathname as their first argument. 
There's a way to do that using the widget object instead. We invoke a method which is the name of the command, prefixed by 
"g_", e.g. "g_grid". So this:

Tkx::ttk__entry(".c.feet", -width => 7, -textvariable => \$feet);
Tkx::grid(".c.feet", -column => 2, -row => 1, -sticky => "we");
becomes this:

my $mw = Tkx::widget->new(".");
my $ft = $mw->new_ttk__entry(-width => 7, -textvariable => \$feet);
$ft->g_grid(-column => 2, -row => 1, -sticky => "we");
Translation Rules
What's somewhat scary about the Tkx module is that it implements all of this on a purely syntactic level. That is, it has 
no clue about buttons and entries and grid. It just knows that if it sees a method "new_something" it's creating a widget 
using the Tcl command "something", or if you call a method "g_otherthing", that it's going to invoke a Tcl command 
"otherthing", and pass the widget pathname associated with the object as a first parameter (followed by any other 
parameters passed to the method).

It's this pure syntactic mapping which gives Tkx its power and amazing brevity (check out the code in Tkx.pm!). It also 
explains why it can automatically track any changes in Tk. Any new commands and options don't need to be explicitly 
implemented in Tkx code; they are automatically available just by using the right syntax.

Now let's talk about those underscores in the Tkx commands and method names. If you've glanced at the Tcl version of the 
code in this tutorial, you know that they can take several forms, i.e.

a single toplevel command, like grid
a multi-word command (called an ensemble in Tcl), e.g. wm title
a command in a namespace, e.g. ttk::button
a single toplevel command with underscores, e.g. tk_messageBox
No translations are needed for simple commands like "grid", but the others need to be tweaked. To translate these into 
Perl, Tkx uses underscores in the following way:

a single underscore is replaced with a space, e.g. wm_title in Perl becomes wm title in Tcl
two underscores is replaced with the namespace qualifier "::", e.g. ttk__button becomes ttk::button
three underscores is replaced with a single underscore, e.g. tk___messageBox becomes tk_messageBox
Given that this purely syntactic translation is all that Tkx does, let's state the obvious: whether or not you use the pure 
command form, which we used in the "feet to meters" example, or the object oriented form, they both do exactly the same 
thing (i.e. invoke the same underlying Tcl command).

Because you can get an object's widget pathname, or get an object reference from a widget pathname, you can also freely 
intermix them. Most programs of any length will probably be a bit simpler if they predominately use the object oriented 
form, but this is almost entirely a stylistic issue.

Feet to Meters, Object Style
Here's the earlier "feet to meters" example, this time rewritten in the object oriented style. The programs do exactly the 
same thing.

use Tkx;

my $mw = Tkx::widget->new(".");
$mw->g_wm_title("Feet to Meters");
my $frm = $mw->new_ttk__frame(-padding => "3 3 12 12");
$frm->g_grid(-column => 0, -row => 0, -sticky => "nwes");
$mw->g_grid_columnconfigure(0, -weight => 1);
$mw->g_grid_rowconfigure(0, -weight => 1);

my $ef = $frm->new_ttk__entry(-width => 7, -textvariable => \$feet);
$ef->g_grid(-column => 2, -row => 1, -sticky => "we");
my $em = $frm->new_ttk__label(-textvariable => \$meters);
$em->g_grid(-column => 2, -row => 2, -sticky => "we");
my $cb = $frm->new_ttk__button(-text => "Calculate", -command => sub {calculate();});
$cb->g_grid(-column => 3, -row => 3, -sticky => "w");

$frm->new_ttk__label(-text => "feet")->g_grid(-column => 3, -row => 1, -sticky => "w");
$frm->new_ttk__label(-text => "is equivalent to")->g_grid(-column => 1, -row => 2, -sticky => "e");
$frm->new_ttk__label(-text => "meters")->g_grid(-column => 3, -row => 2, -sticky => "w");

foreach (Tkx::SplitList($frm->g_winfo_children)) {
    Tkx::grid_configure($_, -padx => 5, -pady => 5);
}
$ef->g_focus;
$mw->g_bind("<Return>", sub {calculate();});

sub calculate {
   $meters = int(0.3048*$feet*10000.0+.5)/10000.0 || '';
}

Tkx::MainLoop();
Configuration options
All widgets have multiple configuration options that control how the widget is displayed or how it behaves.

The available options for a widget depend upon the widget class, of course. There is a lot of consistency between different 
widget classes, so options that do similar things tend to be named the same. For example, both a button and a label have a 
text option to adjust the text displayed by the widget, while a scrollbar would not have a text option since it's not 
needed. A button has a command option telling it what to do when pushed, while a label, which holds just static text, does 
not.

While widgets may have many configuration options, they have sensible defaults. In practice, each widget has only a few 
configuration options that are commonly used. As we describe different widgets, we'll focus on those. While reference 
documentation will describe all the options, it can be difficult to find the few you actually need.

Configuration options can be set when the widget is first created by specifying their names and values as optional 
parameters. Later, you can retrieve the current values of those options, and with a tiny number of exceptions, change them 
at any time.

If you're unsure what configuration options a widget supports, you can ask the widget to describe them. This gives you a 
long list of all its options.

This is all best illustrated with the following interactive dialog with the interpreter.

% python
>>> from tkinter import *
>>> from tkinter import ttk
>>> root = Tk()

# create a button, passing two options:
>>> button = ttk.Button(root, text="Hello", command="buttonpressed")
>>> button.grid()

#check the current value of the text option:
>>> button['text']
'Hello'

# change the value of the text option:
>>> button['text'] = 'goodbye'

# another way to do the same thing:
>>> button.configure(text='goodbye')

# check the current value of the text option:
>>> button['text']
'goodbye'

# get all information about the text option:
>>> button.configure('text')
('text', 'text', 'Text', '', 'goodbye')

# get information on all options for this widget:
>>> button.configure()
{'cursor': ('cursor', 'cursor', 'Cursor', '', ''), 'style': ('style', 'style', 'Style', '', ''), 
'default': ('default', 'default', 'Default', <index object at 0x00DFFD10>, <index object at 0x00DFFD10>), 
'text': ('text', 'text', 'Text', '', 'goodbye'), 'image': ('image', 'image', 'Image', '', ''), 
'class': ('class', '', '', '', ''), 'padding': ('padding', 'padding', 'Pad', '', ''), 
'width': ('width', 'width', 'Width', '', ''), 
'state': ('state', 'state', 'State', <index object at 0x0167FA20>, <index object at 0x0167FA20>), 
'command': ('command', 'command' , 'Command', '', 'buttonpressed'), 
'textvariable': ('textvariable', 'textVariable', 'Variable', '', ''), 
'compound': ('compound', 'compound', 'Compound', <index object at 0x0167FA08>, <index object at 0x0167FA08>), 
'underline': ('underline', 'underline', 'Underline', -1, -1), 
'takefocus': ('takefocus', 'takeFocus', 'TakeFocus', '', 'ttk::takefocus')}
% wish8.5
create a button, passing two options:
% grid [ttk::button .b -text "Hello" -command {button_pressed}]
check the current value of the text option:
% .b cget -text
Hello
check the current value of the command option:
% .b cget -command
button_pressed
change the value of the text option:
% .b configure -text Goodbye
check the current value of the text option:
% .b cget -text
Goodbye
get all information about the text option:
% .b configure -text
-text text Text {} Goodbye
get information on all options for this widget:
% .b configure
{-takefocus takeFocus TakeFocus ttk::takefocus ttk::takefocus} 
{-command command Command {} button_pressed} {-default default Default normal normal} 
{-text text Text {} Goodbye} {-textvariable textVariable Variable {} {}} 
{-underline underline Underline -1 -1} {-width width Width {} {}} {-image image Image {} {}} 
{-compound compound Compound none none} {-padding padding Pad {} {}} 
{-state state State normal normal} {-takefocus takeFocus TakeFocus {} ttk::takefocus} 
{-cursor cursor Cursor {} {}} {-style style Style {} {}} {-class {} {} {} {}}
% irb
irb(main):001:0> require 'tk'
=> true
irb(main):002:0> require 'tkextlib/tile'
=> true
create a button, passing two options:
irb(main):003:0> root = TkRoot.new
=> #<TkRoot:0xb7c8c9d8 @path=".">
irb(main):004:0> button = Tk::Tile::Button.new(root) {text "Hello"; command "button_pressed"}.grid
=> #<Tk::Tile::TButton:0xb7c86ab0 @cmdtbl=["c00001"], @path=".w00000">
check the current value of the text option:
irb(main):005:0> button['text']
=> "Hello"
check the current value of the command option:
irb(main):006:0> button['command']
=> #<cb_entry:fdbe42342>
change the value of the text option:
irb(main):007:0> button['text'] = 'goodbye'
=> "goodbye"
check the current value of the text option:
irb(main):008:0> button['text']
=> "goodbye"
get all information about the text option:
irb(main):009:0> button.configinfo 'text'
=> ["text", "text", "Text", "", "goodbye"]
get information on all options for this widget:
irb(main):010:0> button.configinfo
=> [["takefocus", "takeFocus", "TakeFocus", true, true], ["command", "command", "Command", "", #<cb_entry:fdbe42342>], 
["default", "default", "Default", "normal", "normal"], ["text", "text", "Text", "", "goodbye"],
 ["textvariable", "textVariable", "Variable", nil, nil], 
["underline", "underline", "Underline", -1, -1], ["width", "width", "Width", "", ""], 
["image", "image", "Image", "", ""], ["compound", "compound", "Compound", "none", "none"], 
["padding", "padding", "Pad", "", ""], ["state", "state", "State", "normal", "normal"], 
["takefocus", "takeFocus", "TakeFocus", nil, true], ["cursor", "cursor", "Cursor", "", ""], 
["style", "style", "Style", [], []], ["class", "", "", "", ""]]
run Perl interactively using the program "psh":
% psh
Perl> use Tkx
Perl> $mw = Tkx::widget->new(".")
.
create a button, passing two options:
Perl> ($b = $mw->new_ttk__button(-text => "Hello", -command => sub {button_pressed();}))->g_grid
.b
check the current value of the text option:
  (note that "m_<foo>" is another one of those magic Tkx translations 
   like "g_<foo>"; in this case it means call the <foo> method on the object)
Perl> $b->m_cget(-text)
Hello
conveniently, the "m_" part is almost always optional:
Perl> $b->cget(-text)
Hello
check the current value of the command option:
Perl> $b->cget(-command)
::perl::CODE(0x839020)
change the value of the text option:
Perl> $b->configure(-text => "Goodbye")

check the current value of the text option:
Perl> $b->cget(-text)
Goodbye
get all information about the text option:
Perl> $b->configure(-text)
-text text Text {} Goodbye
convert the Tcl list this returns into a Perl list:
Perl> Tkx::SplitList($b->configure(-text))
-text, text, Text, , Goodbye
get information on all options for this widget:
Perl> $b->configure
{-takefocus takeFocus TakeFocus ttk::takefocus ttk::takefocus} 
{-command command Command {} ::perl::CODE(0x839020)} {-default default Default normal normal} 
{-text text Text {} Goodbye} {-textvariable textVariable Variable {} {}} 
{-underline underline Underline -1 -1} {-width width Width {} {}} {-image image Image {} {}} 
{-compound compound Compound none none} {-padding padding Pad {} {}} 
{-state state State normal normal} {-takefocus takeFocus TakeFocus {} ttk::takefocus} 
{-cursor cursor Cursor {} {}} {-style style Style {} {}} {-class {} {} {} {}}
As you can see, for each option, Tk will show you the name of the option and its current value (along with three other 
attributes which you can usually ignore).

Ok, if you really want to know, here are the details on the five pieces of data provided for each configuration option. The 
most useful are the first, the option's name, and the fifth, which is the option's current value. The fourth is the default 
value of the option, or in other words, the value it would have if you didn't change it. The other two relate to something 
called the option database. We'll briefly touch on it when we discuss menus, but it's not used in modern applications. The 
second item is the option's name in the database, and the third is its class.

Styles and themes
Tk's "classic" widgets each have a very large number of configuration options, providing for very precise control over 
numerous details of each individual widget's appearance. The need to customize each individual widget often resulted in a 
great deal of repetitive code and inconsistencies.

Tk's "themed" widgets move most of these details into theme and style objects, separate from the widget itself. This makes 
it far easier to create consistent user interfaces while using much less code to do it.

Styles and themes are covered in detail towards the end of the book. It explains the benefits.

So why use styles and themes in Tk? They take the fine-grained details of appearance decisions away from individual 
instances of widgets.

That makes for cleaner code and less repetition. If you have 20 entry widgets in your application, you don't need to repeat 
the exact appearance details every time you create one (or write a wrapper function). Instead, you assign them a style.

Themes collect a series of styles, putting all appearance decisions in one place. And because styles for a button and 
styles for other widgets can share common elements, collecting them in themes promotes consistency and improves reuse.

Changing themes allows for radical customization of your application's appearance. For most mainstream desktop 
applications, it's unlikely you will need to do so. However, you'll see in the next chapter how individual styles can be 
applied to widgets in lieu of making fine-grained changes to individual widgets.

These very different approaches to customization between classic and themed widgets are the main reason both sets of 
widgets exist today. It would not have been feasible to add support for themes while still maintaining backward 
compatibility.

Widget introspection
Tk exposes a treasure trove of information about each and every widget that your application can take advantage of. Much of 
it is available via the winfo facility; see the winfo command reference for full details.

This short example traverses the widget hierarchy, using each widget's winfo_children method to identify child widgets that 
need to be examined. For each widget, we print some basic information, including its class (button, frame, etc.), width, 
height, and position relative to its parent.

def print_hierarchy(w, depth=0):
    print('  '*depth + w.winfo_class() + ' w=' + str(w.winfo_width()) + ' h=' + str(w.winfo_height()) + ' x=' + 
str(w.winfo_x()) + ' y=' + str(w.winfo_y()))
    for i in w.winfo_children():
        print_hierarchy(i, depth+1)

print_hierarchy(root)
proc print_hierarchy {w {depth 0}} {
    puts "[string repeat "  " $depth][winfo class $w] w=[winfo width $w] h=[winfo height $w] x=[winfo x $w] y=[winfo y $w]"
    foreach i [winfo children $w] {
        print_hierarchy $i [expr {$depth+1}]
    }
}
print_hierarchy .
def print_hierarchy(w, depth=0)
    print("  "*depth + w.winfo_class() + ' w=' + w.winfo_width().to_s + ' h=' + w.winfo_height().to_s + ' x=' + 
w.winfo_x().to_s + ' y=' + w.winfo_y().to_s + "\n")
    w.winfo_children().each do |i| 
        print_hierarchy(i, depth+1)
    end
end
print_hierarchy root
sub print_hierarchy {
    my ($w, $depth) = @_;
    $depth //= 0;
    print("  "x$depth, $w->g_winfo_class(), " w=", $w->g_winfo_width(), " h=", $w->g_winfo_height(), " x=", 
$w->g_winfo_x(), " y=", $w->g_winfo_y(), "\n");
    foreach (Tkx::SplitList($w->g_winfo_children())) {
        print_hierarchy(Tkx::widget->new($_), $depth+1);
    }
}
print_hierarchy($mw);
The following are some of the most useful methods:

winfo_class:
a class identifying the type of widget, e.g., TButton for a themed button
winfo_children:
a list of widgets that are the direct children of a widget in the hierarchy
winfo_parent:
parent of the widget in the hierarchy
winfo_toplevel:
the toplevel window containing this widget
winfo_width, winfo_height:
current width and height of the widget; not accurate until it appears onscreen
winfo_reqwidth, winfo_reqheight:
the width and height that the widget requests of the geometry manager (more on this shortly)
winfo_x, winfo_y:
the position of the top-left corner of the widget relative to its parent
winfo_rootx, winfo_rooty:
the position of the top-left corner of the widget relative to the entire screen
winfo_vieweable:
whether the widget is displayed or hidden (all its ancestors in the hierarchy must be viewable for it to be viewable)
Geometry management
As you've seen, widgets don't appear on the screen just by creating them. Placing widgets on the screen (and precisely 
where they are placed) is a separate step called geometry management.

In our feet to meters example, positioning each widget was accomplished by the grid command. We specified the column and 
row where we wanted each widget placed], how things were aligned within the grid, etc. Grid is an example of a geometry 
manager (of which there are several in Tk, grid being the most useful). For now, we'll look at geometry management in 
general; we'll talk about grid in a later chapter.

A geometry manager's job is to figure out exactly where those widgets are going to be put. This turns out to be a complex 
optimization problem, and a good geometry manager relies on quite sophisticated algorithms. A good geometry manager 
provides the flexibility, power, and ease of use that makes programmers happy. It also makes it easy to create appealing 
user interface layouts without needing to jump through hoops. Tk's grid is, without a doubt, one of the absolute best.

We'll go into more detail in a later chapter, but grid was introduced several years after Tk became popular. Before that, 
an older geometry manager named pack was most commonly used. It's equally powerful but much harder to use, making it 
onerous to create layouts that look appealing today. Unfortunately, much of the example Tk code and documentation out there 
uses pack instead of grid (a good clue to how current it is). The widespread use of pack is a leading reason that so many 
Tk user interfaces look terrible. Start new code with grid, and upgrade old code when you can.

The problem
The problem for a geometry manager is to take all the different widgets the program creates, plus the program's 
instructions for where in the window each should go (explicitly, or more often, relative to other widgets), and then 
actually position them in the window.

In doing so, the geometry manager has to balance multiple constraints. Consider these situations:

The widgets may have a natural size, e.g., the natural width of a label would depend on the text it displays and the font 
used to display it. What if the application window containing all these different widgets isn't big enough to accommodate 
them? The geometry manager must decide which widgets to shrink to fit, by how much, etc.
If the application window is bigger than the natural size of all the widgets, how is the extra space used? Is extra space 
placed between each widget, and if so, how is that space distributed? Is it used to make certain widgets larger than they 
usually are, such as a text entry growing to fill a wider window? Which widgets should grow?
If the application window is resized, how does the size and position of each widget inside it change? Will certain areas 
(e.g., a text entry area) expand or shrink while other parts stay the same size, or is the area distributed differently? Do 
certain widgets have a minimum size that you want to avoid going below? A maximum size? Does the window itself have a 
minimum or maximum size?
How can widgets in different parts of the user interface be aligned with each other? How much space should be left between 
them? This is needed to present a clean layout and comply with platform-specific user interface guidelines.
For a complex user interface, which may have many frames nested in other frames nested in the window (etc.), how can all 
the above be accomplished, trading off the conflicting demands of different parts of the entire user interface?
How it works
Geometry management in Tk relies on the concept of master and slave widgets. A master is a widget, typically a toplevel 
application window or a frame. It contains other widgets, called slaves. You can think of a geometry manager taking control 
of the master widget and deciding how all the slave widgets will be displayed within.

The computing community has embraced the more general societal trend towards more diversity, sensitivity, and awareness 
about the impacts of language. As a result, the Tk core will slowly adopt a more inclusive set of terminology. For example, 
where it makes sense, "parent" and "child" will be preferred over "master" and "slave." The current terminology will not 
disappear to preserve backward compatibility. This is something to be aware of for the future. For more details, see TIP 
#581.

Your program tells the geometry manager what slaves to manage within the master, i.e., via calling grid. Your program also 
provides hints as to how it would like each slave to be displayed, e.g., via the column and row options. You can also 
provide other information to the geometry manager. For example, we used columnconfigure and rowconfigure to indicate the 
columns and rows we'd like to expand if extra space is available in the window. Note that all these parameters and hints 
are specific to grid; other geometry managers would use different ones.

The geometry manager collects information about the slaves in the master and the total size of the master. It asks each 
slave widget for its natural size, i.e., how large it would ideally be displayed. The geometry manager's internal algorithm 
calculates the rectangular area each slave will be allocated (if any!). The slave is then responsible for rendering itself 
within that particular rectangle. And of course, we repeat the whole process whenever the size of the master changes (e.g., 
because the toplevel window was resized), the natural size of a slave changes (e.g., because we've changed the text in a 
label), or any geometry manager parameters change (e.g., like row, column, or sticky).

This all works recursively as well. In our example, we had a content frame inside the toplevel application window and then 
several other widgets inside the content frame. We, therefore, had to manage the geometry for two different masters. At the 
outer level, the toplevel window was the master, and the content frame was its slave. At the inner level, the content frame 
was the master, with each of the other widgets being slaves. Notice that the same widget, e.g., the content frame, can be 
both a master and a slave! As we saw previously, this widget hierarchy can be nested much more deeply.

While each master can be managed by only one geometry manager (e.g., grid), different masters can have different geometry 
managers. While grid is the right choice most of the time, others may make sense for a particular layout used in one part 
of your user interface. Other Tk geometry managers include pack, which we've mentioned, and place, which leaves all layout 
decisions entirely up to you. Some complex widgets like canvas and text let you embed other widgets, making them de facto 
geometry managers.

Finally, we've been assuming that slave widgets are the immediate children of their master in the widget hierarchy. While 
this is usually the case, and mostly there's no good reason to do it any other way, it's also possible (with some 
restrictions) to get around this.

Event handling
As with most user interface toolkits, Tk runs an event loop that receives events from the operating system. These are 
things like button presses, keystrokes, mouse movement, window resizing, and so on.

Generally, Tk takes care of managing this event loop for you. It will figure out what widget the event applies to (did a 
user click on this button? if a key was pressed, which textbox had the focus?), and dispatch the event accordingly. 
Individual widgets know how to respond to events; for example, a button might change color when the mouse moves over it and 
revert back when the mouse leaves.

It's critical in event-driven applications that the event loop not be blocked. The event loop runs continuously, normally 
executing dozens of steps per second. At every step, it processes an event. If your program is performing a long operation, 
it can potentially block the event loop. In that case, no events would be processed, no drawing would be done, and it would 
appear as if your application is frozen. There are many ways to prevent this from happening. We'll discuss this in more 
detail in a later chapter.

Command callbacks
You often want your program to handle some event in a particular way, e.g., do something when a button is pushed. For those 
events that are most frequently customized (what good is a button without something happening when you press it?), the 
widget lets you specify a callback via a widget configuration option. We saw this in the example with the command option of 
the button.

def calculate(*args):
    ...

ttk.Button(mainframe, text="Calculate", command=calculate)
proc calculate {} {...}

ttk::button .c.calc -text "Calculate" -command calculate
def calculate
   ...
   
Tk::Tile::Button.new(content) {text 'Calculate'; command {calculate}}
sub calculate {...}

Tkx::ttk__button(".c.calc", -text => "Calculate", -command => sub {calculate();});
Callbacks in Tk tend to be simpler than in user interface toolkits used with compiled languages (where a callback must be a 
procedure with a certain set of parameters or an object method with a certain signature). Instead, the callback is just an 
ordinary bit of code that the interpreter evaluates. While it can be as complicated as you want to make it, most of the 
time, you'll just want your callback to call some other function or method.

Binding to events
For events that don't have a widget-specific callback configuration option associated with them, you can use Tk's bind to 
capture any event and then (like with callbacks) execute an arbitrary piece of code.

Here's a (silly) example showing a label responding to different events. When an event occurs, a description of the event 
is displayed in the label.

from tkinter import *
from tkinter import ttk
root = Tk()
l =ttk.Label(root, text="Starting...")
l.grid()
l.bind('<Enter>', lambda e: l.configure(text='Moved mouse inside'))
l.bind('<Leave>', lambda e: l.configure(text='Moved mouse outside'))
l.bind('<ButtonPress-1>', lambda e: l.configure(text='Clicked left mouse button'))
l.bind('<3>', lambda e: l.configure(text='Clicked third mouse button'))
l.bind('<Double-1>', lambda e: l.configure(text='Double clicked'))
l.bind('<B3-Motion>', lambda e: l.configure(text=f'third button drag to {e.x},{e.y}'))
root.mainloop()
package require Tk
grid [ttk::label .l -text "Starting..."] 
bind .l <Enter> {.l configure -text "Moved mouse inside"}
bind .l <Leave> {.l configure -text "Moved mouse outside"}
bind .l <ButtonPress-1> {.l configure -text "Clicked left mouse button"}
bind .l <3> {.l configure -text "Clicked third mouse button"}
bind .l <Double-1> {.l configure -text "Double clicked"}
bind .l <B3-Motion> {.l configure -text "third button drag to %x %y"}
Note that the bind command lives in the global namespace; there is not a ttk::bind command.

require 'tk'
require 'tkextlib/tile'
root = TkRoot.new
l = Tk::Tile::Label.new(root) {text "Starting..."}.grid
l.bind("Enter") {l['text'] = "Moved mouse inside"}
l.bind("Leave") {l['text'] = "Moved mouse outside"}
l.bind("ButtonPress-1") {l['text'] = "Clicked left mouse button"}
l.bind("3") {l['text'] = "Clicked third mouse button"}
l.bind("Double-1") {l['text'] = "Double clicked"}
l.bind("B3-Motion", proc{|x,y| l['text'] = "third button drag to #{x} #{y}"}, "%x %y")
Tk.mainloop
use Tkx;
my $mw = Tkx::widget->new(".");
(my $l = $mw->new_ttk__label(-text => "Starting..."))->g_grid;
$l->g_bind("<Enter>",     sub {$l->configure(-text => "Moved mouse inside")});
$l->g_bind("<Leave>",     sub {$l->configure(-text => "Moved mouse outside")});
$l->g_bind("<ButtonPress-1>",         sub {$l->configure(-text => "Clicked left mouse button")});
$l->g_bind("<3>",         sub {$l->configure(-text => "Clicked third mouse button")});
$l->g_bind("<Double-1>",  sub {$l->configure(-text => "Double clicked")});
$l->g_bind("<B3-Motion>", [sub { my($x,$y) = @_;
                                 $l->configure(-text => "third button drag to $x $y")
	                   }, Tkx::Ev("%x", "%y")]);
Tkx::MainLoop();
The first two bindings are pretty straightforward, just watching for simple events. An <Enter> event means the mouse has 
moved over top the widget, while the <Leave> event is generated when the mouse moves outside the widget to a different one.

The next binding looks for a mouse click, specifically a <ButtonPress-1> event. Here, the <ButtonPress> is the actual 
event, but the -1 is an event detail specifying the left (main) mouse button on the mouse. The binding will only trigger 
when a <ButtonPress> event is generated involving the main mouse button. If another mouse button was clicked, this binding 
would ignore it.

This next binding looks for a <3> event. This is actually a shorthand for <ButtonPress-3>. It will respond to events 
generated when the third mouse button is clicked. The next binding, <Double-1> (shorthand for <Double-ButtonPress-1>) adds 
another modifier, Double, and so will respond to the left mouse button being double-clicked.

The last binding (<B3-Motion>) also uses a modifier: capture mouse movement (Motion), but only when the third mouse button 
(B3) is held down.

You may have noticed we're being a bit cagey, referring to the "left" mouse button and the "third" mouse button… not the 
"right" mouse button. On Windows and Linux/X11, which have three button mouses, button #1 is the left button and button #3 
is the right button. On macOS, things are different. Sometimes, only a single button mouse is available, in which case 
we'll never get an event for button #3. When a three button mouse is available on macOS, however, the right button is 
actually button #2, not button #3. On macOS, button #3 is the middle button (or scroll wheel button), which is button #2 on 
Windows and Linux/X11. We'll return to this in the chapter on menus.

This last binding also shows an example of how to use event parameters. Many events carry additional information, e.g., the 
position of the mouse when it's clicked. Tk provides access to these parameters in Tcl callback scripts through the use of 
percent substitutions. These percent substitutions let you capture them so they can be used in your script. We'll see 
percent substitutions used later in another context, entry widget validation.

Tkinter abstracts away these percent substitutions and instead encapsulates all the event parameters in an event object. 
Above, we used the x and y fields to retrieve the mouse position.

What's with the lambda expressions? Tkinter expects you to provide a function as the event callback, which is passed an 
event object representing the event that triggered the callback. It's sometimes not worth the bother of defining regular 
named functions for one-off trivial callbacks, such as in this example. But we still need to accept that event object as a 
parameter. Here, we've used Python's anonymous functions via lambda to do just that, ignoring it in all but the last 
binding. In real applications, you'll almost always use a regular function, such as the calculate function in our feet to 
meters example, or a method of an object.

As we've described here, and throughout Tk's documentation, events in Tk are surrounded by angle brackets, e.g. <Enter>. 
The Ruby/Tk authors decided to strip the angle brackets from events in its API, e.g., Enter.

Tkx lets us provide command callbacks as just a Perl function (the first five), or as a two element array (the last case). 
The first element is the Perl code to be called, while the second array element specifies parameters to pass to that code. 
The function Tkx::Ev() will expand its parameter (%x %y in this case) when the callback is invoked, which will perform the 
percent substitutions. These then are passed as parameters to our function.

Multiple bindings for an event
We've just seen how event bindings can be assigned to an individual widget. When a matching event is received by that 
widget, the binding is triggered. But that's not all you can do.

Your binding can capture not only a single event but a short sequence of events. The <Double-1> binding triggers when two 
mouse clicks occur in a short time. You can do the same thing to capture two keys pressed in a row, e.g., 
<KeyPress-a><KeyPress-b> or simply <a><b>.

For keyboard events, case matters. If you want to bind to a capital A, use <KeyPress-A> or <A>.

You can also assign an event binding to a toplevel window. When a matching event occurs anywhere in that window, the 
binding is triggered. In our feet to meters example, we set up a binding for the "Return" key on the main application 
toplevel window. If the "Return" key is pressed when any widget contained in the toplevel window had the focus, that 
binding will fire.

Less commonly, you can create event bindings triggered when a matching event occurs anywhere in the application or even for 
events received by any widget of a given class, e.g., all buttons.

More than one binding can fire for an event. This keeps event handlers concise and limited in scope, making for more 
modular code. For example, the behavior of each widget class in Tk is itself defined with script-level event bindings. 
These stay separate from event bindings in your application. Event bindings assigned to a widget can also be changed (or 
deleted) at any time. They can be modified to alter event handling for widgets of a certain class or parts of your 
application. You can reorder, extend, or change the sequence of event bindings that are triggered for each widget; see the 
bindtags command reference if you're curious.

Available events
The most common events are described below, along with the circumstances when they are generated. Some are generated on 
some platforms and not others. For a complete description of all the different event names, modifiers, and the different 
event parameters that are available with each, the best place to look is the bind command reference.

<Activate>:
Window has become active.
<Deactivate>:
Window has been deactivated.
<MouseWheel>:
Scroll wheel on mouse has been moved.
<KeyPress>:
Key on keyboard has been pressed down.
<KeyRelease>:
Key has been released.
<ButtonPress>:
A mouse button has been pressed.
<ButtonRelease>:
A mouse button has been released.
<Motion>:
Mouse has been moved.
<Configure>:
Widget has changed size or position.
<Destroy>:
Widget is being destroyed.
<FocusIn>:
Widget has been given keyboard focus.
<FocusOut>:
Widget has lost keyboard focus.
<Enter>:
Mouse pointer enters widget.
<Leave>:
Mouse pointer leaves widget.
Event detail for mouse events is the button that was pressed, e.g., 1, 2, or 3. For keyboard events, it's the specific key, 
e.g., A, 9, space, plus, comma, equal. A complete list can be found in the keysyms command reference.

Event modifiers can include, e.g., B1 or Button1 to signify the main mouse button being held down, Double or Triple for 
sequences of the same event. Key modifiers for when keys on the keyboard are held down inline Control, Shift, Alt, Option, 
and Command.

Virtual events
The events we've seen so far are low-level operating system events like mouse clicks and window resizes. Many widgets also 
generate higher-level, semantic events called virtual events. These are indicated by double angle brackets around the event 
name, e.g., <<foo>>.

As we've mentioned, Ruby/Tk strips away the (single) angle brackets from regular event names. Virtual events use a single 
set of angle brackets, e.g., <foo>.
For example, a listbox widget generates a <<ListboxSelect>> virtual event whenever its selection changes. The same virtual 
event is generated whether a user clicked on an item, selected using the arrow keys, or another way. Virtual events avoid 
the problem of setting up multiple, possibly platform-specific event bindings to capture common changes. The available 
virtual events for a widget will be listed in the documentation for the widget class.

Tk also defines virtual events for common operations that are triggered in different ways for different platforms. These 
include <<Cut>>, <<Copy>> and <<Paste>>. A <<ContextMenu>> virtual event is generated when the right mouse button is 
clicked, taking care of that discrepancy between button #2 and button #3 on macOS we noted previously.

You can define your own virtual events, which can be specific to your application. This can be a useful way to keep 
platform-specific details isolated in a single module while using the virtual event throughout your application. Your own 
code can generate virtual events that work in exactly the same way that virtual events generated by Tk do.

root.event_generate("<<MyOwnEvent>>")
event generate . "<<MyOwnEvent>>"
Tk.event_generate(root, "<MyOwnEvent>")
Tkx::event_generate($mw, "<<MyOwnEvent>>");



