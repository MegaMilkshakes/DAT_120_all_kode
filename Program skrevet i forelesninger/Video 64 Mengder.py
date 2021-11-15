# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 20:19:18 2021

@author: gerry
"""

mengde1 = set()
mengde1.add("Gerry")
mengde1.add("elske")
mengde1.add("Anine")
mengde1.add("ikke")
mengde1.add("Anine") #legger ikke til Anine 2 ganger, ingen duplikater!

print("gerry" in mengde1)
print("Gerry" in mengde1)
print("\n")

for element in mengde1:
    print(element)
    #ting blir ikke printet i samme rekkefølge som du skriver dem inn

print("\n")

mengde1.remove("ikke")
for element in mengde1:
    print(element)
    
print("\n Mengde2: ")
mengde2 = set()
mengde2.add("Gerry")
mengde2.add("elsker")
mengde2.add("Snickers")
mengde2.add("og")
mengde2.add("Bacon")
for element in mengde2:
    print(element)

#Mengden av alle som er med i minst en av de to mengdene
#altså slår sammen begge listene og fjerner duplikater
m3 = mengde1.union(mengde2)
print("\n Union: ")
for element in m3:
    print(element)
    
# intersection er omvendt av union. den finner kun det som er med i BEGGE
m3 = mengde1.intersection(mengde2)
print("\n Intersection: ")
for element in m3:
    print(element)
    
    
#ønsker det som er med i mengde1, men ikke er med i mengde 2
m3 = mengde1.difference(mengde2)
print("\n m1 minus m2: ")
for element in m3:
    print(element)

print("\n")

#test
print(m3 <= mengde1) #delmengde. true fordi m3 inneholder det samme eller
                    #mindre av det samme av mengde1
print(m3 <= mengde2) #false fordi m3 ikke er laget ut ifra mengde2, så 
                    #innholdet er ikke likt eller mindre
