# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 20:29:32 2024

@author: User
"""
'''
son = 1
while son<=5:
    print(son, end= ' ')
    son += 1
'''
############################################################################
'''
print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
savol = "Istalgan son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
qiymat = ''
while qiymat != 'exit':
    qiymat = input(savol)
    if qiymat != 'exit':
        print(float(qiymat)**2)
'''
###########################################################################
#ISHORA- FLAG
'''
print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
savol = "Istalgan son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
ishora = True
while ishora: #ishora to'gri bo'lganda shart bajariladi
    qiymat = input(savol)
    if qiymat == 'exit':
        ishora = False
    else:
        print(float(qiymat)**25)
'''

#############################################################################
#DASTURNI TO'XTATISH BREAK WHILE
'''
print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
savol = "Istalgan son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
while True: #abadiy tsikl
    qiymat = input(savol)
    if qiymat == 'exit':
        break # tsikl shart bajarilganda to'xtaydi
    else:
        print(float(qiymat)**2)
'''

#############################################################################
#FOR BREAK
'''
sonlar = list(range(1,11))
for son in sonlar:
    if son == 5:
        break
    print(son**2)     
'''
#CONTINUE
'''
sonlar = list(range(1,11))
for son in sonlar:
    if son == 5:
        continue #bunda dastur bir qadam tashlab o'tadi yani son=5 da bajarilmaydi
    print(son**2) 
'''

#CONTINUE WHILE

son = 0
while son < 10:
    son += 1
    if son % 2 != 0:
        continue #agar sonni qoldiqi bo'lsa tsikl boshiga qaytadi
    else:
        print(son)