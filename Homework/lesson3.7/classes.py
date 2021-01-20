# Lesson 3.7

# Задание 1
# Реализуйте класс «Автомобиль». Необходимо хранить в полях класса: 
# название модели, год выпуска, производителя, объем двигателя, цвет машины,
# цену. Реализуйте методы класса для ввода данных, вывода данных, реализуйте 
# доступ к отдельным полям через методы класса.

# Задание 2
# Реализуйте класс «Книга». Необходимо хранить в полях класса: название 
# книги, год выпуска, издателя, жанр, автора, цену. Реализуйте методы 
# класса для ввода данных, вывода данных, реализуйте доступ к отдельным 
# полям через методы класса.

# Задание 3
# Реализуйте класс «Стадион». Необходимо хранить в полях класса: название 
# стадиона, дату открытия, страну, город, вместимость. Реализуйте методы 
# класса для ввода данных, вывода данных, реализуйте доступ к отдельным 
# полям через методы класса.

# EDIT_1

class automobile:
    def __init__(self, manufacturer, model, year, engine, color, price):
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.engine = engine
        self.color = color
        self.price = price

    def add_car(self):
        """Add new car"""
        self.manufacturer = input('Введите название марки автомобиля: ')
        self.model = input('Введите название модели: ')
        self.year  = input('Введите год выпуска: ')
        self.engine = input('Введите объем двигателя: ')
        self.color = input('Введите цвет автомобиля: ')
        self.price = input('Введите цену автомобиля: ')

    def print_car(self):
        """Showing car information"""
        print(f'Автомобиль: {self.manufacturer} {self.model}, {self.year}' 
              f'года выпуска.\nОбъем двигателя: {self.engine} л.; '
              f'цвет: {self.color}\nЦЕНА: {self.price}')

    def get_name_car(self):
        """Showing car name"""
        print(self.manufacturer, self.model)

    def get_price(self):
        """Showing car price"""
        print(f'Стоимость автомобиля: {self.price}')

    # def __del__(self):
    #     print('Информация про автомобиль удалена')


# EDIT_2

class book:
    
    def __init__(self, name = '', year = '', publisher = '', 
                 genre = '', author = '', price = ''):
        self.name = name
        self.year = year
        self.publisher = publisher
        self.genre = genre
        self.author = author
        self.price = price

    def add_book(self):
        """Add new book"""
        self.name = input('Введите название книги: ')
        self.year  = input('Введите год книги: ')
        self.publisher = input('Введите издательство: ')
        self.genre = input('Введите жанр книги: ')
        self.author = input('Введите автора книги: ')
        self.price = input('Введите цену: ')

    def print_book(self):
        """Showing book information"""
        print(f'Название книги: {self.name}, {self.year} год,' 
              f'издательство {self.publisher}' 
              f'\nЖанр: {self.genre}, автор: {self.author}, ЦЕНА: {self.price}')

    def get_book_name(self):
        """Showing book name"""
        print(f'Название книги: {self.name}')

    def get_price(self):
        """Showing book price"""
        print(f'Стоимость книги: {self.price}')

    # def __del__(self):
    #     print('Книга удалена из памяти.')
    
# EDIT 3

class stadium:
    stadiums = 0
    def __init__(self, name, opening, country, city, capacity = int):
        self.name = name
        self.opening = opening
        self.country = country
        self.city = city
        self.capacity = capacity
        self.stadiums += 1
    
    def add_stadium(self):
        """Add new stadium"""
        self.name = input('Введите название стадиона: ')
        self.opening   = input('Введите дату открытия: ')
        self.country  = input('Введите страну: ')
        self.city = input('Введите город: ')
        self.capacity = input('Введите вместимость: ')

    def print_stadium(self):
        """Showing stadium information"""
        print(f'Название стадиона: {self.name}, открыт {self.opening}\n' 
              f'Местонахождение: {self.country}, {self.city}\n' 
              f'Вместимость: {self.capacity} человек')

    def stadiums_count(self):
        """Showing amount stadium"""
        print(f'Всего стадионов: {self.stadiums}')

    def location(self):
        """Showing stadium location"""
        print(f'Местонахождение стадиона: {self.country}, {self.city}')
