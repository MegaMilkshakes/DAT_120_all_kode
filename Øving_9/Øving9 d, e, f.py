# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 16:32:24 2021

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
    resultat = 0
    for sporsmal in sporsmaler:
        print(sporsmal)
        svar = input("Ditt Svar:")
        if svar == sporsmal.svar:
            resultat += 1
            print("Svaret ditt er riktig!")
        else:
            print("Svaret ditt er feil! \nRett svar er alternativ: " + sporsmal.svar + "\n")
    print("Du fikk " + str(resultat) + " av " + str(len(sporsmaler)) + " riktig!")
    

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