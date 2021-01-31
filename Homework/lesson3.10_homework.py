# lesson3.10

# EDIT_1
# Написать маленькую программу, которая на Ваше усмотрение, 
# реализует полиморфизм. Пример придумать самим

class Toyota:
    def get_information(self) -> str:
        """Showing information about the manufacturer"""
        print('Описание производителя из Википедии')
    
class Camry(Toyota):
    def get_information(self) -> str:
        """Showing information about the car"""
        super().get_information()
        print('Описание модели из Википедии')

class Auris(Toyota):
    def get_information(self) -> str:
        """Showing information about the car"""
        print('Описание модели из Википедии')

# mycar = Camry()
# mycar.get_information() 

# mycar = Auris()
# mycar.get_information()

# EDIT_2
# Реализовать клас Температуры (как сегодня в конце урока), который 
# на основе @property будет возвращать, присваивать данные для цельсиев, 
# фаренгейтов и кельвинов.

class Temperature:
    def __init__(self, mark = int, scale = str):
        self.__mark = mark
        self.__scale = scale
           
    @property
    def celcius(self):
        if self.__scale == 'C': 
            return self.__mark
        if self.__scale == 'F':
            return int((self.__mark - 32) * (5/9))
        if self.__scale == 'K':
            return int(self.__mark - 273.15)
        
    @celcius.setter
    def celsius(self, value):
        self.__mark = value
        self.__scale = 'C'

    @property
    def fahrenheit(self):
        if self.__scale == 'C': 
            return self.__mark + 32
        if self.__scale == 'F':
            return self.__mark
        if self.__scale == 'K':
            return int((self.__mark - 273.15) * (9/5) + 32)
        
    @fahrenheit.setter
    def fahrenheit(self, value):
        self.__mark = value
        self.__scale = 'F'

    @property
    def kelvin(self):
        if self.__scale == 'C': 
            return int(self.__mark + 273.15)
        if self.__scale == 'F':
            return int((self.__mark - 32) * (5/9) + 273.15)
        if self.__scale == 'K':
            return self.__mark

    @kelvin.setter
    def kelvin(self, value):
        self.__mark = value
        self.__scale = 'K'

# a = Temperature (1, 'C')
# print(a.celsius)
# print(a.kelvin)

# a.celsius = 22
# print(a.celsius)
# print(a.kelvin)

# EDIT_3s
# Бонус+ режим: кто сможет закончить пример с ФУНКТОРОМ сортировки ч-з
# класс получит от меня мастеркласс по чистой архитектуре кода, когда
# будем изучать ВЕБ )

class SortKey:
    values = []

    def __init__(self, *kwargs):
        self.attrs = kwargs

    def __call__(self,	instance):
        for attr in self.attrs:
            self.values.append(getattr(instance, attr)) 
            self.values = [str(i) for i in self.values]
            self.values.sort()
            return self.values
            # Да, способ топорный на 100%, но работает :)

class Person:
    def __init__(self,	name, surname, email):
        self.name = name 
        self.surname = surname 
        self.email = email

    def __repr__(self):
        return self.name

joe = Person('Joe', 'CWE', 'joe@mail.com')
mark = Person('Mark', 'BWasdE', 'mark@mail.com')
jack = Person('Jack', 'A123WqweqeE', 'jack@mail.com')
people = [joe, mark, jack]

print(people) # OUTPUT: [Joe, Mark, Jack] 
people.sort(key = SortKey('email'))
print(people) # OUTPUT: [Jack, Joe, Mark]
people.sort(key = SortKey('surname'))
print(people) # OUTPUT: [Mark, Joe, Jack]