inp = int(input())
k = 0
s = 0
while inp != 0:
    if inp % 8 == 0:
        k += 1
        s += inp
    inp = int(input())

if k == 0:
    print('NO')
else:
    print(round(s/k, 1))

