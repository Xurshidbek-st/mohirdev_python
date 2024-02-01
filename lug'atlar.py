# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 19:17:45 2024

@author: User
"""

#Python izohli lu'gati tuzing: Lug'atga shu kunga qadar o'rgangan 10 ta so'z (atamani)
# kiriting (masalan integer, float, string, if, else va hokazo) va har birining qisqacha tarjimasini yozing.

#lugat_0 = {
    #'integer':'butun son',
    #'float':'o\'nlik son',
    #'string':'satr',
    #'if':'agar',
    #'else':'aks holda',
    #'list':'ro\'yxat',
    #'tuple':'o\'zgarmas'
    #}
#Foydalanuvchidan biror so'z kiritishni so'rang va so'zning tarjimasini yuqoridagi lug'atdan chiqarib bering. 
#Agar so'z lu'gatda mavjud bo'lmasa, "Bunda so'z mavjud emas" degan xabarni chiqaring

#kalit = input("Kalit so'zni kiriting:").lower()
#print(lugat_0.get(kalit,"bunday kalit mavjud emas"))   

###########################################################################

mahsulotlar ={
    'olma':10000,
    'anor':20000,
    'uzum':5000,
    'shaftoli':25000,
    'anjir':15000
    }

bozorlik = ['olam', 'anor', 'non', 'baliq', 'anjir'] #bizning ro'yxatimiz
#berilgan ro'yxatdagi elemtlarni mahsulotlar lugatida bor yoki yo'qligini tekshiramiz

for mahsulot in mahsulotlar: #mahsulotlar ichidagi har bir mahsulot uchun
    if mahsulot in bozorlik:# agar bozorlik ichida mahsulot bo'lsa
        print(f"{mahsulot.title()} {mahsulotlar[mahsulot]} so\'m")
        
for buyum in bozorlik:
    if buyum not in mahsulotlar:
        print(f"iltimos ,  dukoningizga {buyum} olib keling")
        
 ####################################################################
print("salom")