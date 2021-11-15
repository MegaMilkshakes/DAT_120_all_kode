# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 16:55:29 2021

@author: Gerry
"""


tall = int(input("Skriv inn tallet du ønsker fakulitet av: "))
while tall < 0:
    print("Fakulitet for negative tall finnes ikke!")
    tall = int(input("Skriv inn gyldig tall du ønsker fakulitet av: "))

resultat = 1
for i in range(1,tall+1):
    print(i)
    resultat *= i
print("Etter for-løkka er ferdig")
print(resultat)
