# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 17:20:34 2021

@author: gerry
"""


fortsetter = True
while fortsetter: 
    lesefil = input("Skriv inn navn på filen med e-poster: ")     
    try:
        lesefil = open(lesefil, "r", encoding="UTF8")
        fortsetter = False
    except FileNotFoundError:
        print("Fila finnes ikke!")
        print("Prøv på nytt.")
        
    
skrivefil = input("Skriv inn navn på filen vi skal skrive til: ")
skrivefil = open(skrivefil, "w", encoding="UTF8")

for linje in lesefil:
    linje1 = linje.strip()
    linje1.find("From:")
    if linje1.find("From:") != -1:
        linje1.find("<")
        if linje.find("<") != -1:
            posisjon1 = 1 + (int(linje1.find("<")))
            linje1.find(">")
            if linje.find(">") != -1:
                posisjon2 = (int(linje1.find(">")))
                print(linje1[posisjon1 : posisjon2])
                skrivefil.write(linje1[posisjon1 : posisjon2] + "\n")
        
        
        
lesefil.close()
skrivefil.close()

# hadoop_1m_uft.txt
# eposter_skrevet.txt