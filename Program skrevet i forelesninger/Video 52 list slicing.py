# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 14:21:00 2021

@author: gerry
"""


#listekutt
liste3 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
liste4 = liste3[3:8] #HUSK fra a, til men ikke med b!!

print(liste4)

#starte i starten til et vist punkt
print(liste3[:8])

#omvendt, start et vist punkt, men gå ut hele lista
print(liste3[5:])

#få en "kopi" av lista
print(liste3[:])

#Steglengde gjøres med en til parameter
print(liste3[1:10:2])

