from random import randint
N=int(input())
A=[0]*N
for i in range(N):
    A[i]=randint(10,99)
print(A)
print()
k=len(A)
print('Количество чисел в массиве A:',k)
s=sum(A)
print('Сумма чисел в массиве A:',s)
print()
K1=0
S1=0
K2=0
S2=0
K3=0
S3=0
K5=0
S5=0
for i in range(N):
    if '5' in str(A[i]):
        K5+=1
        S5+=A[i]
    if str(A[i])==str(A[i])[::-1]:
        K3+=1
        S3+=A[i]
    if A[i]%2!=0:
        K1+=1
        S1+=A[i]
    else:
        K2+=1
        S2+=A[i]
if K1==0:
    print('НЕТ')
    print()
else:
    print('Количество нечетных чисел в массиве A:',K1)
    print('Сумма нечетных чисел в массиве A:', S1)
    print()
if K2==0:
    print('НЕТ')
    print()
else:
    print('Количество четных чисел в массиве A:',K2)
    print('Сумма четных чисел в массиве A:', S2)
    print()
print('Количество палиндромов в массиве A:',K3)
print('Сумма палиндромов в массиве A:',S3)
print()
print('Количество чисел содержащих цифру 5:',K5)
print('Сумма чисел содержащих цифру 5:',S5)








