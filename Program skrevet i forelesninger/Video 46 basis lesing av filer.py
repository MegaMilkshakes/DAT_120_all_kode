# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 18:18:45 2021

@author: Gerry
"""
#       filnavn, modus, encoding for å unngå rar øæå og andre tegn
#open("temp.py", "r", encoding="UTF8") 


filnavn = input("Hvilken fil skal leses? ")
fila = open(filnavn, "r", encoding="UTF8")
for linje in fila:
    print(linje, end="")
fila.close()

