# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 11:38:52 2021

@author: Gerry
"""



import turtle
turtle.setup(720,1150,1180,0)
turtle.speed(10)

antall_diamanter = int(input("Skriv inn antall diamanter du vil ha: "))
VINKEL = 90
LENGDE = 50

turtle.right(45)

antall_loops = 0
for y in range(antall_diamanter):
    
    for x in range(4): #4 fordi 4 sider i en diamant
            turtle.forward(LENGDE + (antall_loops*(LENGDE*2)))
            turtle.right(VINKEL)
    antall_loops += +1
    turtle.penup()
    turtle.left(135)
    turtle.forward(LENGDE*1.5)
    turtle.pendown()
    turtle.right(135)
