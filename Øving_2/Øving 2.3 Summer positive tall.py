# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 10:04:18 2021

@author: Gerry
"""


total_tall = int(0)
tall = int(input("Skriv inn et positivt heltall for summering: "))

while tall >= 0:
    total_tall += + tall
    tall = int(input("Skriv inn nytt positivt heltall for summering: "))
    
print("Den totale summen av tall som er skrevet inn er: ", "\n", total_tall)

