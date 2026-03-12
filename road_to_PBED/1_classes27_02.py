class Robot:
    def __init__(self, name, years, garantiya):
        self.name = name
        self.__years = years
        self.__garantiya = garantiya

    def set_get_garantiya(self, garantiya):
        self.__garantiya = garantiya -5



robot1 = Robot('Саша', 10, 10)

# robot1.__years -= 5
# print(robot1.__years)  # Ошибка!!!

print(robot1.set_get_garantiya(10))  # 5