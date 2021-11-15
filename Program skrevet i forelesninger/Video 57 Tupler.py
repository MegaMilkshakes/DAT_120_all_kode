# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 21:03:36 2021

@author: gerry
"""


#Nesten identisk med ei liste
#Forskjellen er at en Tupler er immutable, kan altså ikke endres etter bruk

#slik lages en liste:
liste = [1, 2, 3, 4, 5]


#slik lages en Tupler:
tuppel = (1, 2, 3, 4, 5)

variabel = (5) #dette blir en int i variabel exploreren, altså tolker 
#paranteser som en mattematisk parantes
variabel1 = (5,) #dette blir en tuple med 1 element
#, forskjellen er komma(,) da blir ikke
#paranteser tolket som en mattematisk parantes

tuppel[2] = 10 #dette gir feilmelding da en tuple ikke kan endres på
#kan heller ikke appende et tuple.