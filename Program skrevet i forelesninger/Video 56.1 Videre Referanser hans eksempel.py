# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 20:47:04 2021

@author: gerry
"""


def endrer_liste(liste):
    liste.append(10)
    liste.append(12)
    liste = [3, 4, 5] # denne tilordningen har ingen konsekvens for noe utenfor
    #denne funksjonen, dette er en lokal variabel, ikke global
    print(liste)
    
if __name__ == "__main__":
    liste1 = [2, 4, 6, 8]
    print(liste1)
    endrer_liste(liste1)
    print(liste1)
    
