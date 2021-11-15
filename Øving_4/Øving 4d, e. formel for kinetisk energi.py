# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 16:07:35 2021

@author: Gerry
"""




def kinetisk_energi_formel(masse, fart):
    KE = 1/2*masse*fart**2
    return KE

masse = float(input("Skriv inn massen til objektet i kg: "))
fart = float(input("Skriv inn farten til objektet i m/s: "))

kinetisk_energi = kinetisk_energi_formel(masse, fart)

print(f"Den kinetiske energien for objektet er: {kinetisk_energi} Joule")

