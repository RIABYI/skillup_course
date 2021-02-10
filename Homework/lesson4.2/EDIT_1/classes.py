# lesson4.2

# Задание 1
# Пользователь вводит с клавиатуры набор чисел. Полученные числа необходимо
# сохранить в список (тип списка нужно выбрать в зависимости от поставленной
# ниже задачи). После чего нужно показать меню, в котором предложить 
# пользователю набор пунктов:

# 1. Добавить новое число в список (если такое число существует в списке, нужно
#  вывести сообщение пользователю об этом, без добавления числа).
# 2. Удалить все вхождения числа из списка (пользователь вводит с клавиатуры 
# число для удаления).
# 3. Показать содержимое списка (в зависимости от выбора пользователя список
#  нужно показать с начала или с конца).
# 4. Проверить есть ли значение в списке.
# 5. Заменить значение в списке (пользователь определяет заменить ли только 
# первое вхождение или все вхождения).
# В зависимости от выбора пользователя выполняется действие, после чего 
# меню отображается снова.

class Mydigits:
    def __init__(self):
            self.__digits = []

    def push(self, val = int):
        """adding a new item"""
        if val not in self.__digits:
            self.__digits.append(val)
            print(f'Число {val} добавлено в список!')     
        else:
            print(f'Число {val} уже в списке! Продолжить?')
            choice = input('y/n: ')
            if choice == 'y':
                self.__digits.append(val)
                print(f'Число {val} снова добавлено в список!')     
            else:
                print(f'Число {val} не добавлено в список!')     
            
    def deletion(self, val = int):
        """deleting all given elements"""
        try:
            self.__digits.remove(val)
            print(f'Число {val} удалено из списка!')
        except ValueError:
            print(f'{val} нет в списке!')

    def get_digits(self, change = str) -> str:
        """displaying the current list"""
        if self.__digits != []: 
            if change == '1':
                print(f"Список сейчас: {', '.join(map(str, self.__digits))}")
            if change == '2':
                print(f"Перевернутый список: {', '.join(map(str, self.__digits[::-1]))}")
            if change != '1' and change != '2':
                print('Ошибка в выборе направления списка!')
        else:
            print('Список сейчас пуст!')

    def check_digits(self, val = int) -> str:
        """checks an element for existence in the list"""
        try:
            if int(val) not in self.__digits:
                print(f'Числа {val} еще нет в списке!')
            else:
                print(f'Число {val} уже в списке! Количество вхождений:' 
                        f'{self.__digits.count(val)}')
        except ValueError:
            print(f'{value} не число!')

    def replace(self, val = int, new_val = int, change = str):
        """replacing list items"""
        try:
            val = int(val)
            new_val = int(new_val)
            if val in self.__digits:
                if change == '1':
                    i = self.__digits.index(val)
                    self.__digits[i] = new_val
                    print(f'Первое вхождение числа {val} заменено на {new_val}!')
                if change == '2':
                    for i in self.__digits:
                        if i == val:
                            i = self.__digits.index(val)
                            self.__digits[i]= new_val
                            print(f'Все вхождения числа {val} заменены на {new_val}!')
                if change != '1' and change != '2':
                     print('Ошибка в последнем выборе действия!')
            else:
                print(f'В списке нет значения {val}')
        except ValueError:
            print('Данные введены неправильно!')