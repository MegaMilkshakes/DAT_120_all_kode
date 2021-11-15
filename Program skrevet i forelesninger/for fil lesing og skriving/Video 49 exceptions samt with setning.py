# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 19:45:56 2021

@author: Gerry
"""

filnavn = input("Hvilken fil skal leses? ")
try:
    with open(filnavn, "r", encoding="UTF8") as fila:
        summen = 0
        for linje in fila:
            summen += int(linje)
        fila.close()
        print(f"Summen ble: {summen}")
except FileNotFoundError:
    print("Finner ikke denne fila!")
except ValueError:
    print("Fila inneholder noe med feil format, ikke tall!")
except:
    print("En annen feil har oppstått!")
#finally:
    #fila.close()

 