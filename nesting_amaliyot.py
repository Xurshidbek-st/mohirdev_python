# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 20:31:34 2024

@author: User
"""

#Adabiyot (ilm-fan, san'at, internet) olamidagi 4 ta mashxur shaxlar haqidagi ma'lumotlarni lug'at ko'rinishida saqlang. 
#Lug'atlarni bitta ro'yxatga joylang, va har bir shaxs haqidagi ma'lumotni konsolga chiqaring.

navoiy = {
    't_yili' : 1441,
    't_joyi' : 'hirot',
    'yunalishi':'shoir',
    'asarlari_soni':100,
    'yoshi': 65
    }
bobur = {
    't_yili' : 1510,
    't_joyi' : 'samarqand',
    'yunalishi':'shoh',
    'asarlari_soni':15,
    'yoshi': 54
    }
zamaxshariy = {
    't_yili' : 1300,
    't_joyi' : 'fors',
    'yunalishi':'yozuvchi',
    'asarlari_soni':45,
    'yoshi': 72
    }
zanajviy = {
    't_yili' : 1215,
    't_joyi' : 'fors',
    'yunalishi':'shoir',
    'asarlari_soni':76,
    'yoshi': 80
    }

adabiyot = [navoiy, bobur, zamaxshariy, zanajviy]
for item in adabiyot:
    print(f"{item['t_yili']}"
          f"{item['t_joyi].title()} shahri,"
          f"{item['yunalishi']}"
          f"{item['asarlari_soni']}")