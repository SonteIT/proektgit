# 1
# a=input()
# b=input()
# if a==b:
#     print('Пароль принят')
# else:
#     print('Пароль не принят')

# 2
# a = int(input())
# if a % 2 == 0:
#     print('Четное')
# else:
#     print('Нечетное')

# 3
# k = int(input())
# a = k // 1000
# b = (k // 100) % 10
# c = (k // 10) % 10
# d = k % 10
# if a + d == b - c:
#     print('ДА')
# else:
#     print('НЕТ')

# 4
# a = int(input())
# if a < 18:
#     print('Доступ запрещен')
# else:
#     print('Доступ разрешен')

# 5
# a=int(input())
# b=int(input())
# c=int(input())
# if b-a==c-b:
#     print('YES')
# else:
#     print('NO')

# 6
# a = int(input())
# b = int(input())
# minim = 0
# if a < b:
#     minim = a
#     print(a)
# if b < a:
#     minim = b
#     print(b)
# if a == b:
#     print(a)

# 7
# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# print(min(a, b, c, d))

# 8
# a = int(input())
# if a <= 13:
#     print('детство')
# if a > 13 and a <= 24:
#     print('молодость')
# if a > 24 and a <= 59:
#     print('зрелость')
# if a > 59:
#     print('старость')

# 9
# a=int(input())
# b=int(input())
# c=int(input())
# s=0
# if a>0:
#     s+=a
# if b>0:
#     s+=b
# if c>0:
#     s+=c
# print(s)

# 10
# a = int(input())
# if a > -1 and a < 17:
#     print('Принадлежит')
# else:
#     print('Не принадлежит')

# 11
# a = int(input())
# if a <= -3 or a >= 7:
#     print('Принадлежит')
# else:
#     print('Не принадлежит')

#12
# a=int(input())
# if a>-30 and  a<=-2 or a>7 and a<=25:
#     print('Принадлежит')
# else:
#     print('Не принадлежит')

#13
# a=int(input())
# if a>=1000 and a<=9999:
#     if a%7==0 or a%17==0:
#         print('YES')
#     else:
#         print('NO')
# else:
#     print('NO')

#14
# a=int(input())
# b=int(input())
# c=int(input())
# if b+c>a and b+a>c and c+a>b:
#     print('YES')
# else:
#     print('NO')

#15
# a=int(input())
# if a%4==0 and a%100!=0 or a%400==0:
#     print("YES")
# else:
#     print("NO")

#16
# a=int(input())
# b=int(input())
# c=int(input())
# d=int(input())
# if a==c or b==d:
#     print("YES")
# else:
#     print('NO')

#17
# a=int(input())
# b=int(input())
# c=int(input())
# d=int(input())
# if abs(a-c)<=1 and abs(b-d)<=1:
#     print("YES")
# else:
#     print("NO")


#18
# a=int(input())
# b=int(input())
# if a>b:
#     print('NO')
# if a<b:
#     print('YES')
# if a==b:
#     print("Don't",'know')

#19
# a=int(input())
# b=int(input())
# c=int(input())
# if a==b==c:
#     print('Равносторонний')
#     exit()
# if a==b or a==c or b==c:
#     print('Равнобедренный')
#     exit()
# else:
#     print('Разносторонний')

#20
# a=int(input())
# b=int(input())
# c=int(input())
# if a<b<c or c>b>a:
#     print(b)
# elif c<a<b or c>a>b:
#     print(a)
# else:
#     print(c)

#21
# a=int(input())
# if a==1 or a==3 or a==5 or a==7 or a==8 or a==10 or a==12:
#     print(31)
# elif a==4 or a==6 or a==9 or a==11:
#     print(30)
# else:
#     print(28)

#22
# w=int(input())
# if w<60:
#     print('Легкий вес')
# elif w<64:
#     print('Первый полусредний вес')
# elif w<69:
#     print('Полусредний вес')

#23
# a=int(input())
# b=int(input())
# c=input()
# if c=='+' or c=='-' or c=='*' or c=='/':
#     if c=='+':
#         print(a+b)
#     elif c=='-':
#         print(a-b)
#     elif c=='*':
#         print(a*b)
#     elif c=='/':
#         if b==0:
#             print('На ноль делить нельзя!')
#             exit()
#         print(a/b)
# else:
#     print('Неверная операция')

#24
# a=input()
# b=input()
# if a!='красный' and a!='синий' and a!='желтый':
#     print('ошибка цвета')
#     exit()
# if b != 'красный' and b != 'синий' and b != 'желтый':
#     print('ошибка цвета')
#     exit()
# if a=='красный' and b=='синий' or a=='синий' and b=='красный':
#     print('фиолетовый')
# elif a=='желтый' and b=='синий' or a=='синий' and b=='желтый':
#     print('зеленый')
# elif a=='красный' and b=='желтый' or a=='желтый' and b=='красный':
#     print('оранжевый')
# elif a=='красный' and b=='красный':
#     print('красный')
# elif a=='желтый' and b=='желтый':
#     print('желтый')
# elif a=='синий' and b=='синий':
#     print('синий')

#25
# a=int(input())
# r='красный'
# b='черный'
# if a>36 or a<0:
#     print('ошибка ввода')
#     exit()
# if a==0:
#     print('зеленый')
# if a>=1 and a<=10:
#     if a%2!=0:
#         print(r)
#     if a%2==0:
#         print(b)
#
# if a>=11 and a<=18:
#     if a%2!=0:
#         print(b)
#     if a%2==0:
#         print(r)
#
# if a>=19 and a<=28:
#     if a%2!=0:
#         print(r)
#     if a%2==0:
#         print(b)
#
# if a>=29 and a<=36:
#     if a%2!=0:
#         print(b)
#     if a%2==0:
#         print(r)

# a1=int(input())
# b1=int(input())
# a2=int(input())
# b2=int(input())
# if a2>a1 and b2>b1:
#     print(a2,b2)
#     exit()
# if a1>a2 and b2>b1:
#     print(a1,b1)
# elif b1-a2>0:
#     print(a2,b1)
# elif b1-a2==0:
#     print(a2)
# elif b1-a2<0:
#     print('пустое множество')

#kr1
# a=int(input())
# if a%100==0:
#     print('YES')
# else:
#     print('NO')

#kr2
# a=int(input())
# b=int(input())
# c=int(input())
# d=int(input())
# if (a+b)%2==0 and (c+d)%2==0 or ((a+b)%2!=0 and (c+d)%2!=0):
#     print('YES')
# else:
#     print('NO')

#kr3
# a=int(input())
# b=input()
# if b=='f' and a>=10 and a<=15:
#     print('YES')
# else:
#     print('NO')

#kr4
# a = int(input())
# if a>10 or a<1:
#     print('ошибка')
#     exit()
# if a == 1:
#     print('I')
# if a == 2:
#     print('II')
# if a == 3:
#     print('III')
# if a == 4:
#     print('IV')
# if a == 5:
#     print('V')
# if a == 6:
#     print('VI')
# if a == 7:
#     print('VII')
# if a == 8:
#     print('VIII')
# if a == 9:
#     print('IX')
# if a == 10:
#     print('X')

#kr5
# a=int(input())
# if a%2!=0:
#     print('YES')
#     exit()
# if a%2==0 and a>=2 and a<=5:
#     print('NO')
#     exit()
# if a%2==0 and a>=6 and a<=20:
#     print('YES')
#     exit()
# if a%2==0 and a>20:
#     print('NO')
#     exit()

#kr6
# a=int(input())
# b=int(input())
# c=int(input())
# d=int(input())
# if a+b==c+d or a-b==c-d:
#     print('YES')
# else:
#     print('NO')


#kr7
# a=int(input())
# b=int(input())
# c=int(input())
# d=int(input())
# if abs(c-a)==1 and abs(d-b)==2 or (abs(a-c)==2 and abs(d-b)==1):
#     print('YES')
# else:
#     print('NO')

#kr8
# a=int(input())
# b=int(input())
# c=int(input())
# d=int(input())
# if (a+b==c+d or a-b==c-d) or (a==c or b==d):
#     print('YES')
# else:
#     print('NO')


