# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 21:25:50 2021

@author: gerry
"""



for i in range(1, 10):
    print(i)
    
print("\n")
liste = [1,3,5,7,9]
for i in liste:
    print(i)
print("\n")

for tall in liste:
    tall = tall*2
    print(tall)
print("\n")
print(liste)
print("\n")

#in operator
if 5 in liste:
    print("5 er med i listen!")
    
#forbedret eksempel
element = int(input("Skriv inn et tall for å se om den er i lista: "))
if element in liste:
    print(f"{element} er med i listen")
    #print("Tallet " + str(element) + " er med i listen")
else:
    print(f"{element} er ikke med i listen")
    #print("Tallet " + str(element) + " er ikke med i listen")
        
    
#eksempel med enumerate, finner indeks og element/verdien
for indeks, element in enumerate(liste):
    print(f"element {element} ligger på indeks {indeks}")
