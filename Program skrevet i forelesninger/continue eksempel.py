# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 18:19:02 2021

@author: Gerry
"""



#tell etasjer i et hotell med 20 etasjer men hopp over 13 pga overtro

for i in range(1, 21):
    if i == 13:
        continue
    print(i)


#continue går tilbake til start av blokka uten å fullføre siste del under continue
