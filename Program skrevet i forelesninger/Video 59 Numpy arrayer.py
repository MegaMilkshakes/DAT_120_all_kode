# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 19:09:47 2021

@author: gerry
"""



#Ligner på ei liste
#Laget mer for matematikk
#import numpy as np, eller bare import numpy
#skriver jeg as np er np forkortelsen når jeg skal skrive den i koden

import numpy as np

array = np.zeros(5) #skriver en array [0., 0., 0., 0., 0.]
print(array)
array[2] = 5
print(array)

#en array kan endres på (er mutable), men lengden kan ikke endres 
#etter den er laget

#om jeg appender en array lages en ny variabel, den originale listen kan ikke
#forlenges

#stigende tall lages slik
stigende = np.arange(7)
print(stigende)
stigende = np.arange(1, 7)
print(stigende)
stigende = np.arange(1, 7, 2)
print(stigende)
#arange aksepterer flyttall
stigende = np.arange(1, 7, 0.5)
print(stigende)

for i in np.arange(1, 5, 0.1):
    print(f"{i:5.2f}")
    
