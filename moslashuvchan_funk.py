# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 12:27:57 2024

@author: User
"""
'''
def summa(*sonlar):
    yigindi = 0
    for son in sonlar:
        yigindi += son
    return yigindi

print(summa(1,2))
print(summa(1,2,3,4,5))
'''

def avto_info(kompaniya,model,**malumotlar):
    """Avto haqidagi ma'lumotlarni lug'at ko'rinishdia qaytaruvchi funksiya"""
    malumotlar['kompaniya']=kompaniya
    malumotlar['model']=model
    return malumotlar

avto1 = avto_info("GM", "malibu", rang='qora', yil=2018)
avto2 = avto_info("Kia", "K5", rang='qizil', narh=35000)