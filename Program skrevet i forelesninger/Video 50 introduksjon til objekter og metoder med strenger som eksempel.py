# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 20:07:25 2021

@author: Gerry
"""

streng1 = "En streng med Flere ord og Noen store bokstaver"

streng2 = "En annen streng med andre ord enn den første strengen"

streng1.upper() #skriver streng1 med STORE BOKSTAVER
#men endrer ikke variabelen

streng1_store_bokstaver = streng1.upper()

streng1.lower()

streng2.upper()

streng3 = "\t\tTeststreng med noen ord \n\n"
print(streng3)

#streng3.strip() fjerner tomme plasser før og etter i strengen

streng_uten_whitespace = streng3.strip()
print(streng_uten_whitespace)

streng1.find("ord")#finner ordet ord i streng1, ordet
#begynner på plass nr20 i rekken, derfor får jeg 20 som output 
#om jeg skriver streng1.find("ord") i consol, eller printer verdien

streng1.find("test")#søker etter ord som ikke finnes gir
#verdi -1 om jeg skriver i consol eller printer verdien

streng3[0]#søker etter hva som står i 0 posisjon.
#HUSK Pyhon starter å telle på 0

#DELSTRENG[Fra og med indeks, til og ikke med indeks]
streng3[5:15]#viser hva som er skrevet i posisjon 
#fra og med 5 til men ikke med 15
