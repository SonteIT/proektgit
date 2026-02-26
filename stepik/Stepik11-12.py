# 1
# print(list(range(1,int(input())+1)))
from heapq import nlargest
from http.cookiejar import join_header_words
from itertools import count
from operator import index

# 2
# abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# print(abc[:int(input())])


# 3
# print(list(range(1,int(input())+1,2)))


# 4
# b=input()
# s=[]
# for i in range(0,len(b),2):
#     s.append(b[i])
# print(s)


# 5
# numbers = [2, 6, 3, 14, 10, 4, 11, 16, 12, 5, 4, 16, 1, 0, 8, 16, 10, 10, 8, 5, 1, 11, 10, 10, 12, 0, 0, 6, 14, 8, 2, 12, 14, 5, 6, 12, 1, 2, 10, 14, 9, 1, 15, 1, 2, 14, 16, 6, 7, 5]
# print(len(numbers))
# print(numbers[-1])
# print(numbers[::-1])
# if 5 and 17 in numbers:
#     print('YES')
# else:
#     print('NO')
# del numbers[0]
# del numbers[-1]
# print(numbers)


# 6
# s=[]
# for i in range(int(input())):
#     n=input()
#     s.append(n)
# print(s)


# 7
# abc = 'abcdefghijklmnopqrstuvwxyz'
# s=[]
# for i in range(len(abc)):
#     s.append(abc[i]*(i+1))
# print(s)


# 8
# s=[]
# for i in range(int(input())):
#     n=int(input())
#     s.append(n**3)
# print(s)


# 9
# n=int(input())
# s=[]
# for i in range(1,n+1):
#     if n%i==0:
#         s.append(i)
# print(s)


# 10
# s=[]
# p=0
# for i in range(int(input())):
#     n=int(input())
#     p+=n
#     s.append(p)
#     p=n
# print(s[1:])


# 11
# s=[]
# res=[]
# for i in range(int(input())):
#     s.append(int(input()))
# for i in range(len(s)):
#     if i % 2 == 0:
#         res.append(s[i])
# print(res)


# 12
# s=[]
# p=''
# for i in range(int(input())):
#     n=input()
#     s.append(n)
# k=int(input())
# for stroka in s:
#     if k <= len(stroka):
#         p += stroka[k-1]
# print(p)


# 13
# s=[]
# for i in range(int(input())):
#     s.extend(input())
# print(s)


# 14
# s=[]
# p=[]
# for i in range(int(input())):
#     n=int(input())
#     p.append(n)
#     s.append((n**2)+(2*n)+1)
# for i in p:
#     print(i)
# print()
# for i in s:
#     print(i)


# 15
# s=[]
# for i in range(int(input())):
#     n=int(input())
#     s.append(n)
# s.remove(min(s))
# s.remove(max(s))
# print(*s,sep='\n')


# 16
# s=[]
# res=[]
# for i in range(int(input())):
#     n=input()
#     s.append(n)
#     if n not in res:
#         res.append(n)
# print(*res,sep='\n')


# 17
# s=[]
# for i in range(int(input())):
#     n=input()
#     s.append(n)
# zapros=input()
# for i in s:
#     if zapros.lower() in i.lower():
#         print(i)


# 18
# s=[]
# zap=[]
# p=0
# for i in range(int(input())):
#     n=input()
#     s.append(n)
# for i in range(int(input())):
#     zapros=input()
#     zap.append(zapros)
# for i in s:
#     p=0
#     for j in zap:
#         if j.lower() in i.lower():
#             p+=1
#     if p==len(zap):
#         print(i)


# 19
# otr=[]
# pol=[]
# nol=[]
# s=[]
# for i in range(int(input())):
#     n=int(input())
#     s.append(n)
# for i in s:
#     if i>0:
#         pol.append(i)
#     if i<0:
#         otr.append(i)
#     if i==0:
#         nol.append(i)
# print(*otr,sep='\n')
# print(*nol,sep='\n')
# print(*pol,sep='\n')


# 20
# n=input().split()
# print('\n'.join(n))


# 23
# n=input().split()
# for i in n:
#     print(i[0],end='.')


# 24
# n=input().split("\\")
# print(*n,sep='\n')


# 25
# numbers=input().split()
# for i in range(len(numbers)):
#     numbers[i] = int(numbers[i])
# for i in numbers:
#     print('+'*i,sep='\n')


# 26
# p=[]
# numbers=input().split('.')
# for i in range(len(numbers)):
#     numbers[i] = int(numbers[i])
# for i in numbers:
#     if 0<=i<=255:
#         p.append(i)
# if len(p)==4:
#     print('ДА')
# else:
#     print("НЕТ")


# 27
# n=input()
# razd=input()
# print(razd.join(n))


# 28
# p=0
# n=input().split()
# for i in range(len(n)):
#     n[i] = int(n[i])
# for i in range(len(n)):
#     for j in range(i+1,len(n)):
#         if n[i] == n[j]:
#             p+=1
# print(p)


# 29
# numbers = [8, 9, 10, 11]
# numbers.insert(1,17)
# numbers.remove(9)
#
# numbers.append(4)
# numbers.append(5)
# numbers.append(6)
#
# numbers.pop(0)
#
# numbers*=2
#
# numbers.insert(3,25)
# print(numbers)


# 30
# a=input().lower().split()
# print('Общее количество артиклей:',a.count('a')+a.count('an')+a.count('the'))


# 31
# a=input().split()
# for i in range(len(a)):
#     a[i] = int(a[i])
# ma=max(a)
# mi=min(a)
# ima=a.index(ma)
# imi=a.index(mi)
# a[ima]=mi
# a[imi]=ma
# print(*a)


# 32
# s = []
# k = input()
# k = k[1:]
# for i in range(int(k)):
#     s.append(input())
# for i in s:
#     if '#' in i:
#         resi = i[:i.index('#')]
#         resi = resi.rstrip()
#         s[s.index(i)] = resi
#     else:
#         s[s.index(i)]=i.rstrip()
# print(*s, sep='\n')


#33
# a=input().split()
# for i in range(len(a)):
#     a[i]=int(a[i])
# a.sort()
# print(*a)
# a.sort(reverse=True)
# print(*a)


#34
# s=[]
# for i in range(int(input())):
#     s.append(input())
# s.sort()
# print(*s,sep='\n')


#35
# res=[i**2 for i in range(1,int(input())+1)]
# print(*res,sep='\n')


#36
# print(*[int(i)**3 for i in input().split()])


#37
# print(*[i for i in input().split()], sep='\n')


#38
# print(*[i for i in input() if i.isdigit()],sep='')


#39
# print(*[int(i)**2 for i in input().split() if int(i)%2==0 and (int(i)**2)%10!=4],sep=' ')


#40
# s=[]
# for i in range(0,int(input())+1,2):
#     s.append(i)
# print(s[1:])


#41
# vb=[]
# l=[int(i) for i in input().split()]
# m=[int(i) for i in input().split()]
# for i in range(len(l)):
#     vb.append(l[i]+m[i])
# print(*vb)


#42
# res=[]
# l=[int(i) for i in input().split()]
# summa=sum(l)
# for i in range(len(l)):
#     res.append(l[i])
#     res.append('+')
# print(*res[:-1],'=',summa,sep='')


#43
n=input().split('-')
if  "".join(n).isdigit():
    if len(n)==4:
        if n[0]=='7':
            n=n[1:]
        if len(n[1])==3 and len(n[2])==3 and len(n[3])==4:
            print('yes')
        else:
            print('no')
    if len(n)==3:
        if len(n[1])==3 and len(n[2])==3 and len(n[3])==4:
            print('yes')
        else:
            print('no')
else:
    print('no')







