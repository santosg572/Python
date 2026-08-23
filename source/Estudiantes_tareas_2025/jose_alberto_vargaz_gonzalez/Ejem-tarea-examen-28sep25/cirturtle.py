import turtle
import random

# Configuración inicial
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("white")

t = turtle.Turtle()

# Colores 
colores = ['red', 'blue', 'green', 'black']

# Generar 50 círculos aleatorios
for _ in range(50):
    # Posición aleatoria en [-100, 100] x [-100, 100]
    x = random.randint(-100, 100)
    y = random.randint(-100, 100)
    
    # Radio aleatorio entre 10 y 20
    radio = random.randint(10, 20)
    
    # Color aleatorio
    color = random.choice(colores)
    
    # Dibujar el círculo
    t.penup()
    t.goto(x, y - radio)  # Posicionarse en el punto de inicio del círculo
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    t.circle(radio)
    t.end_fill()

# Mostrar el dibujo
turtle.done()
