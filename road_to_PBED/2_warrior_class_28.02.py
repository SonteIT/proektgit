import random


class Warrior:
    name = None
    power = None
    healthpoints = None
    critical_hit_chance = 15

    def set_data_warrior(self, name, power, healthpoints):
        self.name = name
        self.power = power
        self.healthpoints = healthpoints

    def attacks(self, target):
        while self.healthpoints > 0 and target.healthpoints > 0:

            if random.randint(0, 100) <= Warrior.critical_hit_chance:
                target.healthpoints -= self.power * 2
                print(
                    f'{self.name} нанес критический удар {target.name}, и отнял у него {self.power * 2} здоровья!.'
                    f'Здоровье {target.name}: {target.healthpoints}\n')

            else:
                target.healthpoints -= self.power
                print(
                    f'{self.name} ударил {target.name}, и отнял у него {self.power} здоровья!'
                    f'Здоровье {target.name}: {target.healthpoints}\n')

            if target.healthpoints <= 0:
                break

            if random.randint(0, 100) <= Warrior.critical_hit_chance:
                self.healthpoints -= target.power * 2
                print(
                    f'{target.name} нанес критический удар {self.name}, и отнял у него {target.power * 2} здоровья!'
                    f'Здоровье {self.name}: {self.healthpoints}\n')
            else:
                self.healthpoints -= target.power
                print(
                    f'{target.name} атаковал {self.name}, отняв у врага {target.power} HP!'
                    f'Здоровье {self.name}: {self.healthpoints}\n')

        if self.healthpoints <= 0:
            return f'{target.name} победил!'
        return f'{self.name} выиграл!'


warrior1 = Warrior()
warrior2 = Warrior()
warrior1.set_data_warrior(input('Имя: '), int(input('Введите силу удара: ')), int(input('Введите кол-во здоровья: ')))
warrior2.set_data_warrior(input('Имя: '), int(input('Введите силу удара: ')), int(input('Введите кол-во здоровья: ')))
print(warrior1.attacks(warrior2))
