# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 20:51:53 2021

@author: Gerry
"""

tall_streng = input("Skriv inn et heltall: ")
tallet = 6
tallet == int(tall_streng)



if tallet < 0:
    print("Tallet er negativt")
    print("Fortsatt endel av \"if-blokken\"")
    print("Avslutt blokken med å fjerne mellomrommene i starten av settningen")
    
#video 21 elif lære
elif tallet == 0:
    print("Tallet er 0")
    
else:
    print("Tallet er ikke negativt")
    print("Fortsatt i blokken \"else\"")
    print("Samme som sist, avslutt blokken med å fjerne mellomrom")
print("denne settningen skrives uansett if eller else tall da den kommer utenom blokkene, denne er en egen settning i koden, ikke del av tidligere if og else")

