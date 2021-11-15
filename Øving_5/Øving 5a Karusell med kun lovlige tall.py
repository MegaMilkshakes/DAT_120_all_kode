# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 11:42:45 2021

@author: gerry
"""




def hoyden_pa_personen(hoyde):
    if hoyde >= 120:
        print("Denne personen er høy nok til å ta karusellen!")
    else:
        print("Denne personen er for lav til karusellen!")


fortsett = True
while fortsett == True:
    try:
        hoyde = float(input("Skriv inn høyden på personen i cm: "))
        if hoyde < 0: #hvis du prøver å skrive inn negativ tall
            print("Høyden kan ikke være negativ! Prøv igjen: ")
        else:
            fortsett = False
    except ValueError: #hvis du prøver å skrive inn et tegn
        print("Ikke gyldig med tegn! Skriv inn et tall!")
        


hoyden_pa_personen(hoyde)