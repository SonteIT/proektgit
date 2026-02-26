# 1
# def draw_box():
#     print('*'*10)
#     for i in range(12):
#         print('*        *',end='')
#         print()
#     print('*'*10)
#
#
# draw_box()
import string


# 2
# def draw_triangle():
#     for i in range(1,11):
#         print('*'*i,sep='\n')
#
#
# draw_triangle()


# 3
# объявление функции
# def print_fio(name, surname, patronymic):
#     print(surname[0].upper(), name[0].upper(), patronymic[0].upper(),sep='')
#
#
# surname, name, patronymic = input(), input(), input()
#
#
# print_fio(surname, name, patronymic)


# 4
# объявление функции
# def print_case_counts(s):
#     U=0
#     L=0
#     for i in s:
#         if i.isupper():
#             U+=1
#         if i.islower():
#             L+=1
#     print(f'Букв в верхнем регистре: {U}')
#     print(f'Букв в нижнем регистре: {L}')
#
#
#
# s = input()
#
#
# print_case_counts(s)


# 5
# def print_digit_sum(num):
#     s=0
#     while num>0:
#         s=s+num%10
#         num=num//10
#     print(s)
#
#
# n = int(input())
#
#
# print_digit_sum(n)


# 6
# def print_sorted_hyphen(s):
#     s=s.split('-')
#     s.sort()
#     p='-'.join(s)
#     print(p)
#
#
#
# s = input()
#
#
# print_sorted_hyphen(s)


# 7
# def draw_triangle(fill, base):
#     for i in range(1, base // 2 + 2, 1):
#         print(fill * i)
#     for j in range(base // 2, 0, -1):
#         print(fill * j)
#
# fill = input()
# base = int(input())
#
#
# draw_triangle(fill, base)


# 8
# def print_perm_time_call(msc_time):
#     if msc_time[0]=='0':
#         if int(msc_time[1])+2>=10:
#             m=str(int(msc_time[1])+2)
#             msc_time=m+msc_time[2:]
#         elif int(msc_time[1])+2<10:
#             m=str(int(msc_time[1])+2)
#             msc_time='0'+m+msc_time[2:]
#         print(f'Созвон будет в {msc_time}.')
#     elif msc_time[0]!='0':
#         m = str(int(msc_time[0:2]) + 2)
#         msc_time = m + msc_time[2:]
#         print(f'Созвон будет в {msc_time}.')
#
#
# msc_time = input()
#
#
# print_perm_time_call(msc_time)


# 9
# объявление функции
# def print_symbol_counts(s):
#     s=s.lower()
#     s=list(s)
#     s.sort()
#     r=[]
#     for i in s:
#         if i not in r:
#             r.append(i)
#     for i in r:
#         print(i,': ',s.count(i),sep='')
#
#
# s = input()
#
#
# print_symbol_counts(s)


# 10
# def convert_to_miles(km):
#     return km * 0.6214
# km = int(input())
# print(convert_to_miles(km))


# 11
# def code_format(text):
#     return(f'<code>{text}</code>')
# text=input()
# print(code_format(text))


# 12
# def get_days(month):
#     if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
#         return 31
#     if month==2:
#         return 28
#     else:
#         return 30
# print(get_days(int(input())))


# 13
# def math_round_to_int(num):
#     if num%1>=0.5:
#         return int(num)+1
#     else:
#         return int(num)
# print(math_round_to_int(float(input())))


# 14
# def number_of_factors(num):
#     factors=0
#     for i in range(1,num+1):
#         if num%i==0:
#             factors+=1
#     return factors
# print(number_of_factors(int(input())))


# 15
# def get_unique(numbers):
# #     unique=[]
# #     for num in numbers:
# #         if num not in unique:
# #             unique.append(num)
# #     return unique
# # print(get_unique(eval(input())))


# 16
# def get_last_index(data, value):
#     ndx=[]
#     for i in range(len(data)):
#         if data[i]==value:
#             ndx.append(i)
#     if len(ndx)==0:
#         return 'ERROR!'
#     return max(ndx)
# print(get_last_index(eval(input()),eval(input())))


# 17
# def find_all(target, symbol):
#     result=[]
#     for i in range(len(target)):
#         if target[i]==symbol:
#             result.append(i)
#     return result
# print(find_all(input(),input()))


# 18
# def merge(list1, list2):
#     l=(list1+list2)
#     l.sort()
#     return l
# print(merge([int(c) for c in input().split()],[int(c) for c in input().split()])


# 19
# def quick_merge(list1, list2):
#     result = []
#
#     p1 = 0  # указатель на первый элемент списка list1
#     p2 = 0  # указатель на первый элемент списка list2
#
#     while p1 < len(list1) and p2 < len(list2):  # пока не закончился какой-нибудь из списков
#         if list1[p1] <= list2[p2]:
#             result.append(list1[p1])
#             p1 += 1
#         else:
#             result.append(list2[p2])
#             p2 += 1
#
#     if p1 < len(list1):  # прицепление остатка
#         result += list1[p1:]
#     else:  # иначе прицепляем остаток другого списка
#         result += list2[p2:]
#
#     return result
#
#
# total_list=[]
# for i in range(int(input())):
#     lst=[int(i) for i in input().split()]
#     total_list=quick_merge(total_list,lst)
# print(*total_list)


# 20
# def is_valid_triangle(side1, side2, side3):
#     if side1+side2>side3 and side2+side3>side1 and side1+side3>side2:
#         return True
#     else:
#         return False
# a, b, c = int(input()), int(input()), int(input())
#
# print(is_valid_triangle(a, b, c))


# 21
# def is_palindrome(text:str):
#     text=text.lower()
#     for i in text:
#         if i in ',.!?- ':
#             text=text.replace(i,'')
#     return text==text[::-1]
# print(is_palindrome(input()))


# 22
# def is_one_away(word1, word2):
#     c=0
#     if len(word1) == len(word2):
#         for i in range(len(word1)):
#             if word1[i] != word2[i]:
#                 c+=1
#     return c==1
# print(is_one_away(input(),input()))


# 23
# def convert_to_python_case(text):
#     txt=text[0].lower()
#     for char in text[1:]:
#         if char.isupper():
#             txt+='_'+char.lower()
#         else:
#             txt+=char
#     return txt
#
#
# txt = input()
#
# print(convert_to_python_case(txt))


# 24
# def is_prime(num):
#     c = 0
#     for i in range(1, num):
#         if num % i == 0:
#             c += 1
#     return c == 1


# 25
# def get_next_prime(num):
#     num += 1
#     while is_prime(num) is False:
#         num += 1
#     return num
# print(get_next_prime(int(input())))


#26
# def is_password_good(password):
#     c=0
#     if len(password)>=8:
#         c+=1
#     for i in range(len(password)):
#         if password[i].isupper():
#             c+=1
#             break
#     for i in range(len(password)):
#         if password[i].islower():
#             c+=1
#             break
#     for i in range(len(password)):
#         if password[i].isdigit():
#             c+=1
#             break
#     return c==4
# print(is_password_good(input()))


#27
# def is_correct_bracket(text):
#     balance=0
#     if text[0]==')':
#         return False
#     for i in range(len(text)):
#         if text[i] == '(':
#             balance+=1
#         elif text[i] == ')':
#             balance-=1
#         if balance==-1:
#             return False
#     return balance==0
#
# print(is_correct_bracket(input()))


#28
# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             return False
#     return True
#
#
# def is_valid_password(password):
#     parts = password.split(':')
#
#     if len(parts) != 3:
#         return False
#
#     p1, p2, p3 = parts
#
#     return (
#         p1 == p1[::-1]
#         and p2.isdigit() and is_prime(int(p2))
#         and p3.isdigit() and int(p3) % 2 == 0
#     )
#
#
# print(is_valid_password(input()))


#29
# def get_middle_point(x1, y1, x2, y2):
#     x_mid=(x1 + x2) / 2
#     y_mid=(y1 + y2) / 2
#     return x_mid, y_mid
# x_1, y_1 = int(input()), int(input())
# x_2, y_2 = int(input()), int(input())
# x, y = get_middle_point(x_1, y_1, x_2, y_2)
# print(x, y)


#30
# from math import pi
# def get_circle(radius):
#     return 2*pi*radius,pi*radius**2
# r = float(input())
# length, square = get_circle(r)
# print(length, square)


#31
# from math import *
# def solve(a, b, c):
#     d = b ** 2 - 4 * a * c
#     if d == 0:
#         x1=-b / (2 * a)
#         x2=-b / (2 * a)
#
#     elif d > 0:
#         x1 = (-b - d ** 0.5) / (2 * a)
#         x2 = (-b + d ** 0.5) / (2 * a)
#     return min(x1, x2),max(x1,x2)
# a, b, c = int(input()), int(input()), int(input())
# x1,x2 = solve(a,b,c)
# print(x1,x2)

#kr1
# def draw_triangle():
#     height = 8
#     for i in range(height):
#         stars = 1 + 2 * i          # количество звёзд в строке: 1,3,5,...
#         spaces = height - i - 1    # отступы слева для центрирования
#         print(' ' * spaces + '*' * stars)
# draw_triangle()


#kr2
# def get_shipping_cost(quantity):
#     return (quantity-1)*120+1000
# print(get_shipping_cost(int(input())))


#kr3
# from math import factorial
# def compute_binom(n, k):
#     return int(factorial(n) / (factorial(k) * factorial(n - k)))
# print(compute_binom(int(input()), int(input())))


#kr4
# zero_to_ninety_nine = ['ноль', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять', 'одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать', 'семнадцать', 'восемнадцать', 'девятнадцать', 'двадцать', 'двадцать один', 'двадцать два', 'двадцать три', 'двадцать четыре', 'двадцать пять', 'двадцать шесть', 'двадцать семь', 'двадцать восемь', 'двадцать девять', 'тридцать', 'тридцать один', 'тридцать два', 'тридцать три', 'тридцать четыре', 'тридцать пять', 'тридцать шесть', 'тридцать семь', 'тридцать восемь', 'тридцать девять', 'сорок', 'сорок один', 'сорок два', 'сорок три', 'сорок четыре', 'сорок пять', 'сорок шесть', 'сорок семь', 'сорок восемь', 'сорок девять', 'пятьдесят', 'пятьдесят один', 'пятьдесят два', 'пятьдесят три', 'пятьдесят четыре', 'пятьдесят пять', 'пятьдесят шесть', 'пятьдесят семь', 'пятьдесят восемь', 'пятьдесят девять', 'шестьдесят', 'шестьдесят один', 'шестьдесят два', 'шестьдесят три', 'шестьдесят четыре', 'шестьдесят пять', 'шестьдесят шесть', 'шестьдесят семь', 'шестьдесят восемь', 'шестьдесят девять', 'семьдесят', 'семьдесят один', 'семьдесят два', 'семьдесят три', 'семьдесят четыре', 'семьдесят пять', 'семьдесят шесть', 'семьдесят семь', 'семьдесят восемь', 'семьдесят девять', 'восемьдесят', 'восемьдесят один', 'восемьдесят два', 'восемьдесят три', 'восемьдесят четыре', 'восемьдесят пять', 'восемьдесят шесть', 'восемьдесят семь', 'восемьдесят восемь', 'восемьдесят девять', 'девяносто', 'девяносто один', 'девяносто два', 'девяносто три', 'девяносто четыре', 'девяносто пять', 'девяносто шесть', 'девяносто семь', 'девяносто восемь', 'девяносто девять']
# def number_to_words(num):
#     return zero_to_ninety_nine[num]
# print(number_to_words(7))


#kr7
# def is_pangram(text):
#     text = text.lower()
#     text=text.replace(' ','')
#     c=[]
#     for i in text:
#         if i not in c:
#             c.append(i)
#     return len(c)==26
# print(is_pangram(input()))


#kr5
# lng_ru = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
#
# lng_en = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
# def get_month(language, number):
#     if language == 'ru':
#         return lng_ru[number-1]
#     elif language == 'en':
#         return lng_en[number-1]
# print(get_month(input(),int(input())))


#kr6
def is_magic(date):
    d, m, y = date.split('.')
    d = int(d)
    m = int(m)
    y = int(y[2:])
    return d * m == y

print(is_magic(input()))






































