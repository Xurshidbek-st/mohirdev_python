# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 20:05:41 2024

@author: User
"""
"""
def toliq_ism_yasa(ism, familya, otasining_ismi = ''):
    '''toliq ism qaytaruvchi funksiya'''
    if otasining_ismi:
        toliq_ism = (f"{ism} {familya} {otasining_ismi}")
    else:
        toliq_ism = (f"{ism} {familya}")
    return toliq_ism.title()

talaba1 = toliq_ism_yasa("olim", "hakimov")
talaba2 = toliq_ism_yasa("olim", "hakimov", "abrorovich")
print(f"darsga kelmagan talabalar: {talaba1} va {talaba2}")

"""

'''
def avto_info(kompaniya,model, rangi, karobka, yili, narhi = None):
    avto = {
        'kompaniya':kompaniya,
        'model':model,
        'rang':rangi,
        'karobka':karobka,
        'yil':yili,
        'narh':narhi
        }
    return avto

avto1 = avto_info("GM", "Malibu", "qora", "mexanik", 2018)
avto2 = avto_info("GM", "Gentra", "oq", "avtomat", 2020,15000)
avtolar = [avto1, avto2]

print("onlayn bozorda mavjud avtolar:")
for avto in avtolar:
    if avto['narh']:
        narh = avto['narh']
    else:
        narh = "Nomalum"
    print(f"{avto['rang']} {avto['model']}. Narhi: {narh}")
'''

'''
def oraliq(min, max, qadam = None):
    sonlar = []
    
    if qadam == True:
     while(min<max):
        sonlar.append(min)
        min += 2
    else:
        while(min<max):
           sonlar.append(min)
           min += 1
    return sonlar
print(oraliq(0,10,2))
print(oraliq(20,30))
'''

def avto_info(kompaniya,model, rangi, karobka, yili, narhi = None):
    avto = {
        'kompaniya':kompaniya,
        'model':model,
        'rang':rangi,
        'karobka':karobka,
        'yil':yili,
        'narh':narhi
        }
    return avto
print("Saytimizdagi avtolar ro'yxatini shakllantiramiz.")
avtolar=[] # salondagi avtolar uchun bo'sh ro'yxat
while True:
    print("\nQuyidagi ma'lumotlarni kiriting",end='')
    kompaniya=input("Ishlab chiqaruvchi: ")
    model=input("Modeli: ")
    rangi=input("Rangi: ")
    korobka=input("Korobka: ")
    yili=input("Ishlab chiqarilgan yili: ")
    narhi=input("Narhi: ")
    
    #Foydalanuvchi kiritdan ma'lumotlardan avto_info yordamida 
    #lug'at shakllantirib, har bir lug'atni ro'yxatga qo'shamiz:
    avtolar.append(avto_info(kompaniya, model, rangi, korobka, yili, narhi))
    
    # Yana avto qo'shish-qo'shmaslikni so'raymiz
    javob = input("Yana avto qo'shasizmi? (yes/no): ")
    if javob=='no':
        break