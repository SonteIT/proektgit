def highest_rank(arr):
    d = {}
    for el in arr:
        d[el] = d.get(el, 0) + 1
    lst = []
    m = max(d.values())
    for key, value in d.items():
        if value == m:
            lst.append(key)
    return max(lst)

print(highest_rank([12, 10, 8, 8, 3, 3, 3, 3, 2, 4, 10, 12, 10]))

