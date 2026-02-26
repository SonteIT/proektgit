def convert_to_shalkerbox(item, quantity):
    stacks = quantity // 64
    objects = quantity % 64
    shalkers = stacks // 27
    ost_shalkers = stacks % 27
    if not stacks:
        return {'Кол-во предметов': objects,}

    if not shalkers:
        return {
            'Кол-во стаков': stacks,
            'Кол-во предметов': objects
        }

    return {
        'Кол-во шалкеров': shalkers,
        'Кол-во предметов': ost_shalkers,
    }

res = {}
for _ in range(int(input('Введите кол-во предметов для постройки: '))):
    item, quantity = input('Введите название предмета и его кол-во через пробел: ').split()
    res[item] = convert_to_shalkerbox(item, int(quantity))


for i, j in res.items():
    print(f'------{i.upper()}------')
    for k, v in j.items():
        print(f'{k}: {v}')




