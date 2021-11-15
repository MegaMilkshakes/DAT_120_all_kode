# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 08:21:54 2021

@author: Gerry
"""

import turtle
turtle.setup(720,950,1180,0)


STORRELSE = 50

#helst lag dette i en forloop, ikke copy paste koden
#må du endre eksempel størrelse må du fikse for mange
#plasser, mens i en loop kun 1plass
turtle.forward(STORRELSE)
turtle.right(90)
turtle.forward(STORRELSE)
turtle.right(90)
turtle.forward(STORRELSE)
turtle.right(90)
turtle.forward(STORRELSE)
turtle.right(90)

#kjør dette programmet i cmd
#cd = change directory
#om du kjører i cmd tegner den figuren og vindue forsvinner
#for å fikse dette bruk:
# turtle.done()
#turtle.done() fynker ikke i spyder mer enn 1gang
#kan endre hvilket program som skal kjøre koden din
#gjøres i "run" "config per file"