import random
import time


class Hero:
    def __init__(self, name: str, power: int, hp: int, critical_hit_chance=100):
        self.name = name
        self.power = power
        self.hp = hp
        self.critical_hit_chance = critical_hit_chance
        self.max_hp = self.hp
        self.debuffs = {'bleeding': 0, 'poisoning' : 0}


    @property
    def power(self):
        return self.__power

    @power.setter
    def power(self, value):
        if value > 500:
            self.__power = 500
            print('В этом мире запрещено устанавливать такое большое значение! Боги назначили максимальное значение силы:  500.')
        elif value < 0:
            self.__power = 0
            print('В этой вселенной с такими показателями не выжить! Боги назначили минимальное значение силы: 1' )
        else:
            self.__power = value

    @property
    def hp(self):
        return self.__hp

    @hp.setter
    def hp(self, value):
        if value > 1000:
            self.__hp = 1000
            print('В этом мире запрещено устанавливать такое большое значение! Боги назначили максимальное значение здоровья:  1000.')
        elif value < 0:
            self.__hp = 0
            print('В этой вселенной с такими показателями не выжить! Боги назначили минимальное значение здоровья: 1')
        else:
            self.__hp = value

    def take_damage(self, damage):
        self.hp -= damage

    def attack(self, target, damage=None):
        if damage is None:
            damage = self.power
        target.take_damage(damage)
        print(f'{self.name} атаковал {target.name}, нанеся {round(damage, 0)} урона. У {target.name} осталось {round(target.hp,0)} HP')


class Warrior(Hero):
    def attack(self, target, damage=None):
        current_damage = self.power
        flag = False
        if random.randint(0, 100) <= self.critical_hit_chance:
            flag = True
            current_damage *= 2
        if flag:
            super().attack(target, damage=current_damage)
        else:
            super().attack(target, damage=current_damage)
        if random.randint(0, 100) <= 15:
            target.debuffs['bleeding'] += 3

    def take_damage(self, damage):
        if random.randint(1, 100) <= 20:
            damage = 0
            print(f'{self.name} нанес удар по щиту!')
        super().take_damage(damage)



class Archer(Hero):
    def __init__(self, name, power, hp, arrows=10):
        super().__init__(name, power, hp)
        self.arrows = arrows

    def attack(self, target, damage=None):
        damage = self.power * 1.2
        if self.arrows > 0:
            self.arrows -= 1
            super().attack(target, damage=damage)
            print(f'у {self.name} осталось {self.arrows} стрел')
        else:
            print('Нету стрел!')
            super().attack(target, damage=self.power)


class Wizard(Hero):
    def __init__(self, name, power, hp):
        super().__init__(name, power, hp)

    def random_buff(self):
        list_of_buffs = ['critical', 'healing']
        return random.choice(list_of_buffs)

    def attack(self, target, damage=None):
        damage = self.power
        lst = self.random_buff()
        if random.randint(1, 100) <= 15:
            if lst == 'critical':
                damage *= 2
                print('Маг выпил секретное зелье и нанес критический удар!')
            elif lst == 'healing':
                print(f'Маг использовал запретный прием, восстановив часть здоровья! Текущее здоровье: {self.hp}')
                heal = self.hp * 0.2
                self.hp += heal
        super().attack(target, damage=damage)


dict_of_heroes = {'Лучник': Archer, 'Мечник': Warrior, 'Маг': Wizard}
inp1 = input('Введите класс первого участника Смертельной Битвы(Мечник, Лучник или Маг): ').capitalize()
print()
class_1 = dict_of_heroes.get(inp1)
inp2 = input('Введите класс второго участника Смертельной Битвы(Мечник, Лучник или Маг): ').capitalize()
print()
class_2 = dict_of_heroes.get(inp2)

name1 = input('Введите имя первого бойца: ')
print()
pow1 = int(input('Введите силу первого бойца: '))
print()
hp1 = int(input('Введите здоровье первого бойца: '))
print()
first_participant = class_1(name1, pow1, hp1)

name2 = input('Введите имя второго участника: ')
print()
pow2 = int(input('Введите силу второго участника: '))
print()
hp2 = int(input('Введите здоровье второго участника: '))
print()

second_participant = class_2(name2, pow2, hp2)

while True:
    first_participant.attack(second_participant)
    if second_participant.debuffs['bleeding'] > 0:
        while second_participant.debuffs['bleeding'] > 0:
            if second_participant.hp <= 0:
                break
            print("-" * 30)
            second_participant.take_damage(second_participant.max_hp * 0.05)
            time.sleep(1)
            print(f'{second_participant.name} кровоточит от удара {first_participant.name} и теряет'
                  f' {round(second_participant.max_hp * 0.05, 0)} HP! Осталось {round(second_participant.hp, 0)} HP!')
            second_participant.debuffs['bleeding'] -= 1


    print("-" * 30)
    time.sleep(0.7)
    if second_participant.hp <= 0:
        if first_participant.hp - second_participant.hp <= 150:
            print(f'{first_participant.name} зубами вырывает победу у {second_participant.name}!')
        elif first_participant.hp - second_participant.hp  >= 400:
            print(f'{first_participant.name} с легкостью побеждает {second_participant.name}!')
        else:
            print(f'{first_participant.name} побеждает {second_participant.name}!')
        print("-" * 30)
        break


    second_participant.attack(first_participant)
    if first_participant.debuffs['bleeding'] > 0:
        while first_participant.debuffs['bleeding'] > 0:
            if first_participant.hp <= 0:
                break
            print("-" * 30)
            first_participant.take_damage(first_participant.max_hp * 0.05)
            time.sleep(2)
            print(f'{first_participant.name} кровоточит от удара {second_participant.name} и теряет'
                  f' {round(first_participant.max_hp * 0.05, 0)} HP! Осталось {round(first_participant.hp, 0)} HP!')
            first_participant.debuffs['bleeding'] -= 1


    print("-" * 30)
    time.sleep(0.7)
    if first_participant.hp <= 0:
        if second_participant.hp - first_participant.hp <= 150:
            print(f'{second_participant.name} в тяжелой схватке выйгрывает {first_participant.name}!')
        elif second_participant.hp - first_participant.hp  >= 400:
            print(f'{second_participant.name} без проблем одолел {first_participant.name}!')
        else:
            print(f'{second_participant.name} выйгрывает {first_participant.name}!')
        print("-" * 30)
        break
