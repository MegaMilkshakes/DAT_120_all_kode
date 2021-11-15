# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 15:20:14 2021

@author: Gerry
"""


teksten = ""
tekstlinje = input("Skriv inn første linje: ")
while tekstlinje != "":
    teksten = teksten + tekstlinje + "\n"
    # \n er newline, altså enter, altså hver linje du skriver 
    #inn kommer på en ny linje
    tekstlinje = input("Skriv inn neste linje: ")
    
print("Den endelige teksten ble: ")
print(teksten)

