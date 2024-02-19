# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 12:12:52 2024

@author: User
"""

def bahola(ismlar):
    baholar = {}
    while ismlar:
        ism = ismlar.pop()
        baho = input(f" Talaba {ism.title()} ning bahosini kiriting:")
        baholar[ism] = int(baho)
    return baholar

talabalar = ["ali", "vali", "hasan", "husan"]
baholar = bahola(talabalar)
print(baholar)
        