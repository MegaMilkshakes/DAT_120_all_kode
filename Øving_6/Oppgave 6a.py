# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 12:32:33 2021

@author: gerry
"""

import matplotlib.pyplot as plt
import numpy as np
import random as rnd
import sys

r_fil = open("trykk_og_temperaturlogg.csv", "r", encoding="UTF8")
linje = r_fil.readline()
dato_og_tid = []
tid_siden_start = []
trykk_baro = []
trykk_abso = []
temp = []

for linje in r_fil:
    r_liste = linje.split(";")
    dato_og_tid.append(r_liste[0])
    tid_siden_start.append(r_liste[1])
    trykk_baro.append(r_liste[2])
    trykk_abso.append([3])
    temp.append(r_liste[4])

arr_tid_og_dato = np.array(tid_siden_start)
arr_tid_siden_start = np.array(tid_siden_start)
arr_trykk_baro = np.array(trykk_baro)
arr_trykk_abso = np.array(trykk_abso)

plt.plot(arr_tid_siden_start, arr_trykk_abso, "-", label = "Trykk")
plt.plot(arr_tid_siden_start, "-", label = "Temperatur")
plt.xlabel("Tid")
plt.ylabel("Trykk")
plt.legend()
plt.show()
r_fil.close()
