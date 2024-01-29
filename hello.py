# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 19:52:51 2023

@author: User
"""
#message = 'hello world!'
#print(message)

#radius = 5
#pi = 3.14
#aylana_yuzi = pi * radius**2
#print("radiusi", radius,"ga teng aylana yuzi=", aylana_yuzi)

#kocha = "bogbon"
#mahalla = "sogbon"
#tuman ="bodomzor"
#viloyat  = "samarqand"

#generall = (kocha + ' ko\'chasi,' + ' ' + mahalla + ' mahallasi,' + ' ' + tuman + ' tumani,' + ' ' + viloyat + ' viloyati')
#bogbomprint(generall)

#kocha = input("kochani kiriting\n>>>>>")
#mahalla = input("mahallani kiriting\n>>>>")
#tuman = input("tumanni kiriting\n>>>")
#viloyat = input("viloyatni kiriting\n>>>")
#print(kocha + ' ko\'chasi,\n' + ' ' + mahalla + ' mahallasi,\n' + ' ' + tuman + ' tumani,\n' + ' ' + viloyat + ' viloyati\n')
#################################################

#son_k = int(input("Istalgan sonni kiriting:"))
#print(son_k, 'ning kvadrati', son_k**2,'ga teng')
#print(son_k, 'ning kubi', son_k**3, 'ga teng')

#################################################

#yosh = int(input("yoshingizni kiriting:\n>>>"))
#birthday_y = ("siz", 2023 - yosh, "da tug'ilgansiz")
#print(birthday_y)

################################################

#first_num = int(input("Birinchi sonni kiriting\n>>>"))
#second_num = int(input("Ikkinchi sonni kiriting\n>>>"))

#addition = first_num + second_num
#multiply = first_num * second_num
#bol = first_num/second_num
#ayirma = first_num - second_num

#print(addition)
#print(multiply)
#print(bol)
#print(ayirma)

###############################################
# ============RO"YXATLAR =====================
###############################################

#ismlar = ["Jahon", "Navruz", "Ruslon", "Murod"]
#print("Salom", ismlar[0], "bugun choyxona bormi?")
#print(ismlar[0], "sen kecha", ismlar[2], "ni ko'rdingmi")

###############################################

#sonlar = [21, 2, -4, 2.1, 12, 5.5]
#addition = sonlar[2] - sonlar[3]
#bol = sonlar[4] / sonlar[1]

#sonlar[2] = 12

#multiply = sonlar[2] * sonlar[0]
#print(addition)
#print(multiply)
#print(bol)
################################################

#t_shaxslar = ["Amir Temur", "Jaloliddin", "Chingizxon", "Makedonskiy"]
#z_shaxslar = ["Ilon Mask", "Bezos", "Sukkerberg", "MRX"]
#person = t_shaxslar.pop(0)
#personz = z_shaxslar.pop(2)

#print("Men tarixiy shaxslardan", person, "bilan", ", zamonaviy shaxslardan esa", personz, "bilan suhbat qilishni istayman")

################################################

#cars = ['bmw', 'mercedes-benz', 'volvo', 'gm', 'toyotto']
#cars.sort()
#cars.sort(reverse=True)
#print(len(cars))
#sonlar = list(range(21,31)) #berilgan oraliqdagi sonlarni chiqarish
#toq_sonlar = list(range(1,20,2))#sonlarni 2 qadam bo'yicha chiqarish

#narhlar = [1500, 2500, 1250, 800, 2800]
#qimmat = max(narhlar) # ro'yxat elementlari eng kattasini aniqlash
#arzon = min(narhlar) #ro'yxat elementlari eng kichigini aniqlash
#jami = sum(narhlar) # ro'yxat elementlari yig'indisi

#print("Eng arzoni ", arzon , " Eng qimmati ", qimmat, " jami ", jami)
#my_cars = cars[:] #ro'yxatdan nusxa olish

################################################
                 # AMALIYOT
################################################

#world = ['America', 'Europa',  'asia', 'China', 'Australia', 'africa']
#world.sort(reverse = True)

#sonlar = list(range(120,1201,2))
#ayirma = max(sonlar) - min(sonlar)
#boshi = sonlar[0:21]
#urtasi = sonlar[270:291]
#oxiri = sonlar[520:541]
#print('ruyxat boshidagi elemetlar: ', boshi, ' ruyxat urtasidagi elementlar ', urtasi, ' ruyxat oxiridagi elementlar: ', oxiri)

taomlar = ['osh', 'manti', 'somsa', 'shashlik', 'shurva']
nonushta = taomlar[:]
nonushta.remove('osh')
nonushta.append('salatlar')
nonushta.append('qazi')
nonushta=tuple(nonushta)
nonushta.append('mastava')
print(nonushta)
