from random import randint

limit_of_numbers_left, limit_of_numbers_right = map(int, input(
    'Введите диапазон чисел для угадывания, например "1 100": ').split())
rand_digit = randint(limit_of_numbers_left, limit_of_numbers_right)

print()

number_of_attempts = input('Введите кол-во попыток, или введите "Бесконечность",'
                           'если не хотите ограничений в попытках: ')

print()

if number_of_attempts == 'Бесконечность' or number_of_attempts == 'бесконечность':
    number_of_unlimited_attempts = 1
    digit = int(input('Введите число: '))
    while digit != rand_digit:
        number_of_unlimited_attempts += 1
        if digit > rand_digit:
            print('Меньше!')
            print()
        elif digit < rand_digit:
            print('Больше!')
            print()
        digit = int(input('Введите число: '))
    else:
        print(f'Число {rand_digit} угадано за {number_of_unlimited_attempts} попыток!')


else:
    for attempt in range(int(number_of_attempts)):
        digit = int(input('Введите число: '))
        print()
        if digit != rand_digit:
            if digit > rand_digit:
                print('Меньше!')
                print()
            elif digit < rand_digit:
                print('Больше!')
                print()
        else:
            print(f'Число {rand_digit} угадано!')
            break
    else:
        print('Вы не угадали число!')
