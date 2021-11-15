# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 18:07:47 2021

@author: Gerry
"""


def skriv_ei_linje_skraa_venstre(storrelse, x, y):
    if y == storrelse-x-1:
            print("*", end="")
    else:
        print(" ", end="")


def skriv_ei_linje_skraa_hoyre(x, y):
        if y == x+1:
            print("*", end="")
        else:
            print(" ", end="")


def skriv_overste_del(storrelse, y):
    for x in range(storrelse):
        skriv_ei_linje_skraa_venstre(storrelse, x, y)
    for x in range(storrelse-1):
        skriv_ei_linje_skraa_hoyre(x, y)
    print()

    
    
    
storrelse = int(input("Hvor stor skal diamanten være? "))

for y in range(storrelse):
    skriv_overste_del(storrelse, y)
    
for y in range(storrelse-2,-1,-1):
    skriv_overste_del(storrelse, y)
    

