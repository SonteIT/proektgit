import random
import time

class Hero:
    def __init__(self, name: str, power: int, hp: int, critical_hit_chance=40):
        self.name = name
        self.power = power
        self.hp = hp
        self.critical_hit_chance = critical_hit_chance

    def take_damage(self, damage):
        self.hp -= damage

    def attack(self, target, damage=None):
        if damage is None:
            damage = self.power
        target.take_damage(damage)
        print(f'{self.name} атаковал {target.name}, нанеся {damage} урона. У {target.name} осталось {target.hp} HP')


class Warrior(Hero):
    def attack(self, target, damage=None):
        current_damage = self.power
        flag = False
        if random.randint(0, 100) <= self.critical_hit_chance:
            flag = True
            current_damage *= 2
        if flag:
            super().attack(target, damage=current_damage)
            print('Критический удар!')
        else:
            super().attack(target, damage=current_damage)

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
                print('Нанесен магический крит!')
            elif lst == 'healing':
                print('Маг восстанавливает здоровье!')
                heal = self.hp * 0.2
                self.hp += heal
        super().attack(target, damage=damage)


dict_of_heroes = {'Лучник': Archer, 'Мечник': Warrior, 'Маг': Wizard}
inp1 = input('Введите класс первого участника(Мечник, Лучник или Маг): ').capitalize()
print()
class_1 = dict_of_heroes.get(inp1)
inp2 = input('Введите класс второго участника(Мечник, Лучник или Маг): ').capitalize()
print()
class_2 = dict_of_heroes.get(inp2)

name1 = input('Введите имя первого участника: ')
print()
pow1 = int(input('Введите силу первого участника: '))
print()
hp1 = int(input('Введите здоровье первого участника: '))
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
    print("-" * 30)
    time.sleep(0.7)
    if second_participant.hp <= 0:
        print(f'{first_participant.name} победил!')
        print("-" * 30)
        break
    second_participant.attack(first_participant)
    print("-" * 30)
    time.sleep(0.7)
    if first_participant.hp <= 0:
        print(f'{second_participant.name} победил!')
        print("-" * 30)
        break
