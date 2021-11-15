# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 22:35:11 2021

@author: gerry
"""

# SKILLER MELLOM STORE OG SMÅ BOKSTAVER, alt må være prikk likt
# Dictionary, map, assosiativ tabell
# Assosierer nøkler med verdier
# Nøkkel: Det du leter etter, må være immutable
# Verdi: verdien du finner, kan være hva som helst
# Hvordan assisuativ tabell ser ut inni er DAT200 pensum, ikke DAT120


dictionary = dict()
dictionary["Gerry Limos Abrahamsen"] = 45440610 #nøkkel= Gerry Limos Abrahamsen
                                                #verdi = 45440610
dictionary["Anine Jespersen"] = 99462293

dictionary["Bacon Abrahamsen"] = 51687578

#print(dictionary["Gerry Limos Abrahamsen"])

#for nokkel in dictionary:
    #print(nokkel)
    #print(dictionary[nokkel])
    
for nokkel in dictionary: #for å få ting på en linje
    print(nokkel + ": ", end="")
    print(dictionary[nokkel])
    
dict_konstant = {"Gerry Limos Abrahamsen": 45440610, "Anine Jespersen": 99462293}
#kan lage dict som en vanlig variabel
print(dict_konstant)
print(dict_konstant["Anine Jespersen"])

#Kan sjekke om nøkkelen(navnet) er i dictionar med
print("Gerry" in dictionary) #False
print("Gerry Limos Abrahamsen" in dictionary) #True

#kan slette noe i dictionart med del
#del dictionary["Bacon Abrahamsen"]
#dette sletter også verdien som er knyttet til nøkkelen

