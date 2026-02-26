# 1
# print(len(set(input())))


# 2
# string = input()
# if len(string) == len(set(string)):
#     print("YES")
# else:
#     print("NO")


# 3
# set_digits = {'1','2','3','4','5','6','7','8','9','0'}
# set_input1 = input()
# set_input2 = input()
# if set(set_input1 + set_input2) == set_digits:
#     print('YES')
# else:
#     print('NO')


# 4
# set_input1 = input()
# set_input2 = input()
# if set(set_input1) == set(set_input2):
#     print('YES')
# else:
#     print('NO')


# 5
# n = int(input())
# name_set = set()
# for i in range(n):
#     print(len(set(input().lower())))


# 6
# n = int(input())
# s = []
# for i in range(n):
#     s.append(input().lower())
# l = ''.join(s)
# print(len(set(l)))


# 7
# string = input().lower().split()
# result = []
# for s in string:
#     for ch in '.,;:-?!':
#         s = s.replace(ch, "")
#     result.append(s)
# print(len(set(result)))


# 8
# my_set = set()
# m = [int(i) for i in input().split()]
# for i in m:
#     if i not in my_set:
#         my_set.add(i)
#         print('NO')
#     else:
#         print('YES')


# 9
# first_set = set([int(i) for i in input().split()])
# second_set = set([int(i) for i in input().split()])
# print(len(first_set & second_set))


# 10
# first_set = set(map(int,input().split()))
# second_set = set(map(int,input().split()))
# print(*sorted(first_set & second_set))


# 11
# first_set = set(map(int,input().split()))
# second_set = set(map(int,input().split()))
# print(*sorted(first_set - second_set))


# 12
# n = int(input())
# my_set = set(input())
# for i in range(n-1):
#     a = set(input())
#     my_set &= a
# print(*sorted(my_set))


# 13
# d1 = set(input())
# d2 = set(input())
# if d1.isdisjoint(d2):
#     print("NO")
# else:
#     print("YES")


# 14
# n1 = set(input())
# n2 = set(input())
# if n2.issubset(n1):
#     print('YES')
# else:
#     print('NO')


# 15
# n1 = set(map(int, input().split()))
# n2 = set(map(int, input().split()))
# n3 = set(map(int, input().split()))
# obsh_oc = n1.intersection(n2)
# print(*sorted(obsh_oc.difference(n3), reverse=True))


#16
# b = {0,1,2,3,4,5,6,7,8,9,10}
# n1 = set(map(int, input().split()))
# n2 = set(map(int, input().split()))
# n3 = set(map(int, input().split()))
# b -= (n1 | n2 | n3)
# print(*sorted(b))


# 17
# n1 = set(map(int, input().split()))
# n2 = set(map(int, input().split()))
# n3 = set(map(int, input().split()))
#
#
# result = n3 - (n1 | n2)
#
#
# print(*sorted(result,reverse=True))


#18
# items = [10, '30', 30, 10, '56', 34, '12', 90, 89, 34, 45, '67', 12, 10, 90, 23, '45', 56, '56', 1, 5, '6', 5]
# my_set = {int(i) for i in items}
# print(*sorted(my_set))


#19
# words = ['Plum', 'Grapefruit', 'apple', 'orange', 'pomegranate',
#          'Cranberry', 'lime', 'Lemon', 'grapes', 'persimmon',
#          'tangerine', 'Watermelon', 'currant', 'Almond']
# res_set = {i[0].lower() for i in words}
# print(*sorted(res_set))


#19
# sentence = '''My very photogenic mother died in a freak accident (picnic, lightning)
# when I was three, and, save for a pocket of warmth in the darkest past, nothing of her
# subsists within the hollows and dells of memory, over which, if you can still stand
# my style (I am writing under observation), the sun of my infancy had set: surely,
# you all know those redolent remnants of day suspended, with the midges, about some
# hedge in bloom or suddenly entered and traversed by the rambler, at the bottom of a hill,
# in the summer dusk; a furry warmth, golden midges.'''
#
# res_set = {word.strip('.,;:!?()[]{}"\'').lower() for word in sentence.split()}
# print(*sorted(res_set))


#20
# sentence = '''My very photogenic mother died in a freak accident (picnic, lightning)
# when I was three, and, save for a pocket of warmth in the darkest past, nothing of her
# subsists within the hollows and dells of memory, over which, if you can still stand my
# style (I am writing under observation), the sun of my infancy had set: surely, you all
# know those redolent remnants of day suspended, with the midges, about some hedge in bloom
# or suddenly entered and traversed by the rambler, at the bottom of a hill, in the summer dusk;
# a furry warmth, golden midges.'''
#
# res_sentence = {word.strip('.,;:!?()[]{}"\'').lower() for word in sentence.split() if len(word.strip('.,;:!?()[]{}"\'')) < 4}
# print(*sorted(res_sentence))


#21
# files = ['python.png', 'qwerty.py', 'stepik.png', 'beegeek.org', 'windows.pnp',
#          'pen.txt', 'phone.py', 'book.txT', 'board.pNg', 'keyBoard.jpg',
#          'Python.PNg', 'apple.jpeg', 'png.png', 'input.tXt', 'split.pop',
#          'solution.Py', 'stepik.org', 'kotlin.ko', 'github.git']
# res_set = {file.lower() for file in files if file.lower().endswith('.png')}
# print(*sorted(res_set))

#kr1
# n = int(input())
# m = int(input())
# k = int(input())
# p = int(input())
# print(n - m  - k + p)


#kr2
# s = (input().split())
# print(len(s) - len(set(s)))


#kr3
# s = {input() for _ in range(int(input()))}
# if input() not in s:
#     print('OK')
# else:
#     print('REPEAT')


#kr4
# m = int(input())
# n = int(input())
# m_b = {input() for _ in range(m)}
# n_b = [input() for _ in range(n)]
# for i in n_b:
#     if i in m_b:
#         print('YES')
#     else:
#         print('NO')


#kr5
# s1 = set(map(int, input().split()))
# s2 = set(map(int, input().split()))
# if len(s1 & s2)>0:
#     print(*sorted(s1 & s2,reverse=True, key=int))
# elif len(s1 & s2)>0:
#     print(*sorted(s2 & s1,reverse=True, key=int))
# else:
#     print('BAD DAY')


#kr6
# s1 = set(map(int, input().split()))
# s2 = set(map(int, input().split()))
# if s1 == s2:
#     print("YES")
# else:
#     print("NO")










