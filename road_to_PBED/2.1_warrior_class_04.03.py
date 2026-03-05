import random


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


class Warrior(Hero):
    def attack(self, target, damage=None):
        current_damage = self.power
        if random.randint(0, 100) <= self.critical_hit_chance:
            current_damage *= 2
        super().attack(target, damage=current_damage)

    def take_damage(self, damage):
        if random.randint(1, 100) <= 20:
            damage = 0
        super().take_damage(damage)


class Archer(Hero):
    def __init__(self, name, power, hp, arrows=10):
        super().__init__(name, power, hp)
        self.arrows = arrows

    def attack(self, target, damage=None):
        damage = self.power * 1.1
        if self.arrows > 0:
            self.arrows -= 1
            super().attack(target, damage=damage)
        else:
            print('Нету стрел!')


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
            elif lst == 'healing':
                heal = self.hp * 0.2
                self.hp += heal
        super().attack(target, damage=damage)
