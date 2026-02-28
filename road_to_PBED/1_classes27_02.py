class Robot:  # class - ключевое слово. robot - название класса
    name = None  # Создание атрибута. Можно дать любое начально значение.
    lasers_from_eyes = False
    ability_to_walk = True
    best_before_date = '10 years'

    def data(self, name, lasers_from_eyes):
        self.name = name  # Говорю Python'у: имя конкретного робота(объекта) - то значение, которое я передал в функцию
        self.lasers_from_eyes = lasers_from_eyes

    def get_data(self):
        return (f'Имя: {self.name}, Возможность стрелять лазерами: {self.lasers_from_eyes}, '
                f'Возможность ходьбы: {self.ability_to_walk}, Гарантийный срок: {self.best_before_date}')
                # Данные какого-то робота уже переданы. Python их берет, так как self указывает на нужный объект


robot1 = Robot()  # Создание объекта на основе класса
robot1.data(input('Введите имя: '),input('Будет стрелять лазерами из глаз?: '))  # Передаю только те аргументы,
                                                                                 # которые по логике должны быть изменяемы
print(robot1.get_data())
