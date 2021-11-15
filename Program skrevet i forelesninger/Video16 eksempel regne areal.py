# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 19:09:35 2021

@author: Gerry
"""

lengde_meter_streng = input("Skriv inn lengde i meter: ")
bredde_meter_streng = input("Skriv inn bredde i meter: ")
lengde_meter = float(lengde_meter_streng)
bredde_meter = float(bredde_meter_streng)
areal = lengde_meter*bredde_meter
print("Arealet ditt er i meter:")
print(round(areal, 2))
