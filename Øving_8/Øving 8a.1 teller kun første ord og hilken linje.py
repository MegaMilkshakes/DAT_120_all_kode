# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 10:18:26 2021

@author: gerry
"""



ordliste = dict()
linjeteller = 0

with open("oving_1_rein_tekst.txt", "r", encoding="UTF8") as fila:
    for linje in fila:
        linjeteller += 1
        ordene = linje.split()
        for ordet in ordene:
            ordet = ordet.strip(".")
            ordet = ordet.lower()
            if ordet in ordliste:
                teller = ordliste[ordet]
                teller += 1
                ordliste[ordet] = teller
            else:
                ordliste[ordet] = 1
                print(f"Ordet \"{ordet}\" forekommer først på linje {linjeteller}")

fila.close()
