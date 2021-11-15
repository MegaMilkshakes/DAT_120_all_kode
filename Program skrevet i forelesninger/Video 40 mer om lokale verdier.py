# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 18:26:12 2021

@author: Gerry
"""




def skriv_firkant(høyde, bredde, tegn="*"):
    for j in range(høyde):
        for i in range(bredde):
            print(tegn, end="")
        print()
    

bruker_høyde = int(input("Høyde: "))
bruker_bredde = int(input("Bredde: "))
bruker_tegn = input("Skriv in tegn firkant skal lages av: ")


skriv_firkant(7,9)
print("\n ny firkant \n")
skriv_firkant(bruker_høyde,bruker_bredde, bruker_tegn)
print("\n ""Ferdig")
