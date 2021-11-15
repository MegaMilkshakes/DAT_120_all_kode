# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 09:58:44 2021

@author: Gerry
"""



alder = int(input("Skriv inn alderen din:"))

if alder < 18:
    print("Prisen på din billett er 20kr, for under 18år")
elif alder >= 67:
    print("Prisen på din billett er 20kr, for 67år eller over")
else:
    print("Normal pris 40kr")
    
