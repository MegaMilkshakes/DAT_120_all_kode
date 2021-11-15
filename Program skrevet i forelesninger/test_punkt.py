# -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 16:30:20 2021

@author: gerry
"""



import unittest
from punkt_klasse import Punkt


class TestPunkt(unittest.TestCase):
    def test_konstruktoer(self):
        p1 = Punkt(7, 8)
        p2 = Punkt()
        self.assertEqual(p1.x_koordinat, 7)
        self.assertEqual(p1.y_koordinat, 8)
        self.assertEqual(p2.x_koordinat, 0)
        self.assertEqual(p2.y_koordinat, 0)
    
    def test_flytt(self):
        p1 = Punkt(7, 8)
        self.assertEqual(p1.x_koordinat, 7)
        self.assertEqual(p1.y_koordinat, 8)
        p1.flytt(2, 5)
        self.assertEqual(p1.x_koordinat, 9)
        self.assertEqual(p1.y_koordinat, 13)
        p1.flytt(-8, -3)
        self.assertEqual(p1.x_koordinat, 1)
        self.assertEqual(p1.y_koordinat, 10)
        
    def test_avstand_origo(self):
        p1 = Punkt(3, 4)
        self.assertAlmostEqual(p1.avstand_origo(), 5.0, places=5)
        #bruk AlmostEqual siden flyttall ofte får desimaltallfeil
        p2 = Punkt(9, 6)
        self.assertAlmostEqual(p2.avstand_origo(), 10.8167, places=4)
        
    def test_x_koordinat(self): #testesr om ValueError blir raised
        p1 = Punkt(2, 5)
        with self.assertRaises(ValueError):
            p1.x_koordinat = -6
        
        
if __name__ == "__main__":
    unittest.main()
    

#kan bruke self.fail() for å faile koden om den kommer så langt i kodelinjen