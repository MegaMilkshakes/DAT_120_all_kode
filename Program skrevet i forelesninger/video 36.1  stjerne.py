# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 08:45:32 2021

@author: Gerry
"""


import turtle
turtle.setup(720,950,1180,0)
turtle.speed(10)
turtle.forward(100)

for i in range(9):
    turtle.right(160)
    turtle.forward(200)
    
turtle.penup()
turtle.forward(100)
turtle.pendown()

turtle.forward(100)

for ii in range(24):
    turtle.right(165)
    turtle.forward(200)
    
turtle.right(180)
turtle.penup()
turtle.forward(500)
turtle.pendown()

turtle.forward(100)

for ii in range(36):
    turtle.right(170)
    turtle.forward(200)
    
#vinkelen må være mindre enn 180grader, ellers
#snur du deg jo bare helt rundt.
#prøv seg frem til hvor mange ganger den må tegne for å komme helt rundt
