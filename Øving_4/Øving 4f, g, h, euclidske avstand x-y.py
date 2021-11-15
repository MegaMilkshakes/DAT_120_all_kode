# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 16:36:51 2021

@author: Gerry
"""



import math

def euclidske_avstand(x, y):
    avstand = math.sqrt(x**2+y**2)
    return avstand


def avstand_mellom_x(x1, x2):
    avstand1 = x2 - x1
    x = avstand1
    return x


def avstand_mellom_y(y1, y2):
    avstand2 = y2 - y1
    y = avstand2
    return y


x1 = float(input("Skriv inn det første x-koordinate: "))
x2 = float(input("Skriv inn det andre x-koordinate: "))
y1 = float(input("Skriv inn det første y-koordinate: "))
y2 = float(input("Skriv inn det andre y-koordinate: "))

x = avstand_mellom_x(x1, x2)
y = avstand_mellom_y(y1, y2)

endelige_avstand = euclidske_avstand(x, y)

print(endelige_avstand)

