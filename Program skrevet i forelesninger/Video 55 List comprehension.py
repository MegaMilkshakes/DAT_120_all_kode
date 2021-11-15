# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 19:45:15 2021

@author: gerry
"""

#Alternativ måte å lage en liste
#x**2 x skal være 1-10
liste = list()
for verdi in range(1, 11):
    liste.append(verdi**2)
print(liste)
print("\n")

#alternativ
liste2 = [verdi for verdi in range(1, 11)]
print(liste2)
print("\n")

liste3 = [verdi**2 for verdi in range(1, 11)]
print(liste3)
print("\n")

#if settning inni resten, her print kun oddetall
liste4 = [verdi for verdi in range(1,20) if verdi%2 == 1]
print(liste4)
print("\n")


liste5 = [verdi**2 for verdi in range(1,20) if verdi%2 == 1]
print(liste5)
print("\n")

#alternativ måte å skrive liste5 på
liste6 = list()
for verdi in range(1, 20):
    if verdi%2 == 1:
        liste6.append(verdi**2)
print(liste6)
print("\n")

