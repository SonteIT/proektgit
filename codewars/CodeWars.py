####25.01.2026
# import copy
# def duck_duck_goose(players, goose):
#     p = copy.deepcopy(players)
#     while len(players) < goose:
#         players += p
#     return players[goose-1]
# print(duck_duck_goose(['a', 'b', 'c', 'd'], 4))


# def smash(words):
#     return ' '.join(words)


# def grow(arr):
#     a = 1
#     for i in arr:
#         a *= i
#     return a


#26.01.26
# def even_or_odd(number):
#    if number % 2 == 0:
#        return 'Even'
#    return 'Odd'


# def remove(s):
#     if s.endswith('!'):
#         return s[:-1]
#     return s

# def neutralise(s1, s2):
#     res = ''
#     for i,j in zip(s1, s2):
#         if i == j:
#             res += i
#         else:
#             res += '0'
#     return res
# print(neutralise('+-+', '+--'))


#27.01.2026
# def invert(lst):
#     return [-i for i in lst ]
# print(invert([0, -2, -3]))


# def distinct(seq):
#     return list(dict.fromkeys(seq))


# def count_words(string: str):
#     s = string.lower().split()
#     res = {}
#     for i in s:
#         res[i] = res.get(i, 0) + 1
#     return res
#
# print(count_words(input()))


#28.01.2026
# def mouth_size(animal):
#     if animal.lower() == 'alligator':
#         return 'small'
#     return 'wide'


# def get_count(sentence):
#     count = 0
#     for i in sentence:
#         if i in 'aeiou':
#             count += 1
#     return count
#
# print(get_count('hello world'))


#02.02.2026
# def count_sheeps(sheep):
#   return sheep.count(True)


#03.02.2026
# def unique_in_order(sequence):
#     res = []
#     for i in range(1,len(sequence)):
#         if sequence[i] != sequence[i-1]:
#             res.append(sequence[i-1])
#     if sequence:
#         res.append(sequence[-1])
#     return res
# print(unique_in_order(['A']))


# def find_it(seq):
#     res = {}
#     for i in seq:
#         res[i] = res.get(i, 0) + 1
#     for i,j in res.items():
#         if j % 2 != 0:
#             return i
# print(find_it([1,1,2,3,3,3,3,3,3,3]))


#17.02.2026
# def duplicate_count(text):
#     res = 0
#     slovar = {}
#     for i in text.lower():
#         slovar[i] = slovar.get(i, 0) + 1
#     for i, j in slovar.items():
#         if j > 1:
#             res += 1
#     return res
# print(duplicate_count("HelloO"))


#19.02.2026
# def solution(number):
#     s = sum(set(i for i in range(number) if i % 3 == 0 or i % 5 == 0))
#     if s > 0:
#         return s
#     return 0
# print(solution(int(input())))


#24.02.2026
def likes(names: list):
    if len(names) == 1:
        return f'{names[0]} likes this'
    if len(names) == 2:
        return f'{names[0]} and {names[1]} like this'
    if len(names) == 3:
        return f'{names[0]}, {names[1]} and {names[2]} like this'
    if len(names) >= 4:
        return f'{names[0]}, {names[1]} and {len(names)-2} others like this'
    return 'no one likes this'
print(likes([]))











