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

import time

HOME_VOLTAGE = 220
COFFEEMACHINE_SWITCH = True
BLENDER_SWITCH = True
MEATGRINDER_SWITCH = False

class DEVICE:
    # def __init__(self, voltage = int, switch = bool):
    #     self.voltage = voltage
    #     self.switch = switch
    
    def turning_on(self):
        if self.switch == True:
            print('Запуск устройства')
            print('------------------------------')
            time.sleep(1)
            print('Проверка напряжения в сети')
            time.sleep(1)
            if self.voltage == 220:
                print('Напряжение в сети 220В, продолжение работы')
                print('------------------------------')
                print('Устройство начало работу!')
                return(1)
            else:
                print('------------------------------')
                print('Проверьте напряжение в сети!')
                print('------------------------------')
        else:
            print('Проверьте включатель на устройстве!')
            print('------------------------------')

class COFFEEMACHINE(DEVICE):
    def __init__(self, voltage = int, switch = bool, program = int):
        self.voltage = voltage
        self.switch = switch
        self.program = program
    
    def cup_of_coffee(self) -> str:
        """Definition of a drink"""
        if self.program == 1:
            return('Espresso')
        elif self.program == 2:
            return('Americano')
        elif self.program == 3:
            return('Cappuccino')
        elif self.program == 4:
            return('Latte')
        else:
            return('Hot water')

    def coffee_make(self):
        """Making coffee"""
        print('Приветствуем!')
        print(f'{self.cup_of_coffee()} будет приготовлен через 1 минуту!')
        print('------------------------------')
        if super().turning_on() == 1:
            print('------------------------------')
            time.sleep(1)
            print(f'{self.cup_of_coffee()} готов!')

class BLENDER(DEVICE):
    def __init__(self, voltage = int, switch = bool, program = int):
        self.voltage = voltage
        self.switch = switch
        self.program = program
    
    def product(self) -> str:
        """Definition of a program"""
        if self.program == 1:
            return('Ice')
        elif self.program == 2:
            return('Meat')
        elif self.program == 3:
            return('Soup')
        elif self.program == 4:
            return('Vegetables')
        else:
            return('Water')       

    def product_make(self):
        print('Приветствуем!')
        print(f'{self.product()} будет приготовлен через 1 минуту!')
        print('------------------------------')
        if super().turning_on() == 1:
            print('------------------------------')
            time.sleep(1)
            print(f'{self.product()} готов!')

class MEATGRINDER(DEVICE):
    def __init__(self, voltage = int, switch = bool, program = int):
        self.voltage = voltage
        self.switch = switch
        self.program = program
    
    def semifinished(self) -> str:
        """Definition of a program"""
        if self.program == 1:
            return('Fish')
        elif self.program == 2:
            return('Meat')
        elif self.program == 3:
            return('Meat with bones')
        elif self.program == 4:
            return('Sausage')
        else:
            return('Soft')

    def product_make(self):
        print('Приветствуем!')
        print(f'{self.semifinished()} будет приготовлен через 1 минуту!')
        print('------------------------------')
        if super().turning_on() == 1:
            print('------------------------------')
            time.sleep(1)
            print(f'{self.semifinished()} готов!')

# нет смысла заливать следующий код в отдельный main.py, но можно :)

def main():
    print('Ожидаем Ваш выбор:\n1-воспользоваться кофе-машиной;'
        '\n2-воспользоваться блендером;\n3-воспользоваться мясорубкой;'
        '\n4-закончить работу')
    main_choice = input('Введите цифру: ')
    
    if main_choice == '1':
        print('Какой кофе будем варить?\n1-Эспрессо;\n2-Американо;'
            '\n3-Капучино;\n4-Латте\n5-Налить теплой воды')
        choice = input('Введите цифру: ')
        if choice == '1':
            prod = COFFEEMACHINE(HOME_VOLTAGE, COFFEEMACHINE_SWITCH, 1)
        if choice == '2':
            prod = COFFEEMACHINE(HOME_VOLTAGE, COFFEEMACHINE_SWITCH, 2)
        if choice == '3':
            prod = COFFEEMACHINE(HOME_VOLTAGE, COFFEEMACHINE_SWITCH, 3)
        if choice == '4':
            prod = COFFEEMACHINE(HOME_VOLTAGE, COFFEEMACHINE_SWITCH, 4)
        if choice == '5':
            prod = COFFEEMACHINE(HOME_VOLTAGE, COFFEEMACHINE_SWITCH, 5)
        prod.coffee_make()
    
    if main_choice == '2':
        print('Какой продукт в чаше?\n1-Лёд;\n2-Мясо;'
            '\n3-Суп;\n4-Овощи\n5-вода, жидкость')
        choice = input('Введите цифру: ')
        if choice == '1':
            prod = BLENDER(HOME_VOLTAGE, BLENDER_SWITCH, 1)
        if choice == '2':
            prod = BLENDER(HOME_VOLTAGE, BLENDER_SWITCH, 2)
        if choice == '3':
            prod = BLENDER(HOME_VOLTAGE, BLENDER_SWITCH, 3)
        if choice == '4':
            prod = BLENDER(HOME_VOLTAGE, BLENDER_SWITCH, 4)
        if choice == '5':
            prod = BLENDER(HOME_VOLTAGE, BLENDER_SWITCH, 5)
        prod.product_make()

    if main_choice == '3':
        print('Какой продукт переработать?\n1-Рыба;\n2-Мясо;'
            '\n3-Мясо с костями;\n4-Колбаса\n5-Мягкие тела')
        choice = input('Введите цифру: ')
        if choice == '1':
            prod = MEATGRINDER(HOME_VOLTAGE, MEATGRINDER_SWITCH, 1)
        if choice == '2':
            prod = MEATGRINDER(HOME_VOLTAGE, MEATGRINDER_SWITCH, 2)
        if choice == '3':
            prod = MEATGRINDER(HOME_VOLTAGE, MEATGRINDER_SWITCH, 3)
        if choice == '4':
            prod = MEATGRINDER(HOME_VOLTAGE, MEATGRINDER_SWITCH, 4)
        if choice == '5':
            prod = MEATGRINDER(HOME_VOLTAGE, MEATGRINDER_SWITCH, 5)
        prod.product_make()



if __name__ == '__main__':
    print('------------------------------')
    print('Приветствуем в УМНЫЙ ДОМ !')
    print('------------------------------')
    main()
