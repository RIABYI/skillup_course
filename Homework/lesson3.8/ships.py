# lesson3.8

# Задание 1
# Создайте класс Device, который содержит информацию об устройстве.
# С помощью механизма наследования, реализуйте класс CoffeeMachine 
# (содержит информацию о кофемашине), класс Blender (содержит информацию
# о блендере), класс MeatGrinder (содержит информацию о мясорубке).
# Каждый из классов должен содержать необходимые для работы методы.

# Задание 2
# Создайте класс Ship, который содержит информацию о корабле.
# С помощью механизма наследования, реализуйте класс Frigate (содержит 
# информацию о фрегате), класс Destroyer (содержит информацию об эсминце), 
# класс Cruiser (содержит информацию о крейсере).
# Каждый из классов должен содержать необходимые для работы методы.

# Задание 3
# Запрограммируйте класс Money (объект класса оперирует одной валютой) 
# для работы с деньгами. В классе должны быть предусмотрены поле для хранения
# целой части денег (доллары, евро, гривны и т.д.) и поле для хранения копеек
# (центы, евроценты, копейки и т.д.).
# Реализовать методы для вывода суммы на экран, задания значений для частей.

class SHIP:
    # def __init__(self, purpose = str, displacement = int, crew = int,
    #              armament = int, engine = str, max_speed = int):
    #     self.purpose = purpose
    #     self.displacement = displacement
    #     self.crew = crew
    #     self.armament = armament
    #     self.engine = engine
    #     self.max_speed = max_speed

    def show_ship_information(self):
        """Shows information about the ship"""
        print('---------------------------')
        print(f'Назначение: {self.purpose}'
              f'\nВодоизмещение: {self.displacement} тонн'
              f'\nЭкипаж: {self.crew} человек\nВооружение: {self.armament}'
              f'\nДвигатель: {self.engine}'
              f'\nМаксимальная скорость: {self.max_speed} узлов')
        print('---------------------------')

class FRIGATE(SHIP):
    def __init__(self, name = str, purpose = str, displacement = int, crew = int,
                 armament = int, engine = str, max_speed = int):
        self.name = name
        self.purpose = purpose
        self.displacement = displacement
        self.crew = crew
        self.armament = armament
        self.engine = engine
        self.max_speed = max_speed
    
    def demonstration(self):
        """Show information"""
        print(f'Фрегат {self.name}')
        print('------------------------------------------------')
        print('тут должно быть определение фрегата из википедии')
        super().show_ship_information()

class DESTROYER(SHIP):
    def __init__(self, name = str, purpose = str, displacement = int, crew = int,
                 armament = int, engine = str, max_speed = int):
        self.name = name
        self.purpose = purpose
        self.displacement = displacement
        self.crew = crew
        self.armament = armament
        self.engine = engine
        self.max_speed = max_speed
    
    def demonstration(self):
        """Show information"""
        print(f'Эсминец {self.name}')
        print('------------------------------------------------')
        print('тут должно быть определение эсминца из википедии')
        super().show_ship_information()

class CRUISER(SHIP):
    def __init__(self, name = str, purpose = str, displacement = int, crew = int,
                 armament = int, engine = str, max_speed = int):
        self.name = name
        self.purpose = purpose
        self.displacement = displacement
        self.crew = crew
        self.armament = armament
        self.engine = engine
        self.max_speed = max_speed
    
    def demonstration(self):
        """Show information"""
        print(f'Крейсер {self.name}')
        print('------------------------------------------------')
        print('тут должно быть определение крейсера из википедии')
        super().show_ship_information()

# нет смысла заливать следующий код в отдельный main.py

Avrora = CRUISER('Аврора', 'военный', 6730, 570, 'артиллерия, МТВ', 
                 '3 х паровые', 20)
Hetman = FRIGATE('Гетман Сагайдачный', 'военный', 3100, 180,
                  'артиллерия, МТВ, ЗА', 'ГТСУ', 32)

if __name__ == '__main__':
    print('------------------------------------------')
    print('Приветствуем в демонстраторе кораблей!')
    print('------------------------------------------')
    while True:
        print('Показать информацию о:')
        main_choice = input('1) крейсер "Аврора";\n2) фрегат "Гетман'
                            ' Сагайдачный"\n3) выйти\n')
        print('------------------------------------------')
        if main_choice == '1':
            Avrora.demonstration()
        if main_choice == '2':
            Hetman.demonstration()
        if main_choice == '3':
            break
