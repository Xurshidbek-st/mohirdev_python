# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 18:21:13 2024

@author: User
"""
'''
#modullar yordamida funksiyani boshqa fayldan chaqirib olish
import avto_info_mod as aim
avto1 = aim.avto_info("gm", "malibu", "qora", "AVTOMAT", 2020)
aim.info_print(avto1)
'''
####################################################################
'''
from avto_info_mod import avto_info as ainfo, info_print as iprint
avto1 = ainfo("gm", "malibu", "qora", "AVTOMAT", 2020)
iprint(avto1)
'''
####################################################################

#python modullariga misollar

import random as rnd 
#randint()
#son  = rnd.randint(0,100)#berilgan oraliqdagi biror sonni chiqarish
#print(son)

#choice() berilgan ro'yxat elementlari ichidan bittasini tasodifiy tanlab oladi
ismlar = ["hasan", "husan", "olim", "ali"]
ism = rnd.choice(ismlar)
print(ism)
print(rnd.choice(ism))#tanlanga ismdan istalgan bitta harfni tanlaydi

