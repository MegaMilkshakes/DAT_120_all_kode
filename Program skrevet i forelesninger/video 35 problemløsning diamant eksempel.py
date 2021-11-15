# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 08:56:07 2021

@author: Gerry
"""

storrelse = int(input("Hvor stor skal diamanten være? "))

for y in range(storrelse):
    for x in range(storrelse):
        if y == storrelse-x-1:
            print("*", end="")
        else:
            print(" ", end="")
    for x in range(storrelse-1):
        if y == x+1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
    
for y in range(storrelse-2,-1,-1):
    for x in range(storrelse):
        if y == storrelse-x-1:
            print("*", end="")
        else:
            print(" ", end="")
    for x in range(storrelse-1):
        if y == x+1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

