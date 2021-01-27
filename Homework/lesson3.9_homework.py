# lesson3.9

# Разработайте класс с "полной инкапсуляцией", доступ к атрибутам которого и
# изменение данных реализуются через вызовы методов. В объектно-ориентированном
# программировании принято имена методов для извлечения данных начинать со 
# слова get (взять), а имена методов, в которых свойствам присваиваются значения,
#  – со слова set (установить). Например, getField, setField

class Automobile:
    def __init__(self, manufacturer = str, model = str, price = int):
        self.__manufacturer = manufacturer
        self.__model = model
        self.__price = price

    def get_car_information(self) -> str:
        """Showing car information"""
        print(f'Автомобиль: {self.__manufacturer} {self.__model}'
              f'\nЦЕНА: {self.__price}')

    def get_manufacturer(self) -> str:
        """Return car information: manufacturer"""
        return(self.__manufacturer)

    def get_model(self) -> str:
        """Return car information: model"""
        return(self.__model)

    def get_price(self) -> int:
        """Return car information: price"""
        return(self.__price)

    def set_car_information(self):
        """Changes all car information"""
        self.__manufacturer = input('Введите марку автомобиля: ')
        self.__model = input('Введите модель автомобиля: ')
        self.__price = int(input('Введите стоимость автомобиля: '))

    def __setattr__(self, name, value): #Защищает от создания 'левых' атрибутов
        if name in ['_Automobile__manufacturer', '_Automobile__model', 
                    '_Automobile__price']:
            self.__dict__[name] = value
  
    def __getattr__(self, name): # Объясняет, что атрибут 'левый' 
        if name not in ['_Automobile__manufacturer', '_Automobile__model', 
                        '_Automobile__price']: # Можно заменить на self.__dict__
            return f'Атрибут "{name}" не существует!'


mycar = Automobile('Mazda', '6', 15000) # Создаем объект
mycar.get_car_information() # Получаем информацию (извлекаем все данные) про объект
mycar.zet = 'VAZda' # Пробуем создать 'лишний' атрибут
print(mycar.zet) # Пробуем узнать 'лишний' атрибут
# mycar.set_car_information() # Меняем всю информацию про автомобиль
mycar.get_car_information() 
print(mycar.get_price()) # Извлекаем данные о стоимости автомобиля