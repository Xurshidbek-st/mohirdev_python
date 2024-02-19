# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 18:55:34 2024

@author: User
"""

#import math
#nomsiz funksiyalar - lambda
'''
uzunlik = lambda pi, r : 2*pi*r
print(uzunlik(math.pi,10))

kvadrat = lambda x,y:x**y
print(kvadrat(3,2))
'''
'''
from math import sqrt

sonlar = list(range(11))
ildizlar = list(map(sqrt,sonlar)) #map - funksiyasi qiymat sifatida ham funksiya qabul qiluvchi funksiya(bunda sqrt - funksiya, sonlar esa ro'yxat)
print(ildizlar)

def daraja2(x):
    return x*x
print(list(map(daraja2,sonlar)))
'''

###################################################################################################
'''
import random as r

sonlar = r.sample(range(100),10) # 0-99 oralig'ida 10 ta tasodifiy sonlar

def juftmi(x):
    """x juft bo'lsa True, aks holda False qaytaruvchu funksiya"""
    return x%2==0

juft_sonlar = list(filter(juftmi,sonlar))
print(sonlar)
print(juft_sonlar)
'''
#############################################################################################.

'''
import random as r

sonlar = r.sample(range(100),10) # 0-99 oralig'ida 10 ta tasodifiy sonlar
juft_sonlar = list(filter(lambda son: son%2==0,sonlar))

print(sonlar)
print(juft_sonlar)
'''

############################################################################################


