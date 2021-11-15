# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 17:17:05 2021

@author: gerry
"""




class Sporsmal:
    def __init__(self, tekst, svar):
        self.tekst = tekst
        self.svar = svar
    
    def __str__(self):
        return self.tekst
    
    def korrekt_svar_tekst(self):
        return self.sporsmal.svar


def les_fil():
    lesefil = open("sporsmaalsfil.txt", "r", encoding="UTF8")
    for linje in lesefil:
        linje = linje.strip()
        sporsmal_tekst.append(linje)
    lesefil.close()

    
def spill_spillet(sporsmaler):
    resultat1 = 0
    resultat2 = 0
    for sporsmal in sporsmaler:
        print("\n")
        print(sporsmal)
        svar1 = input("Spilller1 sitt svar:")
        svar2 = input("Spiller2 sitt svar:")
        if svar1 == sporsmal.svar:
            resultat1 += 1
        if svar2 == sporsmal.svar:
            resultat2 += 1
        print("\nRett svaralternativ er: " + sporsmal.svar)
        if svar1 == sporsmal.svar:
            print("Spiller1: Korrekt")
        else:
            print("Spiller1: Feil")
        if svar2 == sporsmal.svar:
            print("Spiller2: Korrekt")
        else:
            print("Spiller2: Feil")
        
          
    print("Spiller 1 fikk " + str(resultat1) + " av " + str(len(sporsmaler)) + " riktig!")
    print("Spiller 2 fikk " + str(resultat2) + " av " + str(len(sporsmaler)) + " riktig!")

    

if __name__ == "__main__":
    sporsmal_tekst = []
        
    les_fil()
    
    sporsmaler = [
        Sporsmal(sporsmal_tekst[0], "2"),
        Sporsmal(sporsmal_tekst[1], "1"),
        Sporsmal(sporsmal_tekst[2], "0"),
        Sporsmal(sporsmal_tekst[3], "2"),
        Sporsmal(sporsmal_tekst[4], "1"),
        Sporsmal(sporsmal_tekst[5], "1"),
        Sporsmal(sporsmal_tekst[6], "3"),
        Sporsmal(sporsmal_tekst[7], "1"),
        ]
    
    spill_spillet(sporsmaler)