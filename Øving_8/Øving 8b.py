# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 11:00:18 2021

@author: gerry
"""


import random


def fleip_eller_fakta():
    uttalelse = []
    uttalelse.append(["Tigere har striper", "Fakta"])
    uttalelse.append(["Jeg har 2 katter", "Fakta"])
    uttalelse.append(["Jeg har 1 hund", "Fleip"])
    uttalelse.append(["Kattene mine er oransj", "Fleip"])
    return uttalelse

def spill_fleip_eller_fakta():
    fef_uttalelse = fleip_eller_fakta()
    random.shuffle(fef_uttalelse)    
    resultat = 0
    for s in fef_uttalelse:
        print("Fleip eller fakta: " + s[0])
        svar = input("Fleip eller Fakta: ")
        if svar == s[1]:
            print("Riktig!")
            resultat += 1
        else:
            print("Ikke riktig =(")
        
    print("Ditt resultat ble: " + str(resultat))

spill_fleip_eller_fakta()