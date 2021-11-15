# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 20:50:12 2021

@author: gerry
"""



import matplotlib.pyplot as plt
import numpy as np

#lag listene først tomme, så kan du appende til disse etterpå
tidspunkt = []
tid_siden_start = []
trykk_absolutt = []
temperatur = []

lesefil = open("trykk_og_temperaturlogg.csv", "r", encoding="UTF8")

for linje in lesefil:
    linje = linje.strip()
    linje.find("Dato")
    if linje.find("Dato") != 0:
        lesefil1 = linje.split(";")
        lesefil1[0] = lesefil1[0].replace(",",".")
        #lesefil[0] = lesefil[0].replace(":",".")
        #lesefil[0] = lesefil[0].replace(" ",".")
        tidspunkt.append(lesefil1[0])
        lesefil1[1] = lesefil1[1].replace(",",".")
        tid_siden_start.append(float(lesefil1[1]))
        lesefil1[3] = lesefil1[3].replace(",",".")
        trykk_absolutt.append(float(lesefil1[3]))
        lesefil1[4] = lesefil1[4].replace(",",".")
        lesefil1[4] = lesefil1[4].strip()
        temperatur.append(float(lesefil1[4]))

#tidspunkt = np.array(tidspunkt)
#tid_siden_start = np.array(tid_siden_start)
#trykk_absolutt = np.array(trykk_absolutt)
#temperatur = np.array(temperatur)


plt.subplot(3, 1, 1)
plt.title("Trykk Absolutt")
plt.plot(tidspunkt, trykk_absolutt)


plt.subplot(3, 1, 2)
plt.title("Temperatur")
plt.plot(tidspunkt, temperatur)


plt.subplot(3, 1, 3)    
plt.title("Histogram")
plt.hist(temperatur, 200)

for linje2 in range(len(tid_siden_start)-1): #dette gjøres for å bruke indeks
                                            #ikke verdien
    if tid_siden_start[int(linje2)+1] - tid_siden_start[int(linje2)] != 10:
        print(tid_siden_start[int(linje2)])
        print(tidspunkt[int(linje2)])

lesefil.close()

