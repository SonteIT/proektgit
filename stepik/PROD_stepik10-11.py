# 1
# d = {
#     0: "zero",
#     1: "one",
#     2: "two",
#     3: "three",
#     4: "four",
#     5: "five",
#     6: "six",
#     7: "seven",
#     8: "eight",
#     9: "nine"
# }
# res = ''
# n = input()
# for i in n:
#     res += d[int(i)] + ' '
# print(res)
import urllib


# 2
# d = { "CS101": "CS101: 3004, Хайнс, 8:00", "CS102": "CS102: 4501, Альварадо, 9:00", "CS103": "CS103: 6755, Рич, 10:00", "NT110": "NT110: 1244, Берк, 11:00", "CM241": "CM241: 1411, Ли, 13:00" }
# print(d[input()])


# 3
# d = {".": '1', ",": '11', "?": '111', "!": '1111', ":": '11111',
#      "A": '2', "B": '22', "C": '222',
#      "D": '3', "E": '33', "F": '333',
#      "G": '4', "H": '44', "I": '444',
#      "J": '5', "K": '55', "L": '555',
#      "M": '6', "N": '66', "O": '666',
#      "P": '7', "Q": '77', "R": '777', "S": '7777',
#      "T": '8', "U": '88', "V": '888',
#      "W": '9', "X": '99', "Y": '999', "Z": '9999',
#      " ": '0'
#      }
# n = input().upper()
# res = ''
# for i in n:
#     if d.get(i) != None:
#         res += d[i]
# print(res)


# 4
# letters = [c for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789']
# morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....',
#          '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.',
#          '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-',
#          '-.--', '--..', '-----', '.----', '..---', '...--', '....-',
#          '.....', '-....', '--...', '---..', '----.']
# morse_dict = dict(zip(letters, morse))
# n = input().upper()
# res = ''
# for i in n:
#     if i in morse_dict:
#         res += morse_dict[i] + ' '
# print(res)


# 5
# s = input().lower()
# res = {}
# p = ''
# for i in s:
#     if i not in '.,!?:;-':
#         p += i
# p = p.split()
# for i in p:
#     res[i] = res.get(i, 0) + 1
# m_v = min(res.values())
# k = [k for k, v in res.items() if v == m_v]
# print(min(k))


# 6
# s = input().split()
# result = {}
# output = []
#
# for word in s:
#     if word not in result:
#         result[word] = 1
#         output.append(word)
#     else:
#         output.append(f"{word}_{result[word]}")
#         result[word] += 1
#
# print(' '.join(output))


# 7
# d_words = {}
# for i in range(int(input())):
#     key, value = map(str, input().split(': '))
#     d_words[key.lower()] = value
# for i in range(int(input())):
#     word = input().lower()
#     print(d_words.get(word, 'Не найдено'))


# 8
# word_1 = input()
# word_2 = input()
# d_1 = {}
# d_2 = {}
#
# for i in word_1:
#     d_1[i] = d_1.get(i, 0) + 1
# for i in word_2:
#     d_2[i] = d_2.get(i, 0) + 1
#
# if d_1 == d_2:
#     print('YES')
# else:
#     print('NO')


# 9
# def clean(s):
#     return ''.join(ch for ch in s.lower() if ch.isalpha())
#
# p1 = clean(input())
# p2 = clean(input())
#
# print('YES' if sorted(p1) == sorted(p2) else 'NO')


# 10
# d = {}
# for i in range(int(input())):
#     word1, word2 = input().split()
#     d[word1] = word2
#     d[word2] = word1
# print(d[input()])


# 11
# d = {}
# for i in range(int(input())):
#     countries = input().split()
#     d[countries[0]] = countries[1:]
# for i in range(int(input())):
#     city = input()
#     for k, v in d.items():
#         if city in v:
#             print(k)


# 12
# d = {}
# for i in range(int(input())):
#     phone = input().lower().split()
#     if phone[1] in d:
#         d[phone[1]].append(phone[0])
#     else:
#         d[phone[1]] = [phone[0]]
# for i in range(int(input())):
#     name = input().lower()
#     print(' '.join(d[name]) if name in d else 'абонент не найден')


# 13
# d1 = {}
# d2 = {}
# word = input()
# for i in word:
#     d1[i] = d1.get(i, 0) + 1
# for i in range(int(input())):
#     char, count_char = map(str, input().split(': '))
#     d2[char] = int(count_char)
# for i in d1:
#     for j in d2:
#         if d1[i] == d2[j]:
#             word = word.replace(i, j)
# print(word)


# kr1
# dnk_rnk = {'A': 'U', 'C': 'G', 'G': 'C', 'T': 'A'}
# cep = input()
# res = ''
# for c in cep:
#     res += dnk_rnk[c]
# print(res)


#kr2
# text = input()
# words = text.split()
# counter = {}
# res = []
# for word in words:
#     count = counter.get(word, 0) + 1
#     res.append(str(count))
#     counter[word] = count
# print(' '.join(res))


# kr3
# word = input()
# d = {
#     1: "AEILNORSTU",
#     2: "DG",
#     3: "BCMP",
#     4: "FHVWY",
#     5: "K",
#     8: "JX",
#     10: "QZ"
# }
#
# result = 0
#
# for i in word:
#     for k,v in d.items():
#         if i in v:
#             result += k
# print(result)


#kr4
# def build_query_string(d):
#     s = []
#     for k, v in d.items():
#          s.append(f'{k}={v}')
#     s = sorted(s)
#     return '&'.join(s)
# print(build_query_string({'sport': 'hockey', 'game': 2, 'time': 17}))


#kr5
# d = {}
# mapping = {'read': 'R', 'write': 'W', 'execute': 'X'}
# for i in range(int(input())):
#     n = input().split()
#     d[n[0]] = n[1:]
# for i in range(int(input())):
#     z,f = input().split()
#     op = mapping.get(z)
#     if op in d.get(f,[]):
#         print('OK')
#     else:
#         print('Access denied')


n = input()
for i in range(1,len(n)):
    print(n.index(n[i]))



