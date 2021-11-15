# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 19:33:28 2021

@author: gerry
"""



import numpy as np

nullere = np.zeros(5)

for i in np.arange(1, 5, 0.1):
    print(f"{i:5.2f}")
    
    
#linspace start, stopp og antall istedenfor steg
test = np.linspace(1, 10, 4) #lager en array fra 1 til 10 men med antall 4 jevnt
#fordelt
print(test)

oddetall = np.array([1, 3, 5, 7, 9])
print(oddetall)

enere = np.ones(5)
print(enere)

#lage en matrise
matrise = np.zeros((4, 3))
print(matrise)

print("\n")

#matrise med flere lister, de YTTRE listene må være like lange
matrise2 = np.array([[1, 2, 3], [2, 2, 2], [3, 2, 1]])
print(matrise2)

#spør etter form på matrisen
print(matrise2.shape) #3, 3

#gange med en vanlig liste repeterer listen x-antall ganger
liste = [2, 3]
print(liste)
print(liste*5)
#gange med array ganger hver verdi x-antall ganger
print(oddetall)
print(oddetall*5)
#samme med + og minus. den utgjør dette per verdi/posisjon

#kan plusse/gange/dele/minuse 2 arrays sålenge de er samme lengde
#da plusser/ganger/deler/minuser du første element med første element
#andre med andre, tredje med tredje element osv
test3 = np.array([2, 3, 4, 5, 6])
print(oddetall)
print(test3)
print(oddetall + test3)
print(oddetall * test3)

matrise3 = np.array([[2, 0, 0], [0, 2, 0], [0, 0, 2]])
print(matrise2 * matrise3) #her ganges element for element
print(matrise2 @ matrise3) #her ganges matrise med matrise
#standard matisemultiplikasjon

#Andre numpy kommandoer som tar element for element i en array
print(np.sin(matrise2))
#ta indeks på matrise (sjekk hva som står i hvilken posisjon)
print(matrise2[0, 1]) #dette gir 2 pga posisjon 0 i rekken, i rekke 1. 
#tell fra 0
#for en hel rad, bortover og nedover
matrise4 = np.array([[1 ,2 ,3],[4, 5, 6],[7, 8, 9]])
print(matrise4[0,:]) #bortover
print(matrise4[:, 0]) #nedover
print(matrise4[0:2, 0:2]) #deler av matrisen