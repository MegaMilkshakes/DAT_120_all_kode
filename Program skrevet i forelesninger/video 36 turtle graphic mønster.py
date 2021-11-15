# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 08:35:08 2021

@author: Gerry
"""

import turtle
turtle.setup(720,950,1180,0)

STORRELSE = 50
VINKEL = 15
turtle.speed(10)
#speed 0 animerer ikke, bare fyller ut fort
#ellers speed 1-10

turtle.circle(STORRELSE)

vinkel_saa_langt = 0
while vinkel_saa_langt < 360:
    turtle.circle(STORRELSE)
    turtle.right(VINKEL)
    vinkel_saa_langt += VINKEL
