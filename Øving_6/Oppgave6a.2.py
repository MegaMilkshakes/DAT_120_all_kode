# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 11:12:34 2021

@author: gerry
"""


import matplotlib.pyplot as plt
import numpy as np

tidspunkt = []
tid_siden_start = []
trykk_absolutt = []
temperatur = []

lesefil = open("trykk_og_temperaturlogg.csv", "r", encoding="UTF8")

for linje in lesefil:
    lesefil = linje.split(";")
    tidspunkt.append(lesefil[0])
    tid_siden_start.append(lesefil[1])
    trykk_absolutt.append(lesefil[3])
    temperatur.append(lesefil[4])
    
#tidspunkt = np.array(tidspunkt)
#tid_siden_start = np.array(tid_siden_start)
#trykk_absolutt = np.array(trykk_absolutt)
#temperatur = np.array(temperatur)


plt.subplot(3, 1, 1)
plt.plot(tidspunkt, trykk_absolutt)
plt.subplot(3, 1, 2)
plt.plot(tidspunkt, temperatur)

plt.subplot(3, 1, 3)    
plt.hist(temperatur, 200)

lesefil.close()

