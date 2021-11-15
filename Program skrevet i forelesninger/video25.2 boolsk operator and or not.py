# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 21:51:15 2021

@author: Gerry
"""

tall_streng = input("Skriv inn et tall for måned: ")
maaned = int(tall_streng)

if maaned < 1 or maaned > 12:
    print("ugyldig måned")
else:
    print("gyldig måned")
    
    