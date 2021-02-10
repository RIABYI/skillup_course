# lesson4.2

# Задание 2
# Реализуйте класс стека для работы со строками (стек строк).
# Стек должен иметь фиксированный размер.
# Реализуйте набор операций для работы со стеком:
# ■ помещение строки в стек;
# ■ выталкивание строки из стека;
# ■ подсчет количества строк в стеке;
# ■ проверку пустой ли стек;
# ■ проверку полный ли стек;
# ■ очистку стека;
# ■ получение значения без выталкивания верхней строки
# из стека.
# При старте приложения нужно отобразить меню с помощью, которого
#  пользователь может выбрать необходимую операцию.

# Задание 3
# Измените стек из второго задания, таким образом, чтобы его размер был нефиксированным.

class LimitedStack:
    def __init__(self):
        self.__data = []
    
    def data(self):
        if self.__data != []:
            return self.__data
        else:
            return 'Стек пуст!'

    def push(self, val):
        self.__data.append(val)
        if len(self.__data) == 6:
            return self.pop()
        return f'{val} добавлен!'
    
    def pop(self):
        try:
            tmp = self.__data[0]
            del self.__data[0] 
            return f'{tmp} выпал со списка!'
        except IndexError:
            return 'Стек пуст!'

    def stack_lenght(self):
        return len(self.__data)
    
    def empty_stack(self):
        if self.__data == []:
            return True
        else:
            return False 

    def full_stack(self):
        print(len(self.__data))
        if len(self.__data) == 5:
            return True
        else:
            return False 

    def cleaning(self):
        self.__data.clear()

class NoLimitedStack:
    def __init__(self):
        self.__data = []
    
    def data(self):
        if self.__data != []:
            return self.__data
        else:
            return 'Стек пуст!'

    def push(self, val):
        self.__data.append(val)
        return f'{val} добавлен!'
    
    def pop(self):
        try:
            tmp = self.__data[0]
            del self.__data[0] 
            return f'{tmp} выпал со списка!'
        except IndexError:
            return 'Стек пуст!'

    def stack_lenght(self):
        return len(self.__data)
    
    def empty_stack(self):
        if self.__data == []:
            return True
        else:
            return False 

    def cleaning(self):
        self.__data.clear()