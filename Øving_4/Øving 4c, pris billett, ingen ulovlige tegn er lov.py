# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 15:53:07 2021

@author: Gerry
"""



def pris_billett_etter_alder(alder):
    if alder < 18:
        prisen = "Billetten koster 20kr for folk under 18år"
    elif alder >= 67:
        prisen = "Billetten koster 20kr for folk som er 67år eller eldre"
    else:
        prisen = "Billetten har normalpris 40kr"
    return prisen


fortsett = True
while fortsett == True:
    try:
        alder = int(input("Skriv inn alderen på personen som kjøper billett: "))
        if alder < 0:
            print("Alder kan ikke være negativt!")
        else: fortsett = False
    except ValueError:
        print("Skriv inn et tall!")
        

prisen = pris_billett_etter_alder(alder)

print(prisen)
