# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 17:19:14 2021

@author: Gerry
"""


hoyde = int(input("Høyde: "))
bredde = int(input("Bredde: "))


for ii in range(hoyde):#for hver gang denne ytre for kjører, 
#så kjører den indre hele sin syklus før vi returnerer til ytre
    for i in range(bredde):
        print("*", end="")#ha med end="" for å unngå at print skriver på en ny linje hver gang
    print()#print må være på samme rekke som i range, ikke ii.
    #nå skriver den ut på riktig linje og enter imellom
