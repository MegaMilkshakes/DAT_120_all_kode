# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 15:24:10 2021

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


alder = int(input("Skriv inn alderen på personen som kjøper billett: "))

prisen = pris_billett_etter_alder(alder)

print(prisen)
