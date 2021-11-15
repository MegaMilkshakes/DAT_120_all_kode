# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 21:48:44 2021

@author: Gerry
"""

sekunder_string = input("Skriv inn antall sekunder objektet faller:")
sekunder = float(sekunder_string)

akselerasjon = 9.81
fart = akselerasjon * sekunder

distanse = 0.5 * fart * sekunder

print("Fart:", round(fart, 2),"m/s")
print("Distanse:", round(distanse, 2),"m")
