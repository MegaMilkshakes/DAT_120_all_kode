# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 18:52:59 2021

@author: Gerry
"""




def skriv_firkant(størrelse):
    for j in range(størrelse):
        for i in range(størrelse):
            print("*", end="")
        print()
    

høyde = int(input("Høyde: "))
#bredde = int(input("Bredde: "))


skriv_firkant(3)
print("\n ny firkant \n")
skriv_firkant(høyde)
print("Ferdig")
