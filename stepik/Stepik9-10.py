# 1
# b = input()
# for i in range(0, len(b), 2):
#     print(b[i])
#
# 2
# b = input()
# for i in range(-1, -len(b) - 1, -1):
#     print(b[i])
#
# 3
# i = input()
# f = input()
# o = input()
# print(f[0], i[0], o[0], sep='')
#
# 4
# n = input()
# s = 0
# for i in range(len(n)):
#     s += int(n[i])
# print(s)
#
# 5
# n = input()
# s = 0
# for char in n:
#     if char in '1234567890':
#         s += 1
#         print('Цифра')
#         break
# else:
#     print('Цифр нет')
#
# 6
# n = input()
# pl = 0
# zv = 0
# for i in n:
#     if i == '+':
#         pl += 1
#     if i == '*':
#         zv += 1
# print(f'Символ + встречается {pl} раз')
# print(f'Символ * встречается {zv} раз')
#
# 7
# n = input()
# s = 0
# for i in range(len(n) - 1):
#     if n[i] == n[i + 1]:
#         s += 1
# print(s)
#
# 8
# n = input()
# s = 0
# g = 0
# for char in n:
#     if char in 'ауоыиэяюёеАУОЫИЭЯЮЁЕ':
#         g += 1
#     if char in 'бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ':
#         s += 1
# print(f'Количество гласных букв равно {g}')
# print(f'Количество согласных букв равно {s}')
#
# 9
# n = int(input())
# s = ''
# while n != 0:
#     ost = n % 2
#     s += str(ost)
#     n = n // 2
# print(s[::-1])
#
# 10
# n = input()
# npal = n[::-1]
# if n == npal:
#     print("YES")
# else:
#     print("NO")
#
# 11
# stroka = input()
# kolvosim = len(stroka)
# _3raza = stroka * 3
# pervsim = stroka[0]
# _3sim = stroka[0:3]
# _posl3sim = stroka[-3:]
# obratstr = stroka[::-1]
# perviposl = stroka[1:-1]
# print(kolvosim)
# print(_3raza)
# print(pervsim)
# print(_3sim)
# print(_posl3sim)
# print(obratstr)
# print(perviposl)
#
# 12
# s = input()
# print(s[2])
# print(s[-2])
# print(s[0:5])
# print(s[:-2])
# print(s[::2])  # chet
# print(s[1::2])  # nechet
# print(s[::-1])  # obrpor
# print(s[-1:0:-2])
#
# 13
# from math import *
#
# n = input()
# pervch = n[0:ceil(len(n) / 2)]
# vtorch = n[::-1]
# resvt = vtorch[0:len(vtorch) // 2]
# resresvt = resvt[::-1]
# print(resresvt, pervch, sep='')
#
# 14
# famil, name = map(str, input().split())
# if famil == famil.capitalize() and name == name.capitalize():
#     print("YES")
# else:
#     print("NO")
#
# 15
# print(input().swapcase())
#
# 16
# n = input()
# n = n.lower()
# if 'хорош' in n:
#     print('YES')
# else:
#     print('NO')
#
# 17
# n = input()
# n = n.swapcase()
# count = 0
# for i in n:
#     if i.upper() == i and i not in '1234567890':
#         count += 1
# print(count)
#
# 18
# print(input().count(' ') + 1)
#
# 19
# n = input().lower()
# print('Аденин:', n.count("а"))
# print('Гуанин:', n.count("г"))
# print('Цитозин:', n.count("ц"))
# print('Тимин:', n.count("т"))
#
# 20
# n = int(input())
# count = 0
# for i in range(n):
#     soob = input()
#     if soob.count('11') >= 3:
#         count += 1
# print(count)
#
# 21
# n = input()
# count = 0
# for i in n:
#     if i in '1234567890':
#         count += 1
# print(count)
#
# 22
# n = input()
# if n.endswith('.com') or n.endswith('.ru'):
#     print('YES')
# else:
#     print('NO')
#
# 23
# n = input()
# maxim = 0
# bukva = ''
# for i in n:
#     if n.count(i) >= maxim:
#         bukva = i
#         maxim = n.count(i)
# print(bukva)
#
# 24
# n = input()
# if n.count('f') == 1:
#     print(n.find('f'))
#     exit()
# if n.count('f') >= 2:
#     print(n.find('f'), n.rfind('f'))
#     exit()
# if n.count('f') == 0:
#     print('NO')
#
# 25
# n = input()
# print(n[:n.find('h')] + n[n.rfind('h') + 1:])
#
# 26
# data = input()
# euro = input()
# yuan = input()
# print(f'На {data}: 1€ = {euro}₽, 1¥ = {yuan}₽')
#
# 27
# a = int(input())
# b = int(input())
# print(f'Для чисел {a} и {b}:\n  Сумма кубов: {a}**3 + {b}**3 = {a ** 3 + b ** 3}\n ',
#       f'Куб суммы: ({a} + {b})**3 = {(a + b) ** 3}')
#
# 28
# den = int(input())
# ves = float(input())
# if ves <= 100 - den * 0.2:
#     print('Все идет по плану')
# else:
#     print('Что-то пошло не так')
# print(f'#{den} ДЕНЬ: ТЕКУЩИЙ ВЕС = {ves} кг, ЦЕЛЬ по ВЕСУ = {100 - den * 0.2} кг')
#
# 29
# a = input()
# if a == 'Я':
#     print('Дальше букв нет')
# else:
#     if chr(ord(a)) in "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ":
#         print((chr(ord(a) + 1)))
#
# 30
# a = int(input())
# b = int(input())
# for i in range(a, b + 1):
#     print(chr(i), end=' ')
#
# 31
# a = input()
# for i in a:
#     print(ord(i), end=' ')
#
# 32
# a = input()
# b = input()
# c = input()
# d = input()
# maxim = ''
# sua = 0
# sub = 0
# suc = 0
# sud = 0
# for i in a:
#     sua += ord(i)
# for i in b:
#     sub += ord(i)
# for i in c:
#     suc += ord(i)
# for i in d:
#     sud += ord(i)
# if sua >= sub and sua >= sud and sua >= suc:
#     maxim = a
# elif sub >= sua and sub >= sud and sub >= suc:
#     maxim = b
# elif sud >= sua and sud >= sub and sud >= suc:
#     maxim = d
# elif suc >= sua and suc >= sub and suc >= sud:
#     maxim = c
# print(maxim)
#
# 33
# s = input()
# summa = 0
# for i in s:
#     summa += ord(i)
# print(f"Текст сообщения: '{s}'")
# print(f"Стоимость сообщения: {summa * 3}🐝")
#
# 34
# s = input()
# summa = 0
# for i in s:
#     summa += ord(i)
# print(f"Старая стоимость: {summa * 3}🐝")
# eng = "eyopaxcETOPAHXCBM"
# rus = "еуорахсЕТОРАНХСВМ"
# for i in s:
#     if i in eng:
#         for j in range(len(rus)):
#             s = s.replace(eng[j], rus[j])
# summa = 0
# for i in s:
#     summa += ord(i)
# print(f"Новая стоимость: {summa * 3}🐝")
#
# 35
# sdvig = int(input())
# p = ''
# s = input()
# for i in s:
#     pos = ord(i) - ord('a')
#     pos -= sdvig
#     if pos < 0:
#         pos += 26
#     p += chr(pos + ord('a'))
# print(p)
#
# 36
# s = input()
# s = s.replace('u-', '')
# s = s.replace('[', '')
# s = s.replace(']', '')
# c = 0
# l = ''
# res = ''
# p = ''
# for i in s:
#     if i.isdigit():
#         c += 1
#         p += i
#         if c == 4:
#             c = 0
#             l = int(p)
#             res += chr(l)
#             p = ''
#     else:
#         if p:
#             res += p
#             p = ''
#             c = 0
#         res += i
# if p:
#     res += p
# print(res)
#
# 37
# s = ''
# for i in range(1, int(input()) + 1):
#     n = input()
#     if n.isspace() or n == '':
#         s += str(i) + ': ' + 'COMMENT SHOULD BE DELETED' + '\n'
#     else:
#         s += str(i) + ': ' + n + '\n'
# print(s)
#
# 38
# nickname = input()
# if nickname[0] == '@':
#     if 5 <= len(nickname) <= 15:
#         if nickname[1:].isdigit():
#             print('Correct')
#             exit()
#         if nickname[1:].isalpha():
#             if nickname[1:].islower():
#                 print('Correct')
#                 exit()
#         nickname = nickname[1:]
#         if nickname.isalnum():
#             if nickname.islower():
#                 print('Correct')
#             else:
#                 print('Incorrect')
#         else:
#             print('Incorrect')
#     else:
#         print('Incorrect')
# else:
#     print('Incorrect')
#
# 39
# b='АВЕКМНОРСТУХ'
# an = input()
# if len(an)==9:
#     if(
#     an[0] in b
#     and an[1:4].isdigit()
#     and an[4] in b and an[5] in b
#     and an[6]=='_'
#     and an[7:].isdigit()
#     ):
#         print('YES')
#     else:
#         print('NO')
#
# elif len(an)==10:
#     if (
#             an[0] in b
#             and an[1:4].isdigit()
#             and an[4] in b and an[5] in b
#             and an[6] == '_'
#             and an[7:].isdigit()
#     ):
#         print('YES')
#     else:
#         print('NO')
# else:
#     print('NO')


#kr1
# n=input()
# s=''
# for i in range(len(n)):
#     if i%3!=0:
#         s+=n[i]
# print(s)


#kr2
# print(input().replace('1','one'))


#kr3
# print(input().replace('@',''))


#kr4
# n=input()
# p=0
# for i in n:
#     if i=='f':
#         p+=1
# if p>1:
#     n=n.replace('f','-',1)
#     print(n.find('f'))
# if p==1:
#     print('-1')
#     exit()
# if p==0:
#     print('-2')
#     exit()


#kr5
# n=input()
# perv=n.find('h')
# posl=n.rfind('h')
# srez=n[perv:posl+1]
# print(n[0:perv]+srez[::-1]+n[posl+1:])











