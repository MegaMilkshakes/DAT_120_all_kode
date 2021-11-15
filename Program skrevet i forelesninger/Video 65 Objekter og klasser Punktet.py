# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 19:01:59 2021

@author: gerry
"""


#Klasse: punkt

class Punkt:  #start med stor bokstav, skiller klasse fra funksjoner og variabler
    #konstruktør
    def __init__(self, start_x=0, start_y=0):
        self.x_koordinat = start_x
        self.y_koordinat = start_y
        

punktet = Punkt()

print(punktet.x_koordinat)
print(punktet.y_koordinat)

punktet.x_koordinat = 10
print(punktet.x_koordinat)
print(punktet.y_koordinat)

punktet = Punkt(2, 3)
print(punktet.x_koordinat)
print(punktet.y_koordinat)