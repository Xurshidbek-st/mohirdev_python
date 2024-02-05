# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 21:25:55 2024

@author: User
"""
#Python izohli lug'atini yarating va lug'atga kamida 10 ta so'z qo'shing. Lug'atdagi har bir kalit va qiymatni 
#for tsikli yordamida, alifbo ketma-ketligida chiroyli qilib konsolga chiqaring

#lugat_0 = {
    #'int': 'butun',
    #'float': 'o\'nlik',
    #'tuple': 'o\'zgarmas',
    #'if': 'agar',
    #'else': 'aks holda',
    #'for': 'takrorlash',
    #'not': 'inkor',
    #'lower': 'bosh',
    #'sort': 'saralash',
    #'value': 'qiymat'
    #}

#for kalit, qiymat in sorted(lugat_0.items()):
   # print(f"Kalit : {kalit}")
   # print(f"Qiymat: {qiymat} \n")
   
   ##############################################################################################################
  # Davlatlar va ularning poytaxtlari lug'atini tuzing. Avval lug'atdagi davlatlarni, keyin poytaxtlarni alohida-alohida, 
  #alifbo ketma-ketligida konsolga chiqaring.
  ##############################################################################################################
  
#world_0 = {
      #'America': 'vashingtong',
      #'russia': 'moskva',
      #'Uk': 'angliya',
      #'uzbekistan': 'toshkent',
      #'kazakstan': 'astana',
      #'tajikistan': 'dushanbe',
      #'ozarbayjon': 'baku',
      #'xitoy': 'pekin'
     # }
#for davlatlar in sorted(world_0.keys()):
     # print(davlatlar)
#for poytaxtlar in sorted(world_0.values()):
     # print(poytaxtlar)
     
     ##########################################################################################################
    # Foydalanuvchidan istalgan davlatni kiritishni so'rang va shu davlatning poytaxtini konsolga chiqaring. 
    #Agar foydalanuvchi lug'atda yo'q davlatni kiritsa, "Bizda bunday ma'lumot yo'q" degan xabarni chiqaring.
    ###########################################################################################################
 
#davlat = input("Davlatingizni kiriting: \n")
#world_0 = {
         #'America': 'vashingtong',
        # 'russia': 'moskva',
         #'Uk': 'angliya',
        # 'uzbekistan': 'toshkent',
         #'kazakstan': 'astana',
         #'tajikistan': 'dushanbe',
         #'ozarbayjon': 'baku',
         #  }

#capital = world_0.get(davlat)
#if capital == None:
    #print("kechirasiz bizda bunday malumot yoq")
#else:
   # print(f"{davlat.upper()} ning poytaxi {capital}")
   
   ###########################################################################################################
   #Restoran menusi lug'atini tuzing (kamida 10 ta taom-narh juftligini kiriting). Foydalanuvchidan 3 ta ovqat buyurtma 
   #berishni so'rang. Foydalanuvchi kiritgan taomlarni menu bilan solishtiring, agar taom menuda bo'lsa narhini ko'rsating, 
   #aks holda "bizda bunday taom yo'q" degan xabarni chiqaring.
   ##########################################################################################################
   
taomlar = {
    'somsa': 5000,
    'manti': 10000,
    'shashlik': 15000,
    'shurva': 10000,
    'osh': 20000,
    'dimlama': 25000,
    'salat': 5000,
    'choy': 2000,
    'non': 2000,
    'tandir': 30000
    }

print("3 ta taom buyurtma bering:")
buyurtmalar = []
for n in range(3):
    buyurtmalar.append(input(f"{n+1} - taaom :").lower())
    
for buyurtma in buyurtmalar:
    if buyurtma in taomlar:
        print(f"{buyurtma.title()} {taomlar[buyurtma]} sum")
    else:
        print("kechirasiz")