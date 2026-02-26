# 1
# def matrix(n=0, m=0 ,value=None):
#     if n == 0 and m == 0:
#         return [[0]]
#
#     elif n != 0 and m == 0:
#         return [[0 for i in range(n)]for j in range(n)]
#
#     elif n != 0 and m != 0 and value is None:
#         return [[0 for i in range(m)]for j in range(n)]
#
#     elif m != 0 and n != 0 and value is not None:
#         return [[value for i in range(m)]for j in range(n)]
from idlelib.runscript import indent_message

# 2
# def count_args(*args):
#     return len(args)


# 3
# def sq_sum(*args):
#     return sum([num ** 2 for num in args])


# 4
# def mean(*args):
#     x = [i for i in args if type(i) is float or type(i) is int]
#     if len(x) == 0:
#         return 0.0
#     return sum(x) / len(x)


# 5
# def greet(name,*args):
#     if not len(args):
#         return f'Hello, {name}!'
#     return f'Hello, {name} and {" and ".join(args)}!'


# 6
# def print_products(*args):
#     products = [i for i in args if type(i) is str and i != '']
#     if len(products) == 0:
#         print("Нет продуктов")
#     for i in products:
#         print(str(products.index(i)+1) + ') ' + i)


# #7
# def info_kwargs(**kwargs):
#     s = []
#     for key, value in kwargs.items():
#         s.append(f"{key}: {value}")


# 8
# def sr_arif(a):
#         return sum(a)/len(a)
#
# numbers = [(10, 10, 10), (30, 45, 56), (81, 39), (1, 2, 3),
#            (12,), (-2, -4, 100), (1, 2, 99), (89, 9, 34), (10, 20, 30, -2),
#            (50, 40, 50), (34, 78, 65), (-5, 90, -1, -5), (1, 2, 3, 4, 5, 6),
#            (-9, 8, 4), (90, 1, -45, -21)]
#
# print(min(numbers,key=sr_arif))
# print(max(numbers,key=sr_arif))


# 9
# def s(point):
#     x,y = point
#     return (x ** 2 + y ** 2) ** 0.5
#
# points = [(-1, 1), (5, 6), (12, 0), (4, 3), (0, 1),
#           (-3, 2), (0, 0), (-1, 3), (2, 0),
#           (3, 0), (-9, 1), (3, 6), (8, 8)]
#
# points = sorted(points,key=s)
#
#
# print(points)


# 10
# def s_tuple(tup):
#     return min(tup) + max(tup)
#
# numbers = [(10, 10, 10), (30, 45, 56), (81, 80, 39),
#            (1, 2, 3), (12, 45, 67), (-2, -4, 100), (1, 2, 99),
#             (89, 90, 34), (10, 20, 30), (50, 40, 50),
#            (34, 78, 65), (-5, 90, -1)]
#
# numbers = sorted(numbers, key=s_tuple)
#
# print(numbers)


# 11
# athletes = [('Дима', 10, 130, 35), ('Тимур', 11, 135, 39),
#             ('Руслан', 9, 140, 33), ('Рустам', 10, 128, 30),
#             ('Амир', 16, 170, 70), ('Рома', 16, 188, 100),
#             ('Матвей', 17, 168, 68), ('Петя', 15, 190, 90)]
#
# def sorts(el):
#     return el[num -1]
# num = int(input())
# for i in sorted(athletes, key=sorts):
#     for j in i:
#         print(j, end=' ')
#     print()


# 12
# import math
# integer = int(input())
# d = {'квадрат': integer ** 2,
#      'куб': integer ** 3,
#      'корень': integer ** 0.5,
#      'модуль': abs(integer),
#      'синус': math.sin(integer)}
#
# print(d[input()])


# 12.1
# import math
# def func(n):
#     def func2(x):
#         return x ** n
#     return func2
#
# x = int(input())
# d = {'квадрат': func(2), 'куб': func(3), 'корень': func(0.5), 'модуль': abs, 'синус': math.sin}
# print(d[input()](x))


# 13
# def sum_of_digits(num):
#     return sum(int(digit) for digit in num)
#
# a = input().split()
#
# a_sorted = sorted(a, key=sum_of_digits)
#
# def sort_key(num):
#     return (sum_of_digits(num), int(num))
#
# a_sorted = sorted(a_sorted, key=sort_key)
#
#
# print(*a_sorted)


# 14
# def map(function, items):
#     result = []
#     for item in items:
#         result.append(function(item))
#     return result
#
# def _round(num):
#     return round(num, 2)
# numbers = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344,
#            32.12013, 23.22222, 90.09873,
#            45.45, 314.1528, 2.71828, 1.41546]
# res = map(_round, numbers)
#
# print(*res,sep='\n')


# 15
# def map(function, items):
#     result = []
#     for item in items:
#         result.append(function(item))
#     return result
#
#
# def filter(function, items):
#     result = []
#     for item in items:
#         if function(item):
#             result.append(item)
#     return result
#
#
# def predicate(num):
#     return (100 <= num <= 999) and (num % 5 == 2)
#
#
# def cube(num):
#     return num ** 3
#
#
# numbers = [1014, 1321, 675, 1215, 56, 1386, 1385,
#            431, 1058, 486, 1434, 696, 1016, 1084,
#            424, 1189, 475, 95, 1434, 1462, 815, 776,
#            657, 1225, 912, 537, 1478, 1176, 544, 488,
#            668, 944, 207, 266, 1309, 1027, 257, 1374,
#            1289, 1155, 230, 866, 708, 144, 1434, 1163,
#            345, 394, 560, 338, 232, 182, 1438, 1127, 928,
#            1309, 98, 530, 1013, 898, 669, 105, 130, 1363,
#            947, 72, 1278, 166, 904, 349, 831, 1207, 1496,
#            370, 725, 926, 175, 959, 1282, 336, 1268, 351,
#            1439, 186, 273, 1008, 231, 138, 142, 433, 456,
#            1268, 1018, 1274, 387, 120, 340, 963, 832, 1127]
# res = map(cube, filter(predicate, numbers))
# print(*res, sep='\n')


# 16.1
# def map(function, items):
#     result = []
#     for item in items:
#         result.append(function(item))
#     return result
#
#
# def squares(item):
#     return item ** 2
#
#
# numbers = [97, 42, 9, 32, 3, 45, 31, 77, -1, 11, -2, 75, 5, 51,
#            34, 28, 46, 1, -8, 84, 16, 51, 90, 56, 65, 90, 23, 35,
#            11, -10, 70, 90, 90, 12, 96, 58, -8, -4, 91, 76, 94, 60,
#            72, 43, 4, -6, -5, 51, 58, 60, 30, 38, 67, 62, 36, 72, 34,
#            82, 62, -1, 60, 82, 87, 81, -7, 57, 26, 36, 17, 43, 80, 40,
#            75, 94, 91, 64, 38, 72, 29, 84, 38, 35, 7, 54, 31, 95, 78, 27,
#            82, 1, 64, 94, 31, 29, -8, 98, 24, 61, 7, 73]
# res = sum(map(squares, numbers))
# print(res)


# 16.2
# def reduce(operation, items, initial_value):
#     acc = initial_value
#     for item in items:
#         acc = operation(acc, item)
#     return acc
#
# def sum_of_squares(s, item):
#     return s + item ** 2
#
# numbers = [97, 42, 9, 32, 3, 45, 31, 77, -1, 11, -2, 75, 5, 51,
#            34, 28, 46, 1, -8, 84, 16, 51, 90, 56, 65, 90, 23, 35,
#            11, -10, 70, 90, 90, 12, 96, 58, -8, -4, 91, 76, 94, 60,
#            72, 43, 4, -6, -5, 51, 58, 60, 30, 38, 67, 62, 36, 72, 34,
#            82, 62, -1, 60, 82, 87, 81, -7, 57, 26, 36, 17, 43, 80, 40,
#            75, 94, 91, 64, 38, 72, 29, 84, 38, 35, 7, 54, 31, 95, 78, 27,
#            82, 1, 64, 94, 31, 29, -8, 98, 24, 61, 7, 73]
#
# print(reduce(sum_of_squares, numbers, 0))


# 17
# def map(function, items):
#     result = []
#     for item in items:
#         result.append(function(item))
#     return result
#
#
# def filter(function, items):
#     result = []
#     for item in items:
#         if function(item):
#             result.append(item)
#     return result
#
# def pred(num):
#     return  len(str(abs(num))) == 2 and (num % 7 == 0)
#
#
# def square(num):
#     return num * num
#
#
# numbers = [77, 293, 28, 242, 213, 285, 71, 286,
#            144, 276, 61, 298, 280, 214, 156, 227,
#            228, 51, -4, 202, 58, 99, 270, 219, 94,
#            253, 53, 235, 9, 158, 49, 183, 166, 205,
#            183, 266, 180, 6, 279, 200, 208, 231, 178,
#            201, 260, -35, 152, 115, 79, 284, 181, 92,
#            286, 98, 271, 259, 258, 196, -8, 43, 2, 128,
#            143, 43, 297, 229, 60, 254, -9, 5, 187, 220,
#            -8, 111, 285, 5, 263, 187, 192, -9, 268, -9,
#            23, 71, 135, 7, -161, 65, 135, 29, 148, 242,
#            33, 35, 211, 5, 161, 46, 159, 23, 169, 23,
#            172, 184, -7, 228, 129, 274, 73, 197, 272,
#            54, 278, 26, 280, 13, 171, 2, 79, -2, 183,
#            10, 236, 276, 4, 29, -10, 41, 269, 94, 279,
#            129, 39, 92, -63, 263, 219, 57, 18, 236, 291,
#            234, 10, 250, 0, 64, 172, 216, 30, 15, 229, 205, 123, -105]
# p = filter(pred, numbers)
# res = sum(map(square, p))
# print(res)


# 18
# def map(function, items):
#     result = []
#     for item in items:
#         result.append(function(item))
#     return result


# 19
from functools import reduce

# data = [['Tokyo', 35676000, 'primary'],
#         ['New York', 19354922, 'nan'],
#         ['Mexico City', 19028000, 'primary'],
#         ['Mumbai', 18978000, 'admin'],
#         ['Sao Paulo', 18845000, 'admin'],
#         ['Delhi', 15926000, 'admin'],
#         ['Shanghai', 14987000, 'admin'],
#         ['Kolkata', 14787000, 'admin'],
#         ['Los Angeles', 12815475, 'nan'],
#         ['Dhaka', 12797394, 'primary'],
#         ['Buenos Aires', 12795000, 'primary'],
#         ['Karachi', 12130000, 'admin'],
#         ['Cairo', 11893000, 'primary'],
#         ['Rio de Janeiro', 11748000, 'admin'],
#         ['Osaka', 11294000, 'admin'],
#         ['Beijing', 11106000, 'primary'],
#         ['Manila', 11100000, 'primary'],
#         ['Moscow', 10452000, 'primary'],
#         ['Istanbul', 10061000, 'admin'],
#         ['Paris', 9904000, 'primary']]
#
# a = 'Cities: ' + ', '.join(
#     sorted(list(map(lambda z: z[0], (filter(lambda y: y[1] > 10000000, (filter(lambda x: x[2] == 'primary', data))))))))
# print(a)


# 20
# func = lambda x: (x % 19 == 0) or (x % 13 == 0)


# 21
# func = lambda string: (string.lower()[0] == 'a') and (string.lower()[-1] == 'a')


# 22
# words = ['beverage', 'monday', 'abroad', 'bias', 'abuse', 'abolish', 'abuse',
#          'abuse', 'bid', 'wednesday', 'able', 'betray', 'accident', 'abduct',
#          'bigot', 'bet', 'abandon', 'besides', 'access', 'friday', 'bestow',
#          'abound', 'absent', 'beware', 'abundant', 'abnormal', 'aboard', 'about',
#          'accelerate', 'abort', 'thursday', 'tuesday', 'sunday', 'berth', 'beyond',
#          'benevolent', 'abate', 'abide', 'bicycle', 'beside', 'accept', 'berry', 'bewilder',
#          'abrupt', 'saturday', 'accessory', 'absorb']
#
# a = sorted(filter(lambda w: len(w) == 6, words))
# print(*a, sep = ' ')


#23
# numbers = [46, 61, 34, 17, 56, 26, 93, 1, 3, 82, 71, 37, 80, 27,
#            77, 94, 34, 100, 36, 81, 33, 81, 66, 83, 41, 80, 80, 93,
#            40, 34, 32, 16, 5, 16, 40, 93, 36, 65, 8, 19, 8, 75, 66,
#            21, 72, 32, 41, 59, 35, 64, 49, 78, 83, 27, 57, 53, 43, 35,
#            48, 17, 19, 40, 90, 57, 77, 56, 80, 95, 90, 27, 26, 6, 4, 23,
#            52, 39, 63, 74, 15, 66, 29, 88, 94, 37, 44, 2, 38, 36, 32, 49,
#            5, 33, 60, 94, 89, 8, 36, 94, 46, 33]
#
# res = map(lambda x: x // 2 if x % 2 == 0 else x , filter(lambda number: (number % 2 == 0) or (number % 2 == 1 and number <= 47) , numbers))
# print(*res)


#24
# data = [(19542209, 'New York'), (4887871, 'Alabama'), (1420491, 'Hawaii'), (626299, 'Vermont'),
#         (1805832, 'West Virginia'), (39865590, 'California'), (11799448, 'Ohio'), (10711908, 'Georgia'),
#         (10077331, 'Michigan'), (10439388, 'Virginia'), (7705281, 'Washington'), (7151502, 'Arizona'),
#         (7029917, 'Massachusetts'), (6910840, 'Tennessee')]
#
# res = sorted(data, key=lambda x: x[1][-1], reverse=True)
# for i in res:
#     print(i[1] + ': ' + str(i[0]))


#25
# data = ['год', 'человек', 'время', 'дело', 'жизнь', 'день',
#         'рука', 'раз', 'работа', 'слово', 'место', 'лицо',
#         'друг', 'глаз', 'вопрос', 'дом', 'сторона', 'страна',
#         'мир', 'случай', 'голова', 'ребенок', 'сила', 'конец',
#         'вид', 'система', 'часть', 'город', 'отношение', 'женщина', 'деньги']
# res = sorted(sorted(data), key=len)
# print(*res, sep = ' ')


#26
# mixed_list = ['tuesday', 'abroad', 'abuse', 'beside', 'monday', 'abate', 'accessory', 'absorb', 1384878,
#               'sunday', 'about', 454805, 'saturday', 'abort', 2121919, 2552839, 977970, 1772933, 1564063,
#               'abduct', 901271, 2680434, 'bicycle', 'accelerate', 1109147, 942908, 'berry', 433507, 'bias',
#               'bestow', 1875665, 'besides', 'bewilder', 1586517, 375290, 1503450, 2713047, 'abnormal', 2286106,
#               242192, 701049, 2866491, 'benevolent', 'bigot', 'abuse', 'abrupt', 343772, 'able', 2135748, 690280,
#               686008, 'beyond', 2415643, 'aboard', 'bet', 859105, 'accident', 2223166, 894187, 146564, 1251748,
#               2851543, 1619426, 2263113, 1618068, 'berth', 'abolish', 'beware', 2618492, 1555062, 'access',
#               'absent', 'abundant', 2950603, 'betray', 'beverage', 'abide', 'abandon', 2284251, 'wednesday',
#               2709698, 'thursday', 810387, 'friday', 2576799, 2213552, 1599022, 'accept', 'abuse', 'abound',
#               1352953, 'bid', 1805326, 1499197, 2241159, 605320, 2347441]
#
# res = max(mixed_list, key=lambda x: x if type(x) is int else 0)
# print(res)


#27
a = input().split()
res = map(lambda x:  255 - int(x), a)
print(*res)





