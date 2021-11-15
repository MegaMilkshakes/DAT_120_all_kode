# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 20:47:36 2021

@author: gerry
"""


from punkt_klasse import Punkt


class RettLinje:
    def __init__(self, startpunkt: Punkt, sluttpunkt: Punkt):
        self.startpunkt = startpunkt
        self.sluttpunkt = sluttpunkt
        
    def __str__(self):
        return f"linje fra {self.startpunkt} til {self.sluttpunkt}"
    
    def lengde(self):
        return self.startpunkt.avstand(self.sluttpunkt)
    
if __name__ == "__main__":
    p1 = Punkt(6, 2)
    p2 = Punkt(3, 6)
    l1 = RettLinje(p1, p2)
    print(l1)
    print(l1.lengde())
    p2.flytt(2, 2)
    print(l1)
    print(l1.lengde())


