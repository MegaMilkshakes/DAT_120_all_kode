# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 21:24:07 2021

@author: gerry
"""

#Stolpediagram/søylediagram/barchart
#kakediagram/piechart
#histogram/


import matplotlib.pyplot as plt
import random

karakterer = ["A", "B", "C", "D", "E", "F"]

antall = [5, 15, 40, 24, 18, 26]

#plt.bar(karakterer, antall, color=("red","orange","yellow", "blue", "green", "magenta"))

#plt.pie(antall, labels=karakterer) #antall element i listen må matche


#for flere diagram i samme vindu bruk subplot(antall vertikalt, antall horisontalt, hvilket diagram er dette)

plt.subplot(2, 2, 1)
plt.bar(karakterer, antall, color=("red","orange","yellow", "blue", "green", "magenta"))
plt.title("karakterfordeling, stolper")


plt.subplot(2, 2, 2)
plt.pie(antall, labels=karakterer) #antall element i listen må matche
plt.title("karakterfordeling kakediagram")


#random.random()

plt.subplot(2, 2, 3)
verdier = []
for i in range(20000):
    verdi = random.random() + random.random() + random.random()
    verdier.append(verdi)
plt.hist(verdier, 40)
plt.title("3 tilfeldige tall")
plt.show()
