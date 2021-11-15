# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 19:19:02 2021

@author: Gerry
"""
fortsetter = True
while fortsetter:
    filnavn = input("Hvilken fil skal leses? ")
    try:
        fila = open(filnavn, "r", encoding="UTF8")
        fortsetter = False
    except FileNotFoundError:
        print("Kan ikke finne fila")
        print("Prøv på nytt")
        #exit()
    
summen = 0
for linje in fila:
    try:
        summen += int(linje)
    except ValueError:
        #pass
        print("Fant ei linje som ikke tolkes som et tall!")
fila.close()
print(f"Summen ble: {summen}")
