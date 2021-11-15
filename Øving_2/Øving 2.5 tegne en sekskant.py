# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 11:18:54 2021

@author: Gerry
"""



import turtle
turtle.setup(720,1150,1180,0)

VINKEL = 60
PIKSLER = 80

#turtle.color("green")
#turtle.fillcolor("blue")

#turtle.begin_fill()
for i in range(6):
    turtle.forward(PIKSLER)
    turtle.right(VINKEL)  
#turtle.end_fill()
