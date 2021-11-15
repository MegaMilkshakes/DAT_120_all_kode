# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 17:50:31 2021

@author: Gerry
"""

hoyde = int(input("Høyde: "))
#bredde = int(input("Bredde: "))


for ii in range(hoyde):
    for i in range(ii+1):
        print("*", end="")
    print()