"""создать квадратную матрицу случайных чисел,
найти суммы чисел воротников,включая их границы"""
from random import randint

N = int(input("Введите размерность матрицы: "))
print()
A = [[randint(1, 9) for j in range(N)] for i in range(N)]
for i in range(N):
    for j in range(N):
        print(A[i][j], end=' ')
    print()
print()
t = r = l = b = 0

for i in range(N):
    for j in range(N):
        if i < j and i + j < N - 1:
            t += A[i][j]
        if i < j and i + j > N - 1:
            r += A[i][j]
        if i > j and i + j < N - 1:
            l += A[i][j]
        if i > j and i + j > N - 1:
            b += A[i][j]
print("Сумма чисел верхнего воротника: ", t)
print("Сумма чисел правого воротника: ", r)
print("Сумма чисел нижнего воротника: ", b)
print("Сумма чисел левого воротника: ", l)
