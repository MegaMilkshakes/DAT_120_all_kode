# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 07:57:33 2021

@author: Gerry
"""

import turtle
turtle.setup(720,1150,1180,0)

turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)

turtle.circle(100) #100 er radius pixel
turtle.circle(80)
turtle.circle(60)
turtle.circle(40)

turtle.penup()#flytt pilen uten å tegne strek bak
turtle.forward(200)
turtle.pendown()

turtle.pencolor("green")
turtle.circle(100)
turtle.circle(80)
turtle.circle(60)
turtle.circle(40)

turtle.fillcolor("yellow")
turtle.begin_fill()
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.end_fill()

turtle.fillcolor("orange")
turtle.begin_fill()
turtle.circle(100)
turtle.end_fill()

