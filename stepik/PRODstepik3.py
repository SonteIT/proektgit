# 1
# def func(num1, num2):
#     return num1 % num2 == 0
# print(func(int(input()), int(input())))


# 2
# list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# list1[2][2].append(7000)
#
# print(list1)


# 3
# list1 = ['a', 'b', ['c', ['d', 'e', ['f', 'g'], 'k'], 'l'], 'm', 'n']
# sub_list = ['h', 'i', 'j']
# list1[2][1][2].extend(sub_list)
# print(list1)


# 4
# list1 = [[1, 7, 8], [9, 7, 102], [6, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
# maximum = 0
# for i in range(len(list1)):
#     for j in range(len(list1[i])):
#         if list1[i][j] > maximum:
#             maximum = list1[i][j]
# print(maximum)


# 5
# list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
# for i in list1:
#     i = i.reverse()
#
# print(list1)


# 6
# list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
# total = 0
# counter = 0
# for i in range (len(list1)):
#     for j in range(len(list1[i])):
#         total += list1[i][j]
#         counter += 1
# print(total/counter)


# 7
# n = int(input())
# s = []
# for i in range(1,n+1):
#     s.append(i)
# for i in range(n):
#     print(s)


# 8
# n = int(input())
# s = [[j for j in range(1, i+1)] for i in range(1, n+1)]
# print(*s,sep='\n')
#
#

# 9
# n = int(input())
# s = []
# for i in range(n+1):
#     row = [1]*(i+1)
#     for j in range(i+1):
#         if j != 0 and j != i:
#             row[j] = s[i-1][j] + s[i-1][j-1]
#     s.append(row)
# print(s[-1])


# 10
# n = input().replace(' ', '')
# spisres = []
# tek_group = [n[0]]
# for i in range(1,len(n)):
#     if n[i] == n[i - 1]:
#         tek_group.append(n[i])
#     else:
#         spisres.append(tek_group)
#         tek_group = [n[i]]
# spisres.append(tek_group)
#
#
# print(spisres)


# 11
# def chunked(l, n):
#     l = [i for i in l.split()]
#     p = []
#     for i in range(0, len(l), n):
#         p.append(l[i:i + n])
#     return p
#
#
# print(chunked(input(), int(input())))


# 13
# n = int(input())
# m = int(input())
# A = [[0] * m for i in range(n)]
# for i in range(n):
#     for j in range(m):
#         A[i][j] = input()
# for i in range(n):
#     for j in range(m):
#         print(A[i][j], end=' ')
#     print()
#
# print()
#
# for i in range(m):
#     for j in range(n):
#         print(A[j][i], end=' ')
#     print()


# 14
# n = int(input())
# s = 0
# matrix = []
# for i in range(n):
#     temp = [int(num) for num in input().split()]
#     matrix.append(temp)
# for i in range(n):
#     for j in range(n):
#         if i == j:
#             s += matrix[i][j]
# print(s)

# 15
# n = int(input())
# matrix = []
# s = 0
# for i in range(n):
#     temp = [int(num) for num in input().split()]
#     matrix.append(temp)
# for i in range(n):
#     s = 0
#     for j in range(n):
#         if matrix[i][j] > sum(matrix[i]) / len(matrix[i]):
#             s += 1
#     print(s)


# # 16
# n = int(input())
# matrix = []
# m = -9999999999999999
# for i in range(n):
#     temp = [int(num) for num in input().split()]
#     matrix.append(temp)
# for i in range(n):
#     for j in range(n):
#         if i >= j:
#             if matrix[i][j] > m:
#                 m = matrix[i][j]
# print(m)


# 17
# n = int(input())
# matrix = []
# m = -9999999999999999
# for i in range(n):
#     temp = [int(num) for num in input().split()]
#     matrix.append(temp)
# for i in range(n):
#     for j in range(n):
#         if (i >= j and i <= n - 1 -j) or (i <= j and i >= n - 1 -j):
#             if matrix[i][j] > m:
#                 m = matrix[i][j]
# print(m)


# 18
# n = int(input())
# matrix = []
# s_up = s_down = s_left = s_right = 0
# for i in range(n):
#     temp = [int(num) for num in input().split()]
#     matrix.append(temp)
# for i in range(n):
#     for j in range(n):
#         if i < j and i < n - 1 - j:
#             s_up += matrix[i][j]
#         if i < j and i > n - 1 - j:
#             s_right += matrix[i][j]
#         if i > j and i > n - 1 - j:
#             s_down += matrix[i][j]
#         if i > j and i < n - 1 - j:
#             s_left += matrix[i][j]
# print(f'Верхняя четверть: {s_up}')
# print(f'Правая четверть: {s_right}')
# print(f'Нижняя четверть: {s_down}')
# print(f'Левая четверть: {s_left}')


# 19
# n = int(input())
# m = int(input())
# for i in range(n):
#     for j in range(m):
#         A = [[str((i * j)).ljust(2) for j in range(m)] for i in range(n)]
# for i in range(n):
#     for j in range(m):
#         print(A[i][j], end=" ")
#     print()


# 20
# n = int(input())
# m = int(input())
# matrix = []
# maxmimum = -99999999
# m_ind = ''
# for i in range(n):
#     temp = [int(num) for num in input().split()]
#     matrix.append(temp)
# for i in range(n):
#     for j in range(m):
#         if matrix[i][j] > maxmimum:
#             maxmimum = matrix[i][j]
#             m_ind = str(i) + ' ' +  str(j)
# print(m_ind)


# 21
# n = int(input())
# m = int(input())
# matrix = []
# for p in range(n):
#     temp = [int(num) for num in input().split()]
#     matrix.append(temp)
# i, j = map(int, input().split())
# for k in range(n):
#     matrix[k][i],matrix[k][j] = matrix[k][j],matrix[k][i]
# for i in range(n):
#     for j in range(m):
#         print(matrix[i][j],end=' ')
#     print()


# 22
# n = int(input())
# matrix = []
# res = 'YES'
# for p in range(n):
#     temp = [int(num) for num in input().split()]
#     matrix.append(temp)
# for i in range(n):
#     for j in range(n):
#         if i != j:
#             if matrix[i][j] != matrix[j][i]:
#                 res = 'NO'
#                 break
# print(res)


# 23
# n = int(input())
# matrix = []
# for p in range(n):
#     temp = [int(num) for num in input().split()]
#     matrix.append(temp)
# matrix.reverse()
# for i in matrix:
#     print(*i)


# 24
# n = int(input())
# matrix = []
# for p in range(n):
#     temp = [int(num) for num in input().split()]
#     matrix.append(temp)
#
# matrix_po = []
# for i in range(n):
#     for j in range(n):
#         if matrix[i][j] not in matrix_po and (matrix[i][j] != 0):
#             matrix_po.append(matrix[i][j])
#         else:
#             print('NO')
#             exit()
#
# s_st = sum(row[0] for row in matrix)
#
# s_d_g = 0
# s_d_p = 0
#
# z = 0
#
# flag = True
#
# for i in range(n):
#     for j in range(n):
#         if i == j:
#             s_d_g += matrix[i][j]
#         if j == n - i - 1:
#             s_d_p += matrix[i][j]
#
# if s_d_g != s_d_p:
#     flag = False
#
# s_s = sum(matrix[0])
# for i in range(n):
#     if sum(matrix[i]) != s_s:
#         flag = False
#
# for j in range(n):
#     current_column_sum = 0
#     for i in range(n):
#         current_column_sum += matrix[i][j]
#
#     if current_column_sum != s_st:
#         flag = False
# if s_s == s_d_g == s_d_p == s_st:
#     print("YES")
# else:
#     print("NO")

n = int(input())
m = int(input())
a = [[0 for i in range(m)]for j in range(n)]
print(a)