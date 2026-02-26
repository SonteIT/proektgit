# a=int(input())
# print(a)
# a+=1
# print(a)
# a+=1
# print(a)

#2
# a,b,c=int(input()),int(input()),int(input())
# print(sum([a,b,c]))

#3
# a,b,c,d=int(input()),int(input()),int(input()),int(input())
# print(sum((a,b,c,d)*3))

#4
# a=int(input())
# b=int(input())
# print(3 * ((a+b) * (a+b) * (a+b))+275*(b*b)-127*a-41)

#5
# a=int(input())
# print('Следующее за числом',a,'число:',a+1)
# print('Для числа',a, 'предыдущее число:',a-1)

#6
# a=int(input())
# print('Объем =',a*a*a)
# print('Площадь полной поверхности =',6*(a*a))

#7
# a=int(input())
# b=int(input())
# print(str(a),'+',str(b),'=',a+b)
# print(str(a),'-',str(b),'=',a-b)
# print(str(a),'*',str(b),'=',a*b)

#8
# a1=int(input())
# d=int(input())
# n=int(input())
# aN=a1+d*(n-1)
# print(aN)

#9
# a=int(input())
# print(a,a*2,a*3,a*4,a*5,sep='---')

#10
# b1=int(input())
# q=int(input())
# n=int(input())
# print(b1*q**(n-1))

#11
# print(int(input())//100)

#12
# n=int(input())
# k=int(input())
# print(k//n)
# print(k%n)

#13
# n=int(input())
# if n%2==0:
#     print(n//2)
# else:
#     print((n//2)+1)

#14
# a=int(input())
# b=a//60
# c=a-b*60
# print(a,'мин - это',b,'час',c,'минут.')

#15
# a=int(input())
# b=a+3
# res=b//4
# print(res)

#16
# a=int(input())
# pervaya=a//100
# vtoraya=(a//10)%10
# tretya=a%10
# print('Сумма цифр =',pervaya+vtoraya+tretya)
# print('Произведение цифр =',pervaya*vtoraya*tretya)

#17
# a=int(input())
# pervaya=a//100
# vtoraya=(a//10)%10
# tretya=a%10
# print(pervaya,vtoraya,tretya,sep='')
# print(pervaya,tretya,vtoraya,sep='')
# print(vtoraya,pervaya,tretya,sep='')
# print(vtoraya,tretya,pervaya,sep='')
# print(tretya,pervaya,vtoraya,sep='')
# print(tretya,vtoraya,pervaya,sep='')

#18
# k=int(input())
# a=k//1000
# b=(k//100)%10
# c=(k//10)%10
# d=k%10
# print('Цифра в позиции тысяч равна', a)
# print('Цифра в позиции сотен равна', b)
# print('Цифра в позиции десятков равна', c)
# print('Цифра в позиции единиц равна', d)

#kr2
# a=int(input())
# b=int(input())
# ks=a**2+2*(a*b)+b**2
# sk=a**2+b**2
# print('Квадрат суммы',a,'и',b,'равен',ks)
# print('Сумма квадратов',a,'и',b,'равна',sk)

#kr3
# a=int(input())
# b=int(input())
# c=int(input())
# d=int(input())
# print(a**b+c**d)

#kr4
# a=int(input())
# b=a*10+a
# c=b*10+a
# print(a+b+c)