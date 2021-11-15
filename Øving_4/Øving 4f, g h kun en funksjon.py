# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 17:20:16 2021

@author: Gerry
"""


import math

def euclidske_avstand(x, y):
    avstand = math.sqrt(x**2+y**2)
    return avstand


def avstand_mellom_to_punkter(x1, x2, y1, y2):
    x = x2 - x1
    y = y2 - y1
    return euclidske_avstand(x, y)


x1 = float(input("Skriv inn det første x-koordinate: "))
x2 = float(input("Skriv inn det andre x-koordinate: "))
y1 = float(input("Skriv inn det første y-koordinate: "))
y2 = float(input("Skriv inn det andre y-koordinate: "))


den_endelige_avstanden = avstand_mellom_to_punkter(x1, x2, y1, y2)

print(den_endelige_avstanden)

