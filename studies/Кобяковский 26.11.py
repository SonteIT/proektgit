from random import randint


def sums_of_diagonals(N):
    A = [[randint(1, 9) for j in range(N)] for i in range(N)]

    print()

    for i in range(N):
        for j in range(N):
            print(A[i][j], end=' ')
        print()


    summa_gl_d = 0
    for i in range(N):
        summa_gl_d += A[i][i]

    summa_pob_d = 0
    for i in range(N):
        j = N - 1 - i
        summa_pob_d += A[i][j]

    return f'\nСумма чисел главной диагонали: {summa_gl_d}, сумма чисел побочной диагонали: {summa_pob_d}'


print(sums_of_diagonals(int(input('Введите размерность матрицы: '))))
