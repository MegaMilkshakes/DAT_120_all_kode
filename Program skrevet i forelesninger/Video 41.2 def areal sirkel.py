# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 19:13:17 2021

@author: Gerry
"""

import math

def areal_sirkel(radius):
    areal = math.pi*radius*radius
    return areal
    print("Test")


def omkrets_sirkel(radius):
    return 2.0*math.pi*radius


radius_streng = input("Skriv inn radius til en sirkel: ")
radius_bruker = float(radius_streng)
areal_global = areal_sirkel(radius_bruker)
print(f"Arealet ble: {areal_global:8.2f}")
omkrets = omkrets_sirkel(radius_bruker)
print(f"Omkretsen ble: {omkrets:8.2f}")#8.2f betyr 8 siffer, 2bak komma , 

