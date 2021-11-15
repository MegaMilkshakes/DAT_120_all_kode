# -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 14:51:03 2021

@author: gerry
"""



#enhetstest eksempel
#gjør koden testbar
def er_tenaaring(alder): #skill ut input og print settningene
    if alder >= 13 and alder < 18: #endrer jeg til <= før 18 vil testen test_tenaaring faile
        return True
    else:
        return False

        #Originalkoden
#tall_streng = input("Skriv inn en alder: ")
#alder = int(tall_streng)
#if alder >= 13 and alder < 18:
#    print("Personen er tenåring")
#else:
#    print("Personen er ikke tenåring")
    
if __name__ == "__main__":
    tall_streng = input("Skriv inn en alder: ")
    alder = int(tall_streng)
    if er_tenaaring(alder):
        print("Personen er tenåring")
    else:
        print("Personen er ikke tenåring")

    
#Prinsipp for testing
#Bør teste flere verdier
#Bør teste alle veier gjennom programmet, test en alder under 13, over 18
    #mellom 13 & 18
#Bør teste grenseverdier, 12, 13 & 17, 18
#Bør teste feilhåndteringer

