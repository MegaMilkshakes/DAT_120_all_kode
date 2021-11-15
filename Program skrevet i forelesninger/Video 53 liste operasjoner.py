# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 20:51:43 2021

@author: gerry
"""

#Liste operasjoner

#pluss

liste1 = [1, 2, 3, 4, 5]
print(liste1)

liste2 = [9, 10, 11, 12]
print(liste2)

liste3 = liste1 + liste2
print(liste3)

#gange blir brukt for å repetere lister x-antall ganger
liste4 = [0, 1]*5
print(liste4)

#kan ikke gange lister med andre lister.
#kun liste ganger med et heltall

#sjekke minimum i liste
print(min(liste1))

#sjekke maximum i lista
print(max(liste1))

#kan kun ta min og max av innhold som kan sammenlignes
#min/max av lister med tall og bokstav/tekst gir ValueError

#bruk index for å finne posisjonen til det du vil
print(liste3.index(10))
#tallet 10 står i 6 posisjon i listen, teller fra 0.

#slett ting fra listen med remove. verdi eller index
liste3.remove(9)
print(liste3)

#slette en index/posisjon
del liste3[5] #sletter 5posisjon, alstå 10 i dette tilfelle
print(liste3)

#sorter liste med sort, kan kun sortere sammenlignbare tall
#nesten som max/min, ingen tekst/bokstav/streng
#bruker ingen parameter sort()
liste5 = [3,6,1,7,8,9,2,2]
print(liste5)
liste5.sort()
print(liste5)

#reverse brukes til å snu listen
#bruker ingen parameter reverse()
print(liste1)
liste1.reverse()
print(liste1)
