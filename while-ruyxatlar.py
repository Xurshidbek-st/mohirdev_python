# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 19:53:10 2024

@author: User
"""
'''
print("Yaqin do'stlaringiz ro'yxatini tuzamiz")
ismlar = []
n=1
while True:
    savol = f"{n} - do'stingizni kiriting"
    ism = input(savol)
    ismlar.append(ism)
    takrorlash = input("Yana kiritasizmi? (ha/yo'q')")
    n+=1
    if takrorlash != "ha":
        break
print("do'stlaringiz ro'yxati:")
for ism in ismlar:
    print(ism.title())
'''
###############################################################
#WHILE - LUGAT.
'''
print("Do'stlaringiz yoshini saqlaymiz:")
dostlar = {}
ishora = True
while ishora:
    ism = input("do'stingizni ismini kiriting:")
    yosh = input(f"{ism} do'stingizni yoshini kiriting:")
    dostlar[ism] = int(yosh)
    
    javob = input("yana malumot qo'shasizmi? (ha/yoq)")
    if javob != "ha":
        ishora = False
    
for ism, yosh in dostlar.items():
    print(f"{ism.title()} {yosh} da")
'''
#################################################################
#ro'yxat ichida  malumtlarni o'chirish
'''
cars = ['nexia', 'lacetti', 'gentra', 'nexia', 'matiz', 'captiva', 'nexia']
while 'nexia' in cars:
    cars.remove('nexia')
print(cars)
'''
################################################################

talabalar = ['botir', 'olim', 'hasan']
baholangan_talabalar = {}
while talabalar:
    talaba = talabalar.pop()
    baho = input(f"{talaba.title()} ning nahosini kit=riting:")
    print(f"{talaba.title()} baholandi")
    baholangan_talabalar[talaba] = int(baho)
    for talaba, baho in baholangan_talabalar.items():
        print(baholangan_talabalar)