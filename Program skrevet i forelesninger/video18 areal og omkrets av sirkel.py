# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 19:24:34 2021

@author: Gerry
"""

import math

radius_streng = input("Skriv inn radius:")
radius = float(radius_streng)

a = math.pi * radius * radius
o = 2 * math.pi * radius

print("Areal:", round(a, 2), "Omkrets", round(o, 2))
