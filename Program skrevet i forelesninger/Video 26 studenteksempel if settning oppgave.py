# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 21:54:51 2021

@author: Gerry
"""

# ax^2 + bx + c = 0
# hvordan skrive opphøyd? 

import math

a = int(input("Skriv inn et tall for a:"))
b = int(input("Skriv inn et tall for b:"))
c = int(input("Skriv inn et tall for c:"))

verditest = b**2 - 4*a*c
#må være 0 eller høyere

if verditest >0:
    losning1 = (-b + math.sqrt(verditest)) / (2*a)
    losning2 = (-b - math.sqrt(verditest)) / (2*a)
    print(f"Likninger har to løsninger: {losning1} og {losning2}")
    
elif verditest == 0:
    losning = (-b)/(2*a)
    print(f"Likningen har en løsning: {losning}")

else:
    print("Likningen har ingen løsninger")