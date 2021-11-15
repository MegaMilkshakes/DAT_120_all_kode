# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 16:11:40 2021

@author: Gerry
"""
tall = int(input("Skriv inn tallet du ønsker fakulitet av: "))

#resultat er lagt inn i etterkant for å vise hvorfor vi begynner med 0

resultat = 1

#for å unngå at fakuliteten for tall starter på 0, bruk 2
#parameter i range(), altså ikke bare range(tall, men bruk range(1,tall))
#for å få med det siste tallet må vi legge til +1 i range i tallet

for i in range(1,tall+1):
    
    #i er en variabel som blir definert i for-løkka
    
    print(i)
    resultat = resultat * i
print("Etter for-løkka er ferdig")


#resultat er kun for å vise hvorfor 0 er med i fakulitet

print(resultat)

