from ctypes.macholib.framework import framework_info
from math import *
#1
# a,b,=float(input()),float(input())
# print((a*b)/2)

#2
# c=float(input())
# a=float(input())
# b=float(input())
# print(c/(a+b))

#3
# a=float(input())
# if a==0:
#     print('Обратного числа не существует')
#     exit()
# print(a**-1)

#4
# a=float(input())
# print((5/9)*(a-32))

#5
# a=float(input())
# if a-2>=1:
#     print(int((a-2)*4+21))
# else:
#     print(a*10.5)

#6
# a=float(input())
# print(int((a*10)%10))

#7
# a=float(input())
# o=a%(a//a)
# print(o)

#8
# a=[int(input()),int(input()),int(input()),int(input()),int(input())]
# print('Наименьшее число =',min(a))
# print('Наибольшее число =',max(a))

#9
# a=[int(input()),int(input()),int(input())]
# print(max(a))
# print(sum(a)-max(a)-min(a))
# print(min(a))

#10
# n=int(input())
# a=n//100
# b=(n//10)%10
# c=n%10
# if max(a,b,c)-min(a,b,c)==a+b+c-(max(a,b,c)+min(a,b,c)):
#     print("Число интересное")
# else:
#     print('Число неинтересное')

#11
# a=float(input())
# b=float(input())
# c=float(input())
# d=float(input())
# e=float(input())
# print(abs(a)+abs(b)+abs(c)+abs(d)+abs(e))


#12
# p1=int(input())
# p2=int(input())
# q1=int(input())
# q2=int(input())
# print(abs(p1-q1)+abs(p2-q2))

#13
# print('''"Python is a great language!", said Fred. "I don't ever remember having this much fun before."''')

#14
# a=input()
# b=input()
# print(f'Hello {a} {b}! You have just delved into Python')

#15
# a=input()
# print('Футбольная команда',a, 'имеет длину',len(a),'символов')

#16
# a=input()
# b=input()
# c=input()
# x=min(len(a),len(b),len(c))
# y=max(len(a),len(b),len(c))
# if len(a)==x:
#     print(a)
# elif len(b)==x:
#     print(b)
# elif len(c)==x:
#     print(c)
# if len(a)==y:
#     print(a)
# elif len(b)==y:
#     print(b)
# elif len(c)==y:
#     print(c)


#17
# a=len(input())
# b=len(input())
# c=len(input())
# S=a+b+c
# MI=min(a,b,c)
# MA=max(a,b,c)
# SR=S-MA-MI
# if MA-SR==SR-MI:
#     print("YES")
# else:
#     print("NO")

#18
# a=input()
# if 'синий' in a:
#     print('YES')
# else:
#     print('NO')

#19
# a=input()
# if 'суббота' in a or 'воскресенье' in a:
#     print('YES')
# else:
#     print('NO')

#19
# a=input()
# if '@' in a and '.' in a:
#     print('YES')
# else:
#     print('NO')

#20
# from math import *
# x1=float(input())
# y1=float(input())
# x2=float(input())
# y2=float(input())
# print(sqrt((x1-x2)**2 + (y1-y2)**2))

#21
# from math import *
# r=float(input())
# print(pi*r**2)
# print(2*pi*r)

#22
# from math import *
# a=float(input())
# b=float(input())
# print((a+b)/2)
# print(sqrt(a*b))
# print(2*a*b/(a+b))
# print(sqrt((a**2+b**2)/2))

#23
# from math import *
# x=float(input())
# print(sin(radians(x))+cos(radians(x))+(tan(radians(x))**2))

#24
# from math import *
# a=float(input())
# print(floor(a)+ceil(a))

#25
# from math import *
# a=float(input())
# b=float(input())
# c=float(input())
# D=b**2-4*a*c
# if D<0:
#     print('Нет корней')
#     exit()
# if D==0:
#     x=-b/(2*a)
#     print(x)
#     exit()
# if D>0:
#     x1 = (-b - sqrt(D)) / (2 * a)
#     x2 = (-b + sqrt(D)) / (2 * a)
#     if x1>x2:
#         print(x2)
#         print(x1)
#     else:
#         print(x1)
#         print(x2)

#26
# from math import *
# n=int(input())
# a=float(input())
# print((n*a**2)/(4*tan(pi/n)))