# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 19:11:09 2024

@author: User
"""

#mahsulotlar = ['nokia', 'samsung', 'redmi', 'iphone', 'xiaomi', 'infinix', 'mobi', 'dell', 'asus','zzephus']
#savat = []
#print("5 ta sevimli mahsulotingizni kiriting")

#for n in range(5):
   # savat.append(input(f'savatga {n+1} ta - mahsulot qo\'shing:'))

#for mahsulot in savat:
    #if mahsulot in mahsulotlar:
        #print(f"do'konimizda {mahsulot} bor")
    #else:
       # print(f"do'konimzda mahsulot yoq")
    
#################################################################################

#mahsulotlar = ['nokia', 'samsung', 'redmi', 'iphone', 'xiaomi', 'infinix', 'mobi', 'dell', 'asus','zzephus']
#savat = []
#print("5 ta sevimli mahsulotingizni kiriting")

#for n in range(5):
   # savat.append(input(f'savatga {n+1} ta - mahsulot qo\'shing:'))
    
#bor_mahsulotlar = []
#mavjud_emas = []
#for mahsulot in savat:
    #if mahsulot in mahsulotlar:
        #bor_mahsulotlar.append(mahsulot)
    #else:
       # mavjud_emas.append(mahsulot)
        
#if mavjud_emas:
   # print(f"do'konimizda quyidagi mahsulotlar yo'q:")
    #for mahsulot in mavjud_emas:
       # print (mahsulot)
   # else:
       # print("siz so'ragan barcha mahsulorlar do'konimizda bor")
       
##################################################################################

#users = ['alisher','aziza','yasina','umar']

#login = input("Yangi login tanlang: ")

#if login.lower() in users:
   # print('Login band, yangi login tanlang!')
#else:
   # print(f"Xush kelibsiz, {login.title()}!")
   
#################################################################################
#Foydalanuvchidan biror butun son kiritishni so'rang. Foydalanuvchi kiritgan sonni 2 da 10 gacha 
#bo'lgan sonlardan qay biriga qoldiqsiz bo'linishini konsolga chiqaring.
#########################################################################################
    
son = int(input("Istalgan butun son kiriting: "))

for n in range(2,11):
    if not (son%n):
        print(f"{son} soni {n} ga qoldiqsiz bo'linadi")