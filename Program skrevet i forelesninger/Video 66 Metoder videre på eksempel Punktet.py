# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 19:02:56 2021

@author: gerry
"""


#Klasse: punkt

class Punkt:  #start med stor bokstav, skiller klasse fra funksjoner og variabler
    #konstruktør
    def __init__(self, start_x=0, start_y=0):
        self.x_koordinat = start_x
        self.y_koordinat = start_y
     
    #Mutator    
    def flytt(self, delta_x, delta_y):
        self.x_koordinat += delta_x
        self.y_koordinat += delta_y
        
    #Query    
    def __str__(self): #brukes til brukeren
        return f"Punkt: ({self.x_koordinat}, {self.y_koordinat})"

    #Query
    def __repr__(self): #brukes til systemet
        return f"Punkt ({self.x_koordinat}, {self.y_koordinat})"


if __name__ == "__main__":
    punkt1 = Punkt(2, 3)
    print(punkt1)
    punkt2 = Punkt()
    print(punkt2)
    punkt1.flytt(2, -1)
    print(punkt1)