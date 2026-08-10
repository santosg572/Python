# -*- coding: utf-8 -*-
"""
Created on Mon Sep  8 16:01:57 2025

@author: Carlos Gil
"""
import turtle
import random


screen = turtle.Screen()


screen.setup(width=800, height=600)

t = turtle.Turtle()
t.speed(0)
t.pensize(3)
t.forward(50)
t.right(50)

color= ["red", "blue", "green", "black"]



for i in range(50):
    t.pencolor(random.choice(color))
    t.forward(100)
    t.right(100)
    

t.penup()

t.goto(random.randint(-100, 100), random.randint(-100, 100))

t.pendown()

r= random.randint(10, 20)
t.circle(r)

turtle.done()

