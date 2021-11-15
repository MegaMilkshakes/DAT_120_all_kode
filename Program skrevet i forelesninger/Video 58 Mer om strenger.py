# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 21:35:05 2021

@author: gerry
"""


#en liste er en samling av verdier
#en streng er en samling av tegn, foreksempel en settning er mange bokstaver
streng = "En tekst med noen ord"

#kan ikke endre en streng. den er immutable
 #streng[3] = "g"
#denne får en feilmelding siden streng er immutable

ordliste = streng.split()#uten parameter fører til splitt i hvert whitespace
#whitespace = " ", "\n", "\t"0
print(ordliste)

streng = "      verdi1;verdi2;verdi3;\n"
print(streng)
streng = streng.strip()
print(streng)
#streng.strip() fjerner kun fra start og slutt?
streng = streng.strip(";")
print(streng)

splittet = streng.split(";") #her splittes hvert ord ved ;
#kver "verdi" blir en liste. [verdi1, verdi2, verdi3]
print(splittet)

