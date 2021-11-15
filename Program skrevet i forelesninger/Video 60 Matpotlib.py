# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 20:38:18 2021

@author: gerry
"""
import matplotlib.pyplot as plt
import numpy as np

#plott funksjonen f(x) = x**2
#lag 2 lister for å plotte. x-koordinater, og y-koordinater
x_koordinater = np.linspace(0, 10, 11)
y_koordinater = x_koordinater**2
print(f"{x_koordinater}, \n, {y_koordinater}")


#kan plotte flere figurer i samme diagram

y_koordinater2 = x_koordinater*2

plt.plot(x_koordinater, y_koordinater, "o-", label="x i andre")#o i siste parameter betyr
#kuler i grafen, - betyr du tegner streken mellom kulepunktene
#kan bruke * istedenfor o, 
plt.plot(x_koordinater, y_koordinater2, "*-", label="x*2")
plt.title("Enkle figurer")
plt.xlabel("Verdi")
plt.ylabel("Resultat")
plt.legend() #for å vise label
plt.grid(True) #for å lage grid i figuren
#plt.savefig("flere_figurer.pdf")
plt.show()
