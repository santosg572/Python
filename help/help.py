import turtle

#dd = dir(turtle)


dd = ['back', 'backward', 'begin_fill', 'begin_poly', 'bgcolor', 'bk',  
'circle', 'clear', 'color',  
'degrees', 'delay', 'distance', 'done', 'dot', 'down', 'end_fill', 'fd', 'fillcolor', 'filling', 
'forward',
'goto', 'home', 'left', 
'mainloop', 'math', 'onclick', 'onkey', 'onkeypress', 'pd', 'pen', 'pencolor', 'pendown', 'pensize', 'penup', 'pos', 'radians', 
'shape', 'up', 'write']

for ss in dd:

   print(help('turtle.'+ss))


