# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 17:35:28 2021

@author: Gerry
"""

fortsetter = True
while fortsetter: #== True:
    try:
        tall = int(input("Skriv inn tall du ønsker fakultet av: "))
        if tall < 0:
            print("Fakultet for negative tall finnes ikke!")
        else:
            fortsetter = False
    except ValueError:
            print("Du må skrive inn et tall!")


    
resultat = 1
for i in range(1, tall+1):
    print(i)
    resultat *= i
print("Etter for-løkka er ferdig")
print(resultat)
