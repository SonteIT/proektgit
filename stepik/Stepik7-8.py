# 1
# for i in range(10):
#     print('Python is awesome!')

# 2
# for i in range(6):
#     print('AAA')
# for i in range(5):
#     print('BBBB')
# print('E')
# for i in range(9):
#     print('TTTTT')
# print('G')

# 3
# b=input()
# a=int(input())
# for i in range(a):
#     print(b)

# 4
# b=int(input())
# for i in range(b):
#     print('*'*19)

# 5
# b=input()
# for i in range(10):
#     print(i,b)

# 6
# n=int(input())
# for i in range(0,n+1):
#     print('Квадрат числа',i,'равен',i**2)

# 7
# n=int(input())
# for i in range(n,0,-1):
#     print('*'*i)

# 8
# m=int(input())
# p=int(input())
# n=int(input())
# for i in range(0,n):
#     print(i+1,m*(1+p/(100))**i)

# 9
# m=int(input())
# n=int(input())
# for i in range(m,n+1):
#     print(i)

# 10
# m=int(input())
# n=int(input())
# if m<n:
#     for i in range(m,n+1):
#         print(i)
# else:
#     for i in range(m,n-1,-1):
#         print(i)

# 11
# m=int(input())
# n=int(input())
# for i in range(m,n-1,-1):
#     if i%2!=0:
#         print(i)

# 12
# m=int(input())
# n=int(input())
# for i in range(m,n+1):
#     if i%17==0 or i%10==9 or (i%3==0 and i%5==0):
#         print(i)

# 13
# n=int(input())
# for i in range(1,11):
#     print(n,'x',i,'=',n*i)

# 14
# a=int(input())
# b=int(input())
# s=0
# for i in range(a,b+1):
#     if ((i**3)%10==4) or ((i**3)%10==9):
#         s+=1
# print(s)

# 15
# n=int(input())
# t=0
# for i in range(n):
#     a=int(input())
#     t+=a
# print(t)

# 16
# from math import *
# result = 0
# n = int(input())
# for i in range(1, n + 1):
#     result += (1 / i)
# print(result - log(n))

# 17
# n=int(input())
# t=0
# for i in range(1,n+1):
#     if (i**2)%10==2 or (i**2)%10==5 or (i**2)%10==8:
#         t+=i
# print(t)

# 18
# n=int(input())
# p=1
# for i in range(2,n+1):
#     p=p*i
# print(p)

# 19
# p=1
# for i in range(10):
#     a=int(input())
#     if a!=0:
#         p*=a
# print(p)

# 20
# n=int(input())
# t=0
# for i in range(1,n+1):
#     if n%i==0:
#         t+=i
# print(t)

# 21
# t=0
# p=0
# for i in range(10):
#     a=int(input())
#     if a%2==0:
#         t+=a
#         p+=1
# if p==10:
#     print('YES')
# else:
#     print('NO')

# 22
# n=int(input())
# t=0
# for i in range(1,n+1):
#     if i%2==0:
#         t-=i
#     if i%2!=0:
#         t+=i
# print(t)

# 23
# n=int(input())
# max1=2
# max2=2
# for i in range(1,n+1):
#     a=int(input())
#     if a>max1:
#         max2=max1
#         max1=a
#     elif a>max2:
#         max2=a
# print(max1)
# print(max2)

# 24
# n=int(input())
# tekfib=1
# sledfib=1
# for i in range(n):
#     print(tekfib,end=' ')
#     tekfib,sledfib=sledfib,sledfib+tekfib

# 25
# a=input()
# while a!='КОНЕЦ':
#     print(a)
#     a=input()

# 26
# a=input()
# while a!='КОНЕЦ' and a!='конец':
#     print(a)
#     a=input()

# 27
# a=input()
# s=0
# while a!='стоп' and a!='хватит' and a!='достаточно':
#     s+=1
#     a=input()
# print(s)

# 28
# a=int(input())
# while a%7==0:
#     print(a)
#     a=int(input())

# 29
# a=int(input())
# t=0
# while a>=0:
#     t+=a
#     a=int(input())
# print(t)

# 30
# a=int(input())
# s=0
# while a<6 and a>0:
#     if a==5:
#         s+=1
#     a = int(input())
# print(s)

# 31
# n=int(input())
# s=0
# while n>=25:
#     n-=25
#     s+=1
# while n>=10:
#     n-=10
#     s+=1
# while n>=5:
#     n-=5
#     s+=1
# while n>=1:
#     n-=1
#     s+=1
# print(s)

# 32
# a=int(input())
# while a!=0:
#     print(a%10)
#     a//=10

# 33
# a=int(input())
# while a!=0:
#     print(a%10,end='')
#     a//=10

# 34
# a=int(input())
# MA=0
# MI=9
# while a!=0:
#     if a%10>MA:
#         MA=a%10
#     if a%10<MI:
#         MI=a%10
#     a=a//10
# print('Максимальная цифра равна',MA)
# print('Минимальная цифра равна',MI)

# 35
# a=int(input())
# b=a
# total=0
# kolvo=0
# proizved=1
# while a!=0:
#     total+=a%10
#     proizved*=a%10
#     a//=10
#     kolvo+=1
# kolvonul=kolvo-1
# delitel='1'+('0'*kolvonul)
# perv=b//int(delitel)
# print(total)
# print(kolvo)
# print(proizved)
# print(total/kolvo)
# print(perv)
# print((b%10)+perv)

# 36
# a=int(input())
# while a>=100:
#     a=a//10
# print(a%10)

# 37
# a=int(input())
# s=0
# posl=a%10
# while a>0:
#     novayaposl=a%10
#     a=a//10
#     if posl!=novayaposl:
#         s+=1
# if s>0:
#     print('NO')
# else:
#     print('YES')

# 38
# a=int(input())
# while a>=10:
#     if a%10<=((a//10)%10):
#         a=a//10
#     else:
#         print('NO')
#         exit()
# print('YES')

# 39
# a=int(input())
# for i in range(2,a+1):
#     if a%i==0:
#         print(i)
#         break


# 40
# n = int(input())
# for i in range(1, n + 1):
#     if (i >= 5 and i <= 9) or (i >= 17 and i <= 37) or (i >= 78 and i <= 87):
#         continue
#     print(i)

# a=int(input())
# res=1
# while a:
#     res*=a%10
#     a=a//10
# print(res)

# n=int(input())
# while n>9:
#     n=n//10
# print(n)

# 41
# a=int(input())
# for i in range(a):
#     for j in range(3):
#         print(a,end=" ")
#     print()

# 42
# a=int(input())
# for i in range(a):
#     print(i+1,end=" ")
#     for j in range(4):
#         print(i+1,end=" ")
#     print()

# 43
# n = int(input())
# for i in range(1,n+1):
#     for j in range(1,10):
#         print(i,'+',j,'=',i+j)
#     print()

#44
# n=int(input())
# for i in range(1,n//2+2,1):
#     print('*'*i)
# for j in range(n//2,0,-1):
#     print('*'*j)

#45
# n = int(input())
# for i in range(1, n+1):
#     for j in range(1, i + 1):
#         print(i,end='')
#     print()

#46
#
# from math import sqrt
# for n in range(0,19):
#     for k in range(0,19):
#         for m in range(0,19):
#             if 28*n+30*k+31*m==365:
#                 print(n,k,m,sep=' ')

#47
# for b in range(1,11):
#     for k in range(1,21):
#         for t in range(1,101):
#             if (10*b+5*k+0.5*t)==100 and (b+k+t==100):
#                 print(b,k,t)

#48
# p=151
# for a in range(1,p):
#     for b in range(a,p):
#         for c in range(b,p):
#             for d in range(c,p):
#                 for e in range(d,p):
#                     if (a**5+b**5+c**5+d**5)==e**5:
#                         print(a+b+c+d+e)
#                         print(a,b,c,d,e)

#49
# n=int(input())
# s=0
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         s+=1
#         print(s,end=" ")
#     print()

#51
# n=int(input())
# d=0
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         if i % j == 0:
#             d+=1
#     print(str(i)+'+'*d,end="")
#     d=0
#     print()

#52
# a=int(input())
# # b=int(input())
# # tekmax=0
# # maxsum=0
# # maxc=0
# # for i in range(a,b+1):
# #     tekmax = 0
# #     for j in range(1,i+1):
# #         if i%j==0:
# #             tekmax+=j
# #     if tekmax>maxsum:
# #         maxsum=tekmax
# #         maxc=i
# #     elif tekmax==maxsum:
# #         if i > maxc:
# #             maxc=i
# # print(maxc,maxsum)

#53
# n=int(input())
# p=0
# while n>9:
#     while n!=0:
#         posl=n%10
#         p+=posl
#         n//=10
#     n=p
#     p=0
# print(n)

#54
# n=int(input())
# s=0
# for i in range(1,n+1):
#     p=1
#     for j in range(1, i + 1):
#         p = p * j
#     s+=p
# print(s)

#55
# a=int(input())
# b=int(input())
# for i in range(a,b+1):
#     count=0
#     for j in range(1,i+1):
#         if i%j==0:
#             count+=1
#     if count==2:
#         print(i)

#kr1
# n=int(input())
# for i in range(n):
#     if i==0 or i==n-1:
#         print('*'*19)
#     else:
#         print('*',' '*17,'*',sep='')

#kr2
# n1 = int(input())
# digit = n1 % 10
# n2 = digit
# n1 = n1 // 10
# while n1 > 0:
#     digit = n1 % 10
#     n1 = n1 // 10
#     n2 = n2 * 10
#     n2 = n2 + digit
# print((n2//100)%10)

#kr3
# a=int(input())
# nolpyat=0
# kaka=0
# proizvbol7=1
# sumbol5=0
# troyki=0
# kolposl=0
# chet=0
# posl=a%10
# for i in str(a):
#     if i=='3':
#         troyki+=1
#     if int(i)==posl:
#         kolposl+=1
#     if int(i)%2==0:
#         chet+=1
#     if int(i)>5:
#         sumbol5+=int(i)
#     if int(i)>7:
#         proizvbol7*=int(i)
#         kaka+=1
#     if int(i)==0:
#         nolpyat+=1
#     if int(i)==5:
#         nolpyat+=1
# print(troyki)
# print(kolposl)
# print(chet)
# print(sumbol5)
# if kaka==0:
#     print(1)
# else:
#     print(proizvbol7)
# print(nolpyat)

#kr4
s=[]
for a in range(1,51):
    for b in range(1,51):
        for c in range(1,51):
            for d in range(1,51):
                if a**3+b**3==c**3+d**3:
                        num=a**3+b**3
                        if num not in s:
                            s.append(num)
print(s)







