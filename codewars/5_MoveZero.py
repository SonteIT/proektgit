def move_zeros(lst):
    res_lst = []
    count_zero = 0
    for el in lst:
        if el != 0:
            res_lst.append(el)
        else:
            count_zero += 1
    return res_lst + [0] * count_zero
print(move_zeros([1,0,2,0,3]))  #вариант работает за O(n) времени


def move_zeros(lst):
    return sorted(lst, key=lambda x: x == 0)
print(move_zeros([1,0,2,0,3]))  #вариант работает за O(n log n) времени
