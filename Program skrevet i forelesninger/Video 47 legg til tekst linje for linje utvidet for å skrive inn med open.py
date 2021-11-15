# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 18:53:41 2021

@author: Gerry
"""


teksten = ""
tekstlinje = input("Skriv inn første linje: ")
fila = open("tekstfila.txt", "w", encoding="UTF8")
while tekstlinje != "":
    fila.write(tekstlinje + "\n")
    tekstlinje = input("Skriv inn neste linje: ")
fila.close()





#    teksten += tekstlinje + "\n"
#    tekstlinje = input("Skriv inn neste linje: ")
#print("Den endelige teksten ble: ")
#print(teksten)
