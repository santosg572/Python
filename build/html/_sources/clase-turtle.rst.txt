Clase turtle
============

La clase turtle de Python es una herramienta gráfica interactiva basada en la documentación de Python que permite controlar un 
cursor en forma de tortuga para dibujar líneas, figuras y patrones geométricos en una ventana virtual

**Ejemplos**

1)

.. code:: Python

   import turtle

   turtle.circle(50)

   turtle.circle(70)

   turtle.clear()
      
   turtle.forward(50)

   turtle.left(90)

   turtle.forward(70)  

   turtle.up()

   turtle.left(90)

   turtle.forward(70)

   turtle.down()

   turtle.forward(50)

   turtle.goto(75, 75)

2)

.. code:: Python

   import turtle

   turtle.fillcolor("blue") 

   turtle.begin_fill()
   turtle.circle(100)
   turtle.end_fill()


turtle_dir.txt

**Canvas**

**Pen**

**RawPen**

**RawTurtle**

**Screen**

**ScrolledCanvas**

**Shape**

**TK**

TNavigator
TPen
Tbuffer
Terminator
Turtle
TurtleGraphicsError
TurtleScreen
TurtleScreenBase
Vec2D
addshape

**back**

.. code:: Python

   turtle.back = back(distance)
    Move the turtle backward by distance.
 
    Aliases: back | backward | bk
    
    Argument:
    distance -- a number
        
    Move the turtle backward by distance, opposite to the direction the
    turtle is headed. Do not change the turtle's heading.  
        
    Example:
    >>> position()
    (0.00, 0.00)
    >>> backward(30)
    >>> position()
    (-30.00, 0.00)

**backward**

**begin_fill**

.. code:: Python

   turtle.begin_fill = begin_fill()
    Called just before drawing a shape to be filled.

    No argument.

    Example:
    >>> color("black", "red")
    >>> begin_fill()
    >>> circle(60)
    >>> end_fill()

**bgcolor**

.. code:: Python

   turtle.bgcolor = bgcolor(*args)
    Set or return backgroundcolor of the TurtleScreen.
    
    Arguments (if given): a color string or three numbers
    in the range 0..colormode or a 3-tuple of such numbers.

    Example:
    >>> bgcolor("orange")
    >>> bgcolor()
    'orange'
    >>> bgcolor(0.5,0,0.5)
    >>> bgcolor()
    '#800080'   

**bye**

.. code:: Python

   turtle.bye = bye()
    Shut the turtlegraphics window.

    Example:
    >>> bye()

**circle**

.. code:: Python

   turtle.circle = circle(radius, extent=None, steps=None)
    Draw a circle with given radius.
    
    Arguments:
    radius -- a number
    extent (optional) -- a number
    steps (optional) -- an integer
    
    Draw a circle with given radius. The center is radius units left
    of the turtle; extent - an angle - determines which part of the
    circle is drawn. If extent is not given, draw the entire circle.
    If extent is not a full circle, one endpoint of the arc is the
    current pen position. Draw the arc in counterclockwise direction
    if radius is positive, otherwise in clockwise direction. Finally
    the direction of the turtle is changed by the amount of extent.
    
    As the circle is approximated by an inscribed regular polygon,
    steps determines the number of steps to use. If not given,
    it will be calculated automatically. Maybe used to draw regular
    polygons.

    call: circle(radius)                  # full circle
    --or: circle(radius, extent)          # arc
    --or: circle(radius, extent, steps)
    --or: circle(radius, steps=6)         # 6-sided polygon
    
    Example:
    >>> circle(50)
    >>> circle(120, 180)  # semicircle


**clear**

.. code:: Python

   turtle.clear = clear()
    Delete the turtle's drawings from the screen. Do not move
    
    No arguments.
    
    Delete the turtle's drawings from the screen. Do not move
    State and position of the turtle as well as drawings of other 
    turtles are not affected.
    
    Examples:
    >>> clear()


**clearscreen**

   turtle.clearscreen = clearscreen()
    Delete all drawings and all turtles from the TurtleScreen.
    
    No argument.

    Reset empty TurtleScreen to its initial state: white background,
    no backgroundimage, no eventbindings and tracing on.
    
    Example:
    >>> clear()
    
    Note: this method is not available as function.


**color**

.. code:: Python

   turtle.color = color(*args)
    Return or set the pencolor and fillcolor.
    
    Arguments:
    Several input formats are allowed.
    They use 0, 1, 2, or 3 arguments as follows:

    color()
        Return the current pencolor and the current fillcolor
        as a pair of color specification strings as are returned
        by pencolor and fillcolor.
    color(colorstring), color((r,g,b)), color(r,g,b)
        inputs as in pencolor, set both, fillcolor and pencolor,
        to the given value.
    color(colorstring1, colorstring2),
    color((r1,g1,b1), (r2,g2,b2))
        equivalent to pencolor(colorstring1) and fillcolor(colorstring2)
        and analogously, if the other input format is used.
    
    If turtleshape is a polygon, outline and interior of that polygon
    is drawn with the newly set colors.
    For more info see: pencolor, fillcolor

    Example:
    >>> color('red', 'green')
    >>> color()
    ('red', 'green')
    >>> colormode(255)
    >>> color((40, 80, 120), (160, 200, 240))
    >>> color()
    ('#285078', '#a0c8f0')
    
**degrees**

.. code:: Python

   turtle.degrees = degrees(fullcircle=360.0)
    Set angle measurement units to degrees.
    
    Optional argument:
    fullcircle -  a number

    Set angle measurement units, i. e. set number
    of 'degrees' for a full circle. Default value is
    360 degrees.
    
    Example:
    >>> left(90)
    >>> heading()
    90

    Change angle measurement unit to grad (also known as gon,
    grade, or gradian and equals 1/100-th of the right angle.)
    >>> degrees(400.0)
    >>> heading()
    100 

**delay**

.. code:: Python

   turtle.delay = delay(delay=None)
    Return or set the drawing delay in milliseconds.
    
    Optional argument:
    delay -- positive integer
    
    Example:
    >>> delay(15)
    >>> delay()
    15

**distance**

.. code:: Python

   turtle.distance = distance(x, y=None)
    Return the distance from the turtle to (x,y) in turtle step units.
    
    Arguments:
    x -- a number   or  a pair/vector of numbers   or   a turtle instance
    y -- a number       None                            None

    call: distance(x, y)         # two coordinates
    --or: distance((x, y))       # a pair (tuple) of coordinates
    --or: distance(vec)          # e.g. as returned by pos()
    --or: distance(mypen)        # where mypen is another turtle
    
    Example:
    >>> pos()
    (0.00, 0.00)
    >>> distance(30,40)
    50.0
    >>> pen = Turtle()
    >>> pen.forward(77)
    >>> distance(pen)
    77.0


**done**

.. code:: Python

   turtle.done = mainloop()
    Starts event loop - calling Tkinter's mainloop function.
    
    No argument.

    Must be last statement in a turtle graphics program.
    Must NOT be used if a script is run from within IDLE in -n mode
    (No subprocess) - for interactive use of turtle graphics.
    
    Example:
    >>> mainloop()

**dot**

.. code:: Python

   turtle.dot = dot(size=None, *color)
    Draw a dot with diameter size, using color.
    
    Optional arguments:
    size -- an integer >= 1 (if given)
    color -- a colorstring or a numeric color tuple

    Draw a circular dot with diameter size, using color.
    If size is not given, the maximum of pensize+4 and 2*pensize is used.
    
    Example:
    >>> dot()   
    >>> fd(50); dot(20, "blue"); fd(50)


**down**

.. code:: Python

   turtle.down = down()
    Pull the pen down -- drawing when moving.

    Aliases: pendown | pd | down

    No argument.

    Example:
    >>> pendown()


**end_fill**

.. code:: Python

    Fill the shape drawn after the call begin_fill().
    
    No argument.
    
    Example:
    >>> color("black", "red")
    >>> begin_fill()
    >>> circle(60)
    >>> end_fill()


**exitonclick**

.. code:: Python

   turtle.exitonclick = exitonclick()
    Go into mainloop until the mouse is clicked.
    
    No arguments. 

    Bind bye() method to mouseclick on TurtleScreen.
    If "using_IDLE" - value in configuration dictionary is False
    (default value), enter mainloop.
    If IDLE with -n switch (no subprocess) is used, this value should be
    set to True in turtle.cfg. In this case IDLE's mainloop
    is active also for the client script.
    
    This is a method of the Screen-class and not available for
    TurtleScreen instances.
    
    Example:
    >>> exitonclick()


**fd**

.. code:: Python

   turtle.fd = fd(distance)
    Move the turtle forward by the specified distance.

    Aliases: forward | fd
    
    Argument:
    distance -- a number (integer or float)
    
    Move the turtle forward by the specified distance, in the direction
    the turtle is headed.
    
    Example:
    >>> position()
    (0.00, 0.00)
    >>> forward(25)
    >>> position()
    (25.00,0.00)
    >>> forward(-75)
    >>> position()   
    (-50.00,0.00)

**fillcolor**

.. code:: Python

   turtle.fillcolor = fillcolor(*args)
    Return or set the fillcolor.
    
    Arguments:
    Four input formats are allowed:
      - fillcolor()
        Return the current fillcolor as color specification string,
        possibly in hex-number format (see example).
        May be used as input to another color/pencolor/fillcolor call.
      - fillcolor(colorstring)
        s is a Tk color specification string, such as "red" or "yellow"
      - fillcolor((r, g, b))
        *a tuple* of r, g, and b, which represent, an RGB color,
        and each of r, g, and b are in the range 0..colormode,
        where colormode is either 1.0 or 255
      - fillcolor(r, g, b)
        r, g, and b represent an RGB color, and each of r, g, and b
        are in the range 0..colormode
    
    If turtleshape is a polygon, the interior of that polygon is drawn
    with the newly set fillcolor.

    Example:
    >>> fillcolor('violet')
    >>> col = pencolor()
    >>> fillcolor(col)
    >>> fillcolor(0, .5, 0)



**forward**

.. code:: Python

   turtle.forward = forward(distance)
    Move the turtle forward by the specified distance.
    
    Aliases: forward | fd

    Argument:
    distance -- a number (integer or float)
        
    Move the turtle forward by the specified distance, in the direction
    the turtle is headed.
        
    Example:
    >>> position()
    (0.00, 0.00)
    >>> forward(25) 
    >>> position()   
    (25.00,0.00)
    >>> forward(-75)
    >>> position()
    (-50.00,0.00)


**goto**

.. code:: Python

   turtle.goto = goto(x, y=None)
    Move turtle to an absolute position.

    Aliases: setpos | setposition | goto:
    
    Arguments:
    x -- a number      or     a pair/vector of numbers
    y -- a number             None
    
    call: goto(x, y)         # two coordinates
    --or: goto((x, y))       # a pair (tuple) of coordinates
    --or: goto(vec)          # e.g. as returned by pos()
    
    Move turtle to an absolute position. If the pen is down,
    a line will be drawn. The turtle's orientation does not change.
    
    Example:
    >>> tp = pos()
    >>> tp
    (0.00, 0.00)
    >>> setpos(60,30)
    >>> pos()
    (60.00,30.00)
    >>> setpos((20,80))
    >>> pos()
    (20.00,80.00)
    >>> setpos(tp)
    >>> pos()
    (0.00,0.00)


**home**

.. code:: Python

   turtle.home = home()
    Move turtle to the origin - coordinates (0,0).

    No arguments.

    Move turtle to the origin - coordinates (0,0) and set its
    heading to its start-orientation (which depends on mode).
    
    Example:
    >>> home()


**isdown**

.. code:: Python

   turtle.isdown = isdown()
    Return True if pen is down, False if it's up.
     
    No argument.
     
    Example:
    >>> penup()
    >>> isdown()
    False
    >>> pendown()
    >>> isdown()
    True

**left**

.. code:: Python

   turtle.left = left(angle)
    Turn turtle left by angle units.
     
    Aliases: left | lt
     
    Argument:
    angle -- a number (integer or float)
    
    Turn turtle left by angle units. (Units are by default degrees,
    but can be set via the degrees() and radians() functions.)
    Angle orientation depends on mode. (See this.)

    Example:
    >>> heading()
    22.0
    >>> left(45)
    >>> heading()
    67.0

**mainloop**

.. code:: Python

   turtle.mainloop = mainloop()
    Starts event loop - calling Tkinter's mainloop function.
    
    No argument.
    
    Must be last statement in a turtle graphics program.
    Must NOT be used if a script is run from within IDLE in -n mode
    (No subprocess) - for interactive use of turtle graphics.

    Example:
    >>> mainloop()



**onclick**

.. code:: Python

   turtle.onclick = onclick(fun, btn=1, add=None)
    Bind fun to mouse-click event on this turtle on canvas.
           
    Arguments:
    fun --  a function with two arguments, to which will be assigned
            the coordinates of the clicked point on the canvas.
    btn --  number of the mouse-button defaults to 1 (left mouse button).
    add --  True or False. If True, new binding will be added, otherwise
            it will replace a former binding.
    
    Example for the anonymous turtle, i. e. the procedural way:
    
    >>> def turn(x, y):
    ...     left(360)
    ...
    >>> onclick(turn)  # Now clicking into the turtle will turn it.
    >>> onclick(None)  # event-binding will be removed


**pen**

.. code:: Python

   turtle.pen = pen(pen=None, **pendict)
    Return or set the pen's attributes.
    
    Arguments:
        pen -- a dictionary with some or all of the below listed keys.
        **pendict -- one or more keyword-arguments with the below
                     listed keys as keywords.
    
    Return or set the pen's attributes in a 'pen-dictionary'
    with the following key/value pairs:
       "shown"      :   True/False
       "pendown"    :   True/False
       "pencolor"   :   color-string or color-tuple
       "fillcolor"  :   color-string or color-tuple
       "pensize"    :   positive number
       "speed"      :   number in range 0..10
       "resizemode" :   "auto" or "user" or "noresize"
       "stretchfactor": (positive number, positive number)
       "shearfactor":   number
       "outline"    :   positive number
       "tilt"       :   number

    This dictionary can be used as argument for a subsequent
    pen()-call to restore the former pen-state. Moreover one
    or more of these attributes can be provided as keyword-arguments.
    This can be used to set several pen attributes in one statement.
    
      
    Examples:
    >>> pen(fillcolor="black", pencolor="red", pensize=10)
    >>> pen()
    {'pensize': 10, 'shown': True, 'resizemode': 'auto', 'outline': 1,
    'pencolor': 'red', 'pendown': True, 'fillcolor': 'black',
    'stretchfactor': (1,1), 'speed': 3, 'shearfactor': 0.0}
    >>> penstate=pen()
    >>> color("yellow","")
   >>> penup()
    >>> pen()
    {'pensize': 10, 'shown': True, 'resizemode': 'auto', 'outline': 1,
    'pencolor': 'yellow', 'pendown': False, 'fillcolor': '',
    'stretchfactor': (1,1), 'speed': 3, 'shearfactor': 0.0}
    >>> p.pen(penstate, fillcolor="green")
    >>> p.pen()
    {'pensize': 10, 'shown': True, 'resizemode': 'auto', 'outline': 1,
    'pencolor': 'red', 'pendown': True, 'fillcolor': 'green',
    'stretchfactor': (1,1), 'speed': 3, 'shearfactor': 0.0}

**pencolor**

.. code:: Python

   turtle.pencolor = pencolor(*args)
    Return or set the pencolor.
    
    Arguments:
    Four input formats are allowed:
      - pencolor()
        Return the current pencolor as color specification string,
        possibly in hex-number format (see example).
        May be used as input to another color/pencolor/fillcolor call.
      - pencolor(colorstring)
        s is a Tk color specification string, such as "red" or "yellow"
      - pencolor((r, g, b))
        *a tuple* of r, g, and b, which represent, an RGB color,
        and each of r, g, and b are in the range 0..colormode,
        where colormode is either 1.0 or 255
      - pencolor(r, g, b)
        r, g, and b represent an RGB color, and each of r, g, and b   
        are in the range 0..colormode
    
    If turtleshape is a polygon, the outline of that polygon is drawn
    with the newly set pencolor.
    
    Example:
    >>> pencolor('brown')
    >>> tup = (0.2, 0.8, 0.55)
    >>> pencolor(tup)
    >>> pencolor()
    '#33cc8c'

**pendown**
pensize
penup
pos
position
pu
radians
read_docstrings
readconfig
register_shape
reset
resetscreen
resizemode
right
rt
screensize
seth
setheading
setpos
setposition
settiltangle
setundobuffer
setup
setworldcoordinates
setx
sety
shape
shapesize
shapetransform
shearfactor
showturtle
simpledialog
speed
split
st
stamp
sys
textinput
tilt
tiltangle
time
title
towards
tracer
turtles
turtlesize
types
undo
undobufferentries
up
update
width
window_height
window_width
write
write_docstringdict
xcor
ycor
(base) iMac-de-Fernando:help santosg$ 

