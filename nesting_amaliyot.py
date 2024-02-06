# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 20:31:34 2024

@author: User
"""

#Adabiyot (ilm-fan, san'at, internet) olamidagi 4 ta mashxur shaxlar haqidagi ma'lumotlarni lug'at ko'rinishida saqlang. 
#Lug'atlarni bitta ro'yxatga joylang, va har bir shaxs haqidagi ma'lumotni konsolga chiqaring.
'''
navoiy = {
    'ism':'navoiy',
    'tyil' : 1441,
    'vyil' : 'hirot',
    'yunalishi':'shoir',
    'asarlari_soni':100,
    'yoshi': 65
    }
bobur = {
    'ism':'bobur',
    'tyil' : 1510,
    'vyil' : 'samarqand',
    'yunalishi':'shoh',
    'asarlari_soni':15,
    'yoshi': 54
    }
zamaxshariy = {
    'ism':'zamaxshariy',
    'tyil' : 1300,
    'vyil' : 'fors',
    'yunalishi':'yozuvchi',
    'asarlari_soni':45,
    'yoshi': 72
    }
zanajviy = {
    'ism':'zanjaviy',
    'tyil' : 1215,
    'vyil' : 'fors',
    'yunalishi':'shoir',
    'asarlari_soni':76,
    'yoshi': 80
    }

adabiyot = [navoiy, bobur, zamaxshariy, zanajviy]
for shaxs in adabiyot:
    ism = shaxs['ism']
    tyil = shaxs['tyil']
    vyil = shaxs['vyil']
    print(f"{ism} {tyil}-yilda "
          "yil umr ko'rgan.")
'''
########################################################################################
#Yuqoridagi lug'atlarga har bir shaxsning mashxur asarlari ro'yxatini ham qo'shing. 
#For tsikli yordamida muallifning ismi va uning asarlarini konsolga chiqaring.
'''
navoiy = {
    'ism':'navoiy',
    'tyil' : 1441,
    'vyil' : 1500,
    'asarlari_soni':100,
    'asarlari':['xamsa', 'dfr', 'dfsf']
    }
bobur = {
    'ism':'bobur',
    'tyil' : 1510,
    'vyil' : 1580,
    'asarlari_soni':15,
    'asarlari':['sdffe', 'gtgt', 'dfgtg']
    }
zamaxshariy = {
    'ism':'zamaxshariy',
    'tyil' : 1300,
    'vyil' : 1347,
    'asarlari_soni':45,
    'asarlari': ['fbvc', 'khl', 'iuiy', 'oiopi']
       }
zanajviy = {
    'ism':'zanjaviy',
    'tyil' : 1215,
    'vyil' : 1278,
    'asarlari_soni':76,
    'asarlari': ['nmcbv', 'ghut', 'oitu']
    }

adabiyot = [navoiy, bobur, zamaxshariy, zanajviy]
for shaxs in adabiyot:
    ism=shaxs['ism']
    asarlar = shaxs['asarlari']
    print(f"\n{ism} ning mashxur asarlari: ")
    for asar in asarlar:
       print(asar)
'''

#################################################################################
#Oila a'zolaringiz (do'stlaringiz) dan 3 ta sevimli kino-seriali haqida so'rang. 
#Do'stingiz ismi kalit, uning sevimli kinolarini esa ro'yxat ko'rinishida lug'artga saqlang. Natijani konsolga chiqaring.
'''
kinolar = {
    'ali':['Terminator','Rambo','Titanic'],
    'vali':['Tenet','Inception','Interstellar'],
    'hasan':['Abdullajon','Bomba','Shaytanat'],
    'husan':['Mahallada duv-duv gap','John Wick']
    }

for ism, kinolar in kinolar.items():
    print(f"\n{ism.title()}ning sevimli kinolari:")
    for kino in kinolar:
        print(kino)
'''

#################################################################################
#Davlatlar degan lug'at yarating, lug'at ichida bir nechta davlatlar haqida ma'lumotlarni lug'at ko'rinishida saqlang.
# Har bir davlat haqida ma'lumotni konsolga chiqaring.

davlatlar = {
    "o'zbekiston":{'poytaxt':"toshkent",
                   'maydon':448978,
                   'aholi':33_000_000,
                   'pul birligi':"so'm"
                   },
    "rossiya":{'poytaxt':"moskva",
                   'maydon':17_098_246,
                   'aholi':144_000_000,
                   'pul birligi':"rubl"
                   },
    "aqsh":{'poytaxt':"vashington",
                   'maydon':9_631_418,
                   'aholi':327_000_000,
                   'pul birligi':"dollar"},
    "malayziya":{'poytaxt':"kuala-lumpur",
                   'maydon':329750,
                   'aholi':25_000_000,
                   'pul birligi':"rinngit"}
    }

for davlat, info in davlatlar.items():
    if davlat.lower()=='aqsh':
        davlat = davlat.upper()
    else:
        davlat = davlat.capitalize()
    print(f"\n{davlat}ning poytaxti {info['poytaxt'].title()}"
          f"\nHududi: {info['maydon']} kv.km"
          f"\nAholisi: {info['aholi']}"
          f"\nPul birligi: {info['pul birligi']}")





