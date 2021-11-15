# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 13:16:15 2021

@author: gerry
"""



#lager en tom liste
liste = list()

#Lager en liste med oppgitte elementer, er tallene 1, 2, 3, 4, 5
liste2 = [1, 2, 3, 4, 5]

#Skriver ut lengden på lista
print(len(liste2))

#legger til et element i listen
liste.append(4)
liste.append(5)

#lister har en fast rekkefølge, her printer jeg element
# 2 (fra 0) fra liste2
print(liste2[2])

#elementet trenger ikke være et tall
liste.append("En streng")
liste.append(5.5)
liste.append(liste2)
print(len(liste))

#for liste inni liste kan du "søke" hvilke pos i indre liste
#med å bruke 2 indekser
print(liste[4]) #printer listen inni listen
print(liste[4][2]) #printer element2 fra indre listen

#endre en liste etter den eg laget
liste2[2] = 9 #endrer element 2 i listen til et 9tall
print(liste2)

#telle element fra andre enden
print(liste2[-2])
print(liste2[-3])

#legg inn ett tall midt i, her legges tallet 10 inn i 4posisjon
#og forskyver alt etter
liste2.insert(4, 10)
print(liste2)

