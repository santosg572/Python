Clase turtle
============

.. code::Python

   import turtle

``'addshape', 'back', 'backward', 'begin_fill', 'begin_poly', 'bgcolor', 'bgpic', 'bk', 'bye', 'circle', 'clear', 'clearscreen', 'clearstamp', 'clearstamps', 'clone', 'color', 'colormode', 'config_dict', 'deepcopy', 'degrees', 'delay', 'distance', 'done', 'dot', 'down', 'end_fill', 'end_poly', 'exitonclick', 'fd', 'fillcolor', 'filling', 'forward', 'get_poly', 'get_shapepoly', 'getcanvas', 'getmethparlist', 'getpen', 'getscreen', 'getshapes', 'getturtle', 'goto', 'heading', 'hideturtle', 'home', 'ht', 'inspect', 'isdown', 'isfile', 'isvisible', 'join', 'left', 'listen', 'lt', 'mainloop', 'math', 'mode', 'numinput', 'onclick', 'ondrag', 'onkey', 'onkeypress', 'onkeyrelease', 'onrelease', 'onscreenclick', 'ontimer', 'pd', 'pen', 'pencolor', 'pendown', 'pensize', 'penup', 'pos', 'position', 'pu', 'radians', 'read_docstrings', 'readconfig', 'register_shape', 'reset', 'resetscreen', 'resizemode', 'right', 'rt', 'screensize', 'seth', 'setheading', 'setpos', 'setposition', 'setundobuffer', 'setup', 'setworldcoordinates', 'setx', 'sety', 'shape', 'shapesize', 'shapetransform', 'shearfactor', 'showturtle', 'simpledialog', 'speed', 'split', 'st', 'stamp', 'sys', 'teleport', 'textinput', 'tilt', 'tiltangle', 'time', 'title', 'towards', 'tracer', 'turtles', 'turtlesize', 'types', 'undo', 'undobufferentries', 'up', 'update', 'width', 'window_height', 'window_width', 'write', 'write_docstringdict', 'xcor', 'ycor'``


**Ayuda**

.. code:: Bash

   back(distance)
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

   bgcolor(*args)
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

   circle(radius, extent=None, steps=None)
       Draw a circle with given radius.

       Arguments:
       radius -- a number
       extent (optional) -- a number
       steps (optional) -- an integer

   clear()
       Delete the turtle's drawings from the screen. Do not move

   dot(size=None, *color)
       Draw a dot with diameter size, using color.

       Optional arguments:
       size -- an integer >= 1 (if given)
       color -- a colorstring or a numeric color tuple

   down()
       Pull the pen down -- drawing when moving.

       Aliases: pendown | pd | down

   exitonclick()
       Go into mainloop until the mouse is clicked.

   forward(distance)
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

   goto(x, y=None)
       Move turtle to an absolute position.

       Aliases: setpos | setposition | goto:

       Arguments:
       x -- a number      or     a pair/vector of numbers
       y -- a number             None

   left(angle)
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

   mainloop()
       Starts event loop - calling Tkinter's mainloop function.

       No argument.

       Must be last statement in a turtle graphics program.
       Must NOT be used if a script is run from within IDLE in -n mode
       (No subprocess) - for interactive use of turtle graphics.

       Example:
       >>> mainloop()

   pendown()
       Pull the pen down -- drawing when moving.

       Aliases: pendown | pd | down

       No argument.

       Example:
       >>> pendown()

   pensize(width=None)
       Set or return the line thickness.

       Aliases:  pensize | width

       Argument:
       width -- positive number



**Algunos métodos y ejemplos:**

.. code:: Python

   import turtle

   turtle.bgcolor('red')
   turtle.back(20)
   turtle.circle(20)

.. code:: Python

   turte.clear()

.. code:: Python

   turtle.up()
   turtle.goto(40,30)
   turtle.down()
   turtle.circle(20)
   turtle.up()
   turtle.goto(20,60)
   turtle.down()
   turtle.circle(30)
   turtle.up()
   turtle.goto(-20,60)
   turtle.down()
   turtle.circle(10)

.. code:: Python

   turtle.pensize(3)
   turtle.fd(20)
   turtle.left(90)
   turtle.fd(20)
   turtle.left(45)
   turtle.fd(30)








      

