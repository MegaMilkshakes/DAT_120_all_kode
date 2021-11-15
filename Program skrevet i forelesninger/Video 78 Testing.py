# -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 14:51:03 2021

@author: gerry
"""



#enhetstest eksempel


tall_streng = input("Skriv inn en alder: ")
alder = int(tall_streng)
if alder >= 13 and alder < 18:
    print("Personen er tenåring")
else:
    print("Personen er ikke tenåring")
    
    
#Prinsipp for testing
#Bør teste flere verdier
#Bør teste alle veier gjennom programmet, test en alder under 13, over 18
    #mellom 13 & 18
#Bør teste grenseverdier, 12, 13 & 17, 18
#Bør teste feilhåndteringer

