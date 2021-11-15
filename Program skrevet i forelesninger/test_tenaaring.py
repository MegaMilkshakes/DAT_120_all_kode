# -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 15:19:20 2021

@author: gerry
"""



import unittest
from tenaaring import er_tenaaring


class TestTenaaring(unittest.TestCase):
    def test_er_tenaaring(self):
        self.assertFalse(er_tenaaring(5))
        self.assertFalse(er_tenaaring(12))
        self.assertTrue(er_tenaaring(13))
        self.assertTrue(er_tenaaring(17))
        self.assertFalse(er_tenaaring(18))
        self.assertFalse(er_tenaaring(35))

if __name__ == "__main__":
    unittest.main()
