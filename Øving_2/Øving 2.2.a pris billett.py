# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 09:50:10 2021

@author: Gerry
"""



alder = int(input("Skriv inn alderen på personen som kjøper billett: "))

if alder < 18 or alder >= 67:
    print("Prisen er 20kr")
else:
    print("Prisen er 40kr")
    
