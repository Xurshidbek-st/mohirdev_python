# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 20:33:29 2024

@author: User
"""

#Foydanaluvchidan ismi, familiyasi, tug'ilgan yili, tug'ilgan joyi, email manzili va telefon raqamini qabul qilib,
# lug'at ko'rinishida qaytaruvchi funksiya yozing. Lug'atda foydalanuvchu yoshi ham bo'lsin. 
#Ba'zi argumentlarni kiritishni ixtiyoriy qiling (masalan, tel.raqam, el.manzil)
'''
def user_all_intr(ismi, familyasi, t_yili, t_joyi, email_adres='', tel_num = ''):
    if email_adres and tel_num:
        toliq_malumot = (f"{ismi} {familyasi} {t_yili} {t_joyi} {email_adres} {tel_num}")
    else:
        toliq_malumot = (f"{ismi} {familyasi} {t_yili} {t_joyi}" )
    return toliq_malumot.title()

malumot = user_all_intr("olim", "akramov", 1998, "samarqand" )
malumot1 = user_all_intr("SAmar", "SAlimov", 2000, "toshkent", "smar@GMAIL.COM", 9938405496)
print(f"foydalanuvhciularhaqida tuliq malumot {malumot} va {malumot1}" )
'''
#Yuqoridagi funksiyani while yordamida bir necha bor chaqiring, va mijozlar degan ro'yxatni shakllantiring.
# Ro'yxatdagi mijozlar haqidagi ma'lumotni konsolga chiqaring

def user_all_intr(ismi, familyasi, t_yili, t_joyi, email_adres='', tel_num = ''):


