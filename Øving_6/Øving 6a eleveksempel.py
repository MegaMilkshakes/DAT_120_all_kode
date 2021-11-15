# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 18:50:13 2021

@author: gerry
"""



import matplotlib.pyplot as plt, sys

lesefil = open("trykk_og_temperaturlogg.csv", "r", encoding="UTF8")
linje = lesefil.readline()
tidspunkt = []
tid_siden_start = []
trykk_absolutt = []
temperatur = []

def comma_finder(index):
    o_write = lesefil[index].find(",")
    while o_write >= 0:
        lesefil[index] = lesefil[index].replace(",",".")
        o_write = -1
        
def writer(index, type):
    lesefil[index].strip()
    while lesefil[index] != "":
        type.append(float(lesefil[index]))
        break
    
try:
    for linje in lesefil:
        linje.strip()
        linje.find("Dato")
        if linje.find("Dato") != 0:
            lesefil = linje.split(";")
            tidspunkt.append(lesefil[0])
            tid_siden_start.append(float(lesefil[1]))
            comma_finder(2)
            writer(2, trykk_absolutt)
            comma_finder(4)
            writer(4, temperatur)
except ValueError:
    print("Noe gikk galt")
    sys.exit()
    
try:
    #plt.subplot(3, 1, 1)
    #plt.title("Trykk Absolutt")
    #plt.plot(tidspunkt, trykk_absolutt)
    plt.subplot(3, 1, 2)
    plt.title("Temperatur")
    plt.plot(tidspunkt, temperatur)
    plt.subplot(3, 1, 3)    
    plt.title("Histogram")
    plt.hist(temperatur, 200)
except ValueError:
    print("Fant en verdi jeg ikke kunne plotte")
    