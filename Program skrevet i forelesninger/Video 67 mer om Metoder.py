# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 19:40:40 2021

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
    def avstand_origo(self):
        return (self.x_koordinat**2 + self.y_koordinat**2)**0.5
    
    # Avstand mellom to punkter, antar at det som kommer inn er et punkt
    def avstand(self, annet_punkt):
        xdiff = self.x_koordinat - annet_punkt.x_koordinat
        ydiff = self.y_koordinat - annet_punkt.y_koordinat
        return (xdiff**2 + ydiff**2)**0.5
        
        
    #Query    
    def __str__(self): #brukes til brukeren
        return f"Punkt: ({self.x_koordinat}, {self.y_koordinat})"

    #Query
    def __repr__(self): #brukes til systemet
        return f"Punkt ({self.x_koordinat}, {self.y_koordinat})"

# Skriver dette som en vanlig funksjon (Avstand mellom to punkter som er ovenfor)
def avstand_punkter(punkt1, punkt2):
    xdiff = punkt1.x_koordinat - punkt2.x_koordinat
    ydiff = punkt1.y_koordinat - punkt2.y_koordinat
    return (xdiff**2 + ydiff**2)**0.5

if __name__ == "__main__":
    punkt1 = Punkt(3, 4)
    print(punkt1)
    print(punkt1.avstand_origo())
    punkt2 = Punkt()
    print(punkt2)
    print(punkt2.avstand_origo())
    punkt1.flytt(2, -1)
    print(punkt1)
    print(punkt1.avstand_origo())
    punkt3 = Punkt(5, 10)
    avstanden = punkt1.avstand(punkt3)
    print(f"Avstanden mellom {punkt1} og {punkt3} er {avstanden}")    
    print(avstand_punkter(punkt1, punkt3))