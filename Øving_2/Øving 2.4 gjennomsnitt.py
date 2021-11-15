# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 10:27:57 2021

@author: Gerry
"""



total_tall = int(0)
tall = int(input("Skriv inn et positivt heltall for summering: "))
antall_loops = 0

while tall >= 0:
    antall_loops += 1
    total_tall += + tall
    tall = int(input("Skriv inn nytt positivt heltall for summering: "))
    

    
print("\n","Gjennomsnitt av alle tall er: ", "\n",total_tall/antall_loops)
