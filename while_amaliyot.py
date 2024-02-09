# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 21:17:12 2024

@author: User
"""

#Foydalanuvchidan yaxshi ko'rgan kitoblarini kiritishni so'rang.
# Foydalanuvchi stop so'zini yozishi bilan dasturni to'xtating
'''
savol = "Yaxshi ko'rgan kitoblaringiz qaysi?"
savol += "(Dasturni to'xtatish uchun stop so'zini kiting')"
while True:
    qiymat = input(savol)   
    if qiymat == 'stop':
        break
'''

#####################################################################
#Muzeyga chipta narhi foydalanuvchining yoshiga bog'liq: 7 dan yoshlarga - 2000 so'm, 7-18 gacha 3000 so'm,
# 18-65 gacha 10000 so'm, 65 dan kattalarga bepul. Shunday while tsikl yozingki, dastur foydalanuvchi 
#yoshini so'rasin va chipta narhini chiqarsin. Foydalanuvchi exit yoki quit deb yozganda dastur to'xtasin 
#(ikkita shartni ham tekshiring).
#Yuqoridagi dasturni turli usullarda yozib ko'ring (break, ishora, yoki shart tekshirish)
'''
savol = "Yoshingiz nechida"
while True:
    qiymat = input(savol)
    if qiymat == 'exit' or qiymat == 'quit':
        break
    yosh = int(qiymat)
    if yosh<7:
        narh = 2000
    elif 7<=yosh<18:
        narh = 3000
    elif 18<=yosh<65:
        narh = 10000
    else: narh = 0
    
    if narh==0:
        print("Sizga chipta bepul")
    else:
        print(f"Chipta {narh} so'm")
'''
       


