# 1
# file = open(input(), 'r')
# print(*[line for line in file])
# file.close()


# 2
# file = open(input(), 'r')
# print([line for line in file][-2])
# file.close()


# 3
# from random import choice
#
# file = open('lines.txt', 'r',encoding = 'utf-8')
# a = [line.strip() for line in file]
# res = choice(a)
# print(res)
# file.close()


#4
# file = open('numbers.txt', 'r', encoding = 'utf-8')
# print(sum(map(int, file.readlines())))


#5
# file = open('nums.txt', 'r', encoding = 'utf-8')
# a = [line.strip() for line in file]
# b = sum([int(i) for i in a if i != ''])
# print(b)


#6
# file = open('prices.txt','r', encoding = 'utf-8')
# a = file.read().split()
# d = {}
# for i in range(0,len(a),3):
#     name = a[i]
#     qty = int(a[i + 1])
#     price = int(a[i + 2])
#     total = qty * price
#     if name in d:
#         d[name] += total
#     else:
#         d[name] = total
# print(sum(d.values()))
# file.close()


# file = open('prices.txt', 'r', encoding='utf-8')
# s = 0
# for line in file:
#     tovar, count, price = line.split()
#
#     s += int(count) * int(price)
# print(s)
# file.close()


#7
# with open('input.txt', encoding='utf-8') as file:
#     print('Repeat after me:', file.readline().strip())
#     for line in file:
#         print(line.strip() + '!')


#8
# with open('text.txt', 'r', encoding='utf-8') as file:
#     a = file.read()
#     print(a[::-1])


#9
# with open('data.txt', 'r', encoding='utf-8') as file:
#     res = []
#     for line in reversed(file.readlines()):
#         res.append(line)
#     print(*res,sep = '')


#10
# with open('lines.txt', 'r', encoding='utf-8') as file:
#     max_len = len(max(file.readlines(), key=len))
#     file.seek(0)
#     res = [i for i in file.readlines() if len(i) == max_len]
#     print(*res, sep='')


#11
# with open('numbers.txt','r', encoding='utf-8') as file:
#     for line in file.readlines():
#          nums_in_l_s = line.split()
#          nums_in_l = map(int, nums_in_l_s)
#          print(sum(nums_in_l))


#12
# with open('nums.txt', 'r', encoding='utf-8') as file:
#     dig = ''.join([' ' if i.isalpha() else i for i in file.read()]).split()
#     print(sum(map(int, dig)))


#13
# with open('file.txt', 'r', encoding='utf-8') as file:
#     count_lines = len(file.readlines())
#     file.seek(0)
#     count_words = len([i for i in file.read().split()])
#     file.seek(0)
#     count_letters = 0
#     for i in file.read():
#         if i.isalpha():
#             count_letters += 1
#
#
#     print(f'Input file contains:\n{count_letters} letters\n{count_words} words\n{count_lines} lines')


#14
# from random import choice
# with open('first_names.txt', 'r', encoding='utf-8') as names, open('last_names.txt', 'r', encoding='utf-8') as second_names:
#     first_name = names.read().split()
#     second_name = second_names.read().split()
#     print(choice(first_name),choice(second_name))
#     print(choice(first_name), choice(second_name))
#     print(choice(first_name), choice(second_name))


#15
# with open('population.txt', 'r', encoding='utf-8') as file:
#     c = file.read().split('\n')
#     d = {}
#     for i in c:
#         if '\t' not in i:
#             continue
#         co, popul = i.split('\t')
#         d[co] = int(popul)
#     res = filter(lambda item: item[0][0] == 'G' and item[1] > 500000, d.items())
#     for i,j in res:
#         print(i)












