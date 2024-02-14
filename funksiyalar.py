# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 21:38:46 2024

@author: User
"""
"""
def salom_ber(ism):
    ''' Foydalanuvchining ismini qaqbul qilib unga salom beruvchi matn'''
    print(f"Assalom alaykum hurmatli {ism.title()}")
    
salom_ber("Olim")
salom_ber("hasan")
"""
"""
def ism_familya(ism, familya):
    '''foydalanuvhcini barcha malumotlarini jamlab beruvchi fubksiya'''
    print(f"Foydalanuvhci=hi ismi :{ism.title()} \n"
          f"Foydalanuvchni familyasi :{familya.title()}")
ism_familya("olim", "hakimov")
"""

def yosh_hisobla(tugilgan_yil, joriy_yil = 2024):
    '''funksiyaga standart qiymat berish orqali foydalanuvchi yoshini hisoblovchi funksiya'''
    print(f"siz {joriy_yil - tugilgan_yil} yoshdasiz")
    
yosh_hisobla(1998)