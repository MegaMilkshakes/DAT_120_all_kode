# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 13:52:08 2021

@author: gerry
"""



class Sporsmal:
    def __init__(self, tekst, svar):
        self.tekst = tekst
        self.svar = svar
    
    def __str__(self):
        return self.tekst
        
sporsmal_tekst = [
    "Hvilken farge har epler? \n(1) Rød/Grønn\n(2) Lilla\n(3) Oransj\n\n",
    "Hvilken farge har Bananer?\n(1) Blå\n(2) Sølv\n(3) Gul\n\n",
    "Hvilken farge har Jordbær?\n(1) Gul\n(2) Rød\n(3) Blå\n\n"
    ]


sporsmaler = [
    Sporsmal(sporsmal_tekst[0], "1"),
    Sporsmal(sporsmal_tekst[1], "3"),
    Sporsmal(sporsmal_tekst[2], "2"),
    ]

def spill_spillet(sporsmaler):
    resultat = 0
    for sporsmal in sporsmaler:
        print(sporsmal)
        svar = input("Ditt Svar:")
        if svar == sporsmal.svar:
            resultat += 1
            print("Svaret ditt er riktig!")
        else:
            print("Svaret ditt er feil!")
    print("Du fikk " + str(resultat) + " av " + str(len(sporsmaler)) + " riktig!")
    
spill_spillet(sporsmaler)