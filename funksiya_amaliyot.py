# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 19:31:19 2024

@author: User
"""

#Foydalanuvchidan son qabul qilib, sonni 2 dan 10 gacha bo'lgan sonlarga qoldiqsiz bo'linishini 
#tekshiruvchi funksiya yozing. Natijalarni konsolga chiqaring.
'''
def qoldiqsiz_bulish(son):
    for n in range(2,11):
        if not son%n:
            print(f"{son} {n} ga qoldiqsiz bo'linadi")
qoldiqsiz_bulish(20)
'''
##############################################################################################
#Foydalanuvchidan ikkita son olib, ulardan kattasini konsolga chiqaruvchi funksiya yozing. 
#Agar sonlar teng bo'lsa "Sonlar teng" degan xabarni chiqaring.
'''
def katta_son(son1,son2):
    if(son1>son2):
        print(son1)
    elif (son1 == son2):
        print("Sonlar teng")
    else:
        print(son2)
katta_son(24, 24)
'''
#############################################################################################
