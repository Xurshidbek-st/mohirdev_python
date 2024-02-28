# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 19:49:31 2024

@author: User
"""

import random
def sontop(x=10):
    tasodifiy_son = random.randint(1,x)
    print(f"Men 1 dan {x} gacha son o'yladim.Topa olasizmi?")
    taxminlar = 0
    
    while True:
        taxminlar += 1
        taxmin = int(input(">>>"))
        if taxmin < tasodifiy_son:
            print("Xato.men o'ylagan son bundan kattaroq.Yana harakat qiling:")
        elif taxmin > tasodifiy_son:
            print("Xato men o'ylagan son bundan kichikroq.Yana harakat qiling:")
        else:
            break
   
    print(f"Tabdiklaymiz {taxminlar} ta taxmin bilan topdingiz")
    return taxminlar
    
def sontop_pc(x=10):
    input(f"1 da {x} gacha biror son o'ylang va istalgan tugmani bosing.Men topaman")
    quyi = 1
    yuqori = x
    taxminlar = 0
    while True:
        taxminlar += 1
        if quyi != yuqori:
            taxmin = random.randint(quyi, yuqori)
        else:
            taxmin = yuqori
        javob = input(f"Siz {taxmin} sonni o'yladingiz: to'g'ri(t),"
                      f"men o'ylagan son kattaroq (+), yoki kichikroq(-)".lower())
        if javob == "-":
            yuqori = taxmin - 1
        elif javob == "+":
            quyi = taxmin + 1
        else:
            break 
    
    print("topfim") 
    return taxminlar        

def play(x = 10):
    yana = True
    while yana:
        taxminlar_user = sontop(x)
        taxminlar_pc = sontop(x)
        
        if taxminlar_user > taxminlar_pc:
            print("men yutdim")
        elif taxminlar_pc > taxminlar_user:
            print("siz yutdingiz")
        else:
.            print("durang")
        yana = int(input("yana o'ynaysizmi? Ha(1)/Yo'q(0): "))