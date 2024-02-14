# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 20:05:41 2024

@author: User
"""

def toliq_ism_yasa(ism, familya, otasining_ismi = ''):
    '''toliq ism qaytaruvchi funksiya'''
    if otasining_ismi:
        toliq_ism = (f"{ism} {familya} {otasining_ismi}")
    else:
        toliq_ism = (f"{ism} {familya}")
    return toliq_ism.title()

talaba1 = toliq_ism_yasa("olim", "hakimov")
talaba2 = toliq_ism_yasa("olim", "hakimov", "abrorovich")
print(f"darsga kelmagan talabalar: {talaba1} va {talaba2}")