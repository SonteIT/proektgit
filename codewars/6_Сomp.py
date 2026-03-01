def comp(array1, array2):
    if array1 is None or array2 is None: return False
    B = [x * x for x in array1]
    bd = {}
    ad = {}
    for i in B:
        bd[i] = bd.get(i, 0) + 1
    for i in array2:
        ad[i] = ad.get(i, 0) + 1
    return bd == ad
print(comp([121, 144, 19, 161, 19, 144, 19, 11],[121, 14641, 20736, 361, 25921, 361, 20736, 361]))

