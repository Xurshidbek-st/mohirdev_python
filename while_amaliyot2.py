# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 21:22:27 2024

@author: User
"""

#Foydalanuvchidan buyurtma qabul qiluvchi dastur yozing. Mahsulotlar nomini birma-bir qabul qilib, yangi ro'yxatga joylang..
'''
print("Mahsulotlar ro'yxati")
savat = []
n=1
while True:
    savol = f"{n} - mahsulotni kiriting"
    xarid = input(savol)
    savat.append(xarid)
    takrorlash = input("Yana mahsulot xarid qilasizmi? (ha/yo'q')")
    n+=1
    if takrorlash != "ha":
        break
print("mahsulotlar ro'yxaati:")
for xarid in savat:
    print(xarid)
'''
##############################################################################
#e-bozor uchun mahsulotlar va ularning narhlari lug'atini shakllantiruvchi dastur yozing.
# Foydalanuvchidan lug'atga bir nechta elementlar (mahsulot va uning narhi) kiritishni so'rang.
'''
print("mahsulotlar haqida dastur:")
savat = {}
ishora  = True
while ishora:
    maxsulot = input("Maxsulot nomini kiriting:")
    narx = input(f"{maxsulot} narxini kiriting:")
    savat[maxsulot] = int(narx)
    
    javob = input("yana maxsulot qo'shasizmi? (ha/yo'q)")
    if javob != "ha":
        ishora = False
for maxsulot, narx in savat.items():
    print(f"{maxsulot} {narx} so'mdan")
'''
#############################################################################
#Yuqoridagi ikki dasturni jamlaymiz. Foydalanuvchi buyurtmasi ro'yxatidagi har bir mahsulotni e-bozordagi 
#mahsulotlar bilan solishitiring (tayyor ro'yxat ishlatishingiz mumkin). Agar mahsuot e-bozorda mavjud bo'lsa mahuslot
# narhini chiqaring, aks holda "Bizda bu mahsulot yo'q" degan xabarni kor'sating.
buyurtmalar = ['olma','anjir','uzum','qovun']
mahsulotlar = {'olma':20000,
               'shaftoli':25000,
               'tarvuz':18000,
               'uzum':22000}

while buyurtmalar:
    buyurtma = buyurtmalar.pop()
    if buyurtma in mahsulotlar.keys():
        narh = mahsulotlar[buyurtma]
        print(f"{buyurtma.title()} - {narh} so'm")
    else:
        print(f"Bizda {buyurtma} yo'q")
    