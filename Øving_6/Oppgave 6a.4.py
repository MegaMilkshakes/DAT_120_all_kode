# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 15:35:26 2021

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
    linje = linje.strip()
    linje.find("Dato")
    if linje.find("Dato") != 0:
        lesefil = linje.split(";")
        lesefil[0] = lesefil[0].replace(",",".")
        #lesefil[0] = lesefil[0].replace(":",".")
        #lesefil[0] = lesefil[0].replace(" ",".")
        tidspunkt.append(lesefil[0])
        lesefil[1] = lesefil[1].replace(",",".")
        tid_siden_start.append(float(lesefil[1]))
        lesefil[3] = lesefil[3].replace(",",".")
        trykk_absolutt.append(float(lesefil[3]))
        lesefil[4] = lesefil[4].replace(",",".")
        lesefil[4] = lesefil[4].strip()
        temperatur.append(float(lesefil[4]))


#tidspunkt = np.array(tidspunkt)
#tid_siden_start = np.array(tid_siden_start)
#trykk_absolutt = np.array(trykk_absolutt)
#temperatur = np.array(temperatur)


#plt.subplot(3, 1, 1)
plt.title("Trykk Absolutt")
plt.plot(tidspunkt, trykk_absolutt)


#plt.subplot(3, 1, 2)
#plt.title("Temperatur")
#plt.plot(tidspunkt, temperatur)


#plt.subplot(3, 1, 3)    
#plt.title("Histogram")
#plt.hist(temperatur, 200)


for linje2 in range(len(tid_siden_start)-1):
    if tid_siden_start[int(linje2)+1] - tid_siden_start[int(linje2)] != 10:
        print(tid_siden_start[int(linje2)])
        print(tidspunkt[int(linje2)])
        