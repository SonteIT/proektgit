from random import randint
N=int(input('Введите кол-во строк: '))
M=int(input('Введите кол-во столбцов: '))
A=[[randint(10,99) for j in range(M)] for i in range(N)]
print()

for i in range(N):
    for j in range(M):
       print(A[i][j],end=' ')
    print()

for i in range(0,N-1,2):
    A[i],A[i+1]=A[i+1],A[i]

print()
for i in range(N):
    for j in range(M):
       print(A[i][j],end=' ')
    print()
