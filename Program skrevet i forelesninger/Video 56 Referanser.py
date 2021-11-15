# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 20:20:11 2021

@author: gerry
"""

#hva skjer når du tilordner en variabel

liste1 = [1, 2, 3, 4, 5]
print(liste1)
liste2 = [11, 12, 13, 14]
print(liste2)
liste3 = liste1
print(liste3)

liste1.append(6)
print(f"{liste1} \n{liste3}")
#her ser vi endring i liste1 fører til endring automatisk i liste3
#siden liste3 refererer til akkurat sammen innhold som liste1
liste3[2] = 7
print(liste3)
#endringen skjer lik om vi endrer liste3, endringen kommer i liste1 automatisk

#for å unngå dette må vi kopiere listen
liste_kopi = liste1[ : ]
print(liste_kopi) #her er kopi lik liste1
print(liste1)
liste1.append(10)
print(liste1)
print(liste_kopi)
#dette skjer fordi liste_kopi er et annet objekt, mens liste1 = liste3 uansett

