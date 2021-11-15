# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 18:08:34 2021

@author: Gerry
"""

fortsetter = True


while fortsetter:
prosentscore = int(input("Skriv inn en prosentscore: "))
#ønsker å gjøre testen her
    if prosentscore >0:
        fortsetter = False
        break
    if prosentscore >= 90:
        print("A")
    elif prosentscore >= 80:
        print("B")
    elif prosentscore >= 60:
        print("C")
    elif prosentscore >= 50:
        print("D")
    elif prosentscore >= 40:
        print("E")
    else:
        print("F")
