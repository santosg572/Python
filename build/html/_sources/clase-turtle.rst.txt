Clase turtle
============

La clase turtle de Python es una herramienta gráfica interactiva basada en la documentación de Python que permite controlar un 
cursor en forma de tortuga para dibujar líneas, figuras y patrones geométricos en una ventana virtual

**Algunos Métodos**

.. code::Python

   import turtle

``'back', 'backward', 'begin_fill', 'begin_poly', 'bgcolor', 'bgpic', 'bk', 'circle', 'clear', 'clearscreen', 'clearstamp', 'clearstamps', 'clone', 'color', 'colormode', 'config_dict', 'deepcopy', 'degrees', 'delay', 'distance', 'done', 'dot', 'down', 'end_fill', 'end_poly', 'exitonclick', 'fd', 'fillcolor', 'filling', 'forward', 'get_poly', 'get_shapepoly', 'getcanvas', 'getmethparlist', 'getpen', 'getscreen', 'getshapes', 'getturtle', 'goto', 'heading', 'hideturtle', 'home', 'ht', 'inspect', 'isdown', 'isfile', 'isvisible', 'join', 'left', 'listen', 'lt', 'mainloop', 'math', 'mode', 'numinput', 'onclick', 'ondrag', 'onkey', 'onkeypress', 'onkeyrelease', 'onrelease', 'onscreenclick', 'ontimer', 'pd', 'pen', 'pencolor', 'pendown', 'pensize', 'penup', 'pos', 'position', 'pu', 'radians', 'read_docstrings', 'readconfig', 'register_shape', 'reset', 'resetscreen', 'resizemode', 'right', 'rt', 'screensize', 'seth', 'setheading', 'setpos', 'setposition', 'setundobuffer', 'setup', 'setworldcoordinates', 'setx', 'sety', 'shape', 'shapesize', 'shapetransform', 'shearfactor', 'showturtle', 'simpledialog', 'speed', 'split', 'st', 'stamp', 'sys', 'teleport', 'textinput', 'tilt', 'tiltangle', 'time', 'title', 'towards', 'tracer', 'turtles', 'turtlesize', 'types', 'undo', 'undobufferentries', 'up', 'update', 'width', 'window_height', 'window_width', 'write', 'write_docstringdict', 'xcor', 'ycor'``


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



