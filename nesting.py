# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 19:31:07 2024

@author: User
"""
# RO'YXAT ICHIDA LUG'AT
'''
car_0 = {
        'model' : 'nexia_2',
        'rang' : 'oq',
        'yili' : 2013,
        'ot_kuchi'  : 122,
        'korobka' : 'mexanika',
        'narhi' : 6000
        }
car_1 = {
        'model' : 'lacetti',
        'rang' : 'qora',
        'yili' : 2016,
        'ot_kuchi' : 140,
        'korobka' : 'avtomat',
        'narhi' : 8000
        }
car_2 = {
        'model' : 'gentra',
        'rang' : 'qizil',
        'yili' : 2016,
        'ot_kuchi' : 150,
        'korobka' : 'avtomat',
        'narhi' : 15000
        }
cars = [car_0, car_1, car_2]
for car in cars:
    print(f"{car['model'].title()}, "
        f"{car['rang']} rang, "
        f"{car['yili']}-yil, {car['narhi']}$")
    '''
    ####################################################################
'''
malibus = []
for n in range(10):
    new_car = {
        'model':'malibu',
        'narhi':None,
        'yili':2013,
        'karobka':'avto',
        'masofasi':50000,\
        'rang': None
        }    
    malibus.append(new_car)
for malibu in malibus[:3]:
    malibu['rang']='qizil' #malibus ro'yxaaatining birinchi uchta elementini rangini qizil qilish
#for malibu in malibus:
    #print(malibu)
    
for malibu in malibus[3:6]:
    malibu['rang'] = 'qora' #malibus ro'yxatining 3-dan 6-gacha elementlari rangini qora qilish
    
for malibu in malibus[6:]:
    malibu['rang'] = 'oq'
    malibu['karobka']  = 'mexanika'##malibus ro'yxatining 6-dan keyingi elementlari rangini oq qilish

#for malibu in malibus:
   # print(malibu)
    
for malibu in malibus:
    if malibu['karobka'] == 'avto':
        malibu['narhi']  = 40000
    else:
        malibu['narhi'] = 35000
for malibu in malibus:
    print(malibu)
'''

# LU'GAT ICHIDA RO'YXAT
'''
dasturchilar = {
    'ali':['python', 'c++'],
    'vali':['html', 'css', 'js'],
    'hasan':['php', 'sql'],
    'husan':['python', 'mysql'],
    'maryam':['c++', 'java']
    }

for ism, tillar in dasturchilar.items():
    print(f"\n{ism.title()} quyidagi dasturlash tillaridan foydalanadi")
    for til in tillar:
        print(til.upper(), end = ' ') #dasturchilarni qaysi dasturlash tillaridan foydalanishlarini chiqarish
# end=' '  - qiymatlarni printda bir qatorda chiqarish
'''

##############################################################################################################
#LUG'ATLARNI ICHIGA BOSHQA LUG'ATLARNI JOYLASH

hamkasblar = {
    'ali':{
        'familya':'valiyev',
        'yosh':'25',
        'malumoti':'oliy',
        'tillar':['python', 'c++']
        },
    'vali':{
        'familya':'salimov',
        'yosh':'30',
        'malumoti':'oliy',
        'tillar':['java', 'c++']
        },
    'husan':{
        'familya':'boltayev',
        'yosh':'18',
        'malumoti':'orta',
        'tillar':['html', 'css', 'js']
        },
    'hasan':{
        'familya':'boltayev',
        'yosh':'18',
        'malumoti':'orta',
        'tillar':['html', 'css', 'go']
        }
    }

for ism, info in hamkasblar.items():
   print(f"\n{ism.title()} {info['familya'].title()}, "
          f"Ma'lumoti: {info['malumoti']}. \n"
          "Quyidagi dasturlash tillarini biladi:")
   for til in info['tillar']:
        print(til.upper(), end = ' ')