# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 19:58:22 2021

@author: gerry
"""

#Ordteller for tekstfil;
# Les inn ei tekstfil
# Finn alle ordene
# Tell antall forekomster av hvert ord

ordliste = dict()
with open("oving_1_rein_tekst.txt", "r", encoding="UTF8") as fila:
    for linje in fila:
        ordene = linje.split()
        for ordet in ordene:
            ordet = ordet.lower()
            if ordet in ordliste:
                teller = ordliste[ordet]
                teller += 1
                ordliste[ordet] = teller
            else:
                ordliste[ordet] = 1
    for ordet in ordliste:
        print(f"ordet {ordet} forekommer {ordliste[ordet]} antall ganger")

            
            
            
            
            
#ordet = nøkkelen
#antall forekomster = verdien
