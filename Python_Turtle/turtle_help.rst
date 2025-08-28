=================================== back ===================================
Help on function back in turtle:

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

None
=================================== backward ===================================
Help on function backward in turtle:

turtle.backward = backward(distance)
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

None
=================================== bk ===================================
Help on function bk in turtle:

turtle.bk = bk(distance)
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

None
=================================== circle ===================================
Help on function circle in turtle:

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

None
=================================== clear ===================================
Help on function clear in turtle:

turtle.clear = clear()
    Delete the turtle's drawings from the screen. Do not move 
    
    No arguments.
    
    Delete the turtle's drawings from the screen. Do not move 
    State and position of the turtle as well as drawings of other
    turtles are not affected.
    
    Examples:
    >>> clear()

None
=================================== color ===================================
Help on function color in turtle:

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

None
=================================== degrees ===================================
Help on function degrees in turtle:

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

None
=================================== dot ===================================
Help on function dot in turtle:

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

None
=================================== down ===================================
Help on function down in turtle:

turtle.down = down()
    Pull the pen down -- drawing when moving.
    
    Aliases: pendown | pd | down
    
    No argument.
    
    Example:
    >>> pendown()

None
=================================== exitonclick ===================================
Help on function exitonclick in turtle:

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

None
=================================== fd ===================================
Help on function fd in turtle:

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

None
=================================== forward ===================================
Help on function forward in turtle:

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

None
=================================== goto ===================================
Help on function goto in turtle:

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

None
=================================== heading ===================================
Help on function heading in turtle:

turtle.heading = heading()
    Return the turtle's current heading.
    
    No arguments.
    
    Example:
    >>> left(67)
    >>> heading()
    67.0

None
=================================== home ===================================
Help on function home in turtle:

turtle.home = home()
    Move turtle to the origin - coordinates (0,0).
    
    No arguments.
    
    Move turtle to the origin - coordinates (0,0) and set its
    heading to its start-orientation (which depends on mode).
    
    Example:
    >>> home()

None
=================================== isdown ===================================
Help on function isdown in turtle:

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

None
=================================== left ===================================
Help on function left in turtle:

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

None
=================================== lt ===================================
Help on function lt in turtle:

turtle.lt = lt(angle)
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

None
=================================== mainloop ===================================
Help on function mainloop in turtle:

turtle.mainloop = mainloop()
    Starts event loop - calling Tkinter's mainloop function.
    
    No argument.
    
    Must be last statement in a turtle graphics program.
    Must NOT be used if a script is run from within IDLE in -n mode
    (No subprocess) - for interactive use of turtle graphics.
    
    Example:
    >>> mainloop()

None
=================================== pd ===================================
Help on function pd in turtle:

turtle.pd = pd()
    Pull the pen down -- drawing when moving.
    
    Aliases: pendown | pd | down
    
    No argument.
    
    Example:
    >>> pendown()

None
=================================== pencolor ===================================
Help on function pencolor in turtle:

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

None
=================================== pendown ===================================
Help on function pendown in turtle:

turtle.pendown = pendown()
    Pull the pen down -- drawing when moving.
    
    Aliases: pendown | pd | down
    
    No argument.
    
    Example:
    >>> pendown()

None
=================================== pensize ===================================
Help on function pensize in turtle:

turtle.pensize = pensize(width=None)
    Set or return the line thickness.
    
    Aliases:  pensize | width
    
    Argument:
    width -- positive number
    
    Set the line thickness to width or return it. If resizemode is set
    to "auto" and turtleshape is a polygon, that polygon is drawn with
    the same line thickness. If no argument is given, current pensize
    is returned.
    
    Example:
    >>> pensize()
    1
    >>> pensize(10)   # from here on lines of width 10 are drawn

None
=================================== pos ===================================
Help on function pos in turtle:

turtle.pos = pos()
    Return the turtle's current location (x,y), as a Vec2D-vector.
    
    Aliases: pos | position
    
    No arguments.
    
    Example:
    >>> pos()
    (0.00, 240.00)

None
=================================== position ===================================
Help on function position in turtle:

turtle.position = position()
    Return the turtle's current location (x,y), as a Vec2D-vector.
    
    Aliases: pos | position
    
    No arguments.
    
    Example:
    >>> pos()
    (0.00, 240.00)

None
=================================== radians ===================================
Help on function radians in turtle:

turtle.radians = radians()
    Set the angle measurement units to radians.
    
    No arguments.
    
    Example:
    >>> heading()
    90
    >>> radians()
    >>> heading()
    1.5707963267948966

None
=================================== right ===================================
Help on function right in turtle:

turtle.right = right(angle)
    Turn turtle right by angle units.
    
    Aliases: right | rt
    
    Argument:
    angle -- a number (integer or float)
    
    Turn turtle right by angle units. (Units are by default degrees,
    but can be set via the degrees() and radians() functions.)
    Angle orientation depends on mode. (See this.)
    
    Example:
    >>> heading()
    22.0
    >>> right(45)
    >>> heading()
    337.0

None
=================================== rt ===================================
Help on function rt in turtle:

turtle.rt = rt(angle)
    Turn turtle right by angle units.
    
    Aliases: right | rt
    
    Argument:
    angle -- a number (integer or float)
    
    Turn turtle right by angle units. (Units are by default degrees,
    but can be set via the degrees() and radians() functions.)
    Angle orientation depends on mode. (See this.)
    
    Example:
    >>> heading()
    22.0
    >>> right(45)
    >>> heading()
    337.0

None
=================================== screensize ===================================
Help on function screensize in turtle:

turtle.screensize = screensize(canvwidth=None, canvheight=None, bg=None)
    Resize the canvas the turtles are drawing on.
    
    Optional arguments:
    canvwidth -- positive integer, new width of canvas in pixels
    canvheight --  positive integer, new height of canvas in pixels
    bg -- colorstring or color-tuple, new backgroundcolor
    If no arguments are given, return current (canvaswidth, canvasheight)
    
    Do not alter the drawing window. To observe hidden parts of
    the canvas use the scrollbars. (Can make visible those parts
    of a drawing, which were outside the canvas before!)
    
    Example (for a Turtle instance named turtle):
    >>> turtle.screensize(2000,1500)
    >>> # e.g. to search for an erroneously escaped turtle ;-)

None
=================================== setpos ===================================
Help on function setpos in turtle:

turtle.setpos = setpos(x, y=None)
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

None
=================================== setx ===================================
Help on function setx in turtle:

turtle.setx = setx(x)
    Set the turtle's first coordinate to x
    
    Argument:
    x -- a number (integer or float)
    
    Set the turtle's first coordinate to x, leave second coordinate
    unchanged.
    
    Example:
    >>> position()
    (0.00, 240.00)
    >>> setx(10)
    >>> position()
    (10.00, 240.00)

None
=================================== sety ===================================
Help on function sety in turtle:

turtle.sety = sety(y)
    Set the turtle's second coordinate to y
    
    Argument:
    y -- a number (integer or float)
    
    Set the turtle's first coordinate to x, second coordinate remains
    unchanged.
    
    Example:
    >>> position()
    (0.00, 40.00)
    >>> sety(-10)
    >>> position()
    (0.00, -10.00)

None
=================================== up ===================================
Help on function up in turtle:

turtle.up = up()
    Pull the pen up -- no drawing when moving.
    
    Aliases: penup | pu | up
    
    No argument
    
    Example:
    >>> penup()

None
=================================== width ===================================
Help on function width in turtle:

turtle.width = width(width=None)
    Set or return the line thickness.
    
    Aliases:  pensize | width
    
    Argument:
    width -- positive number
    
    Set the line thickness to width or return it. If resizemode is set
    to "auto" and turtleshape is a polygon, that polygon is drawn with
    the same line thickness. If no argument is given, current pensize
    is returned.
    
    Example:
    >>> pensize()
    1
    >>> pensize(10)   # from here on lines of width 10 are drawn

None
