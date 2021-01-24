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

import requests

class MONEY:
    def __init__(self, cash = int, coins = float):
        self.cash = cash
        self.coins = coins

    def add_cash(self) -> int:
        """adds money to the wallet"""
        new_money = float(input('Введите добавляемую сумму через точку: '))
        self.cash += int(new_money)
        self.coins += (new_money-int(new_money))
        if self.coins >= 1:
            self.cash += int(self.coins)
            self.coins -= (int(self.coins)) 
        return (self.cash, self.coins)   

    def withdraw_money(self) -> int:
        """takes money from the wallet"""
        take_money = float(input('Введите отнимаемую сумму через точку: '))
        self.cash -= int(take_money)
        self.coins -= ( take_money-int(take_money))
        if self.coins < 0:
            self.cash -= int(self.coins)
            self.coins += (int(self.coins))
        return (self.cash, self.coins)   

    def show_money(self) -> str:
        """shows how much money"""
        if self.coins == 0: 
            print(f'You have {self.cash} {self.name}')
        if self.coins > 0: 
            print(f'You have {self.cash}.{int(self.coins*100)} {self.name}')

    @staticmethod
    def exchange_rates() -> int: 
        "checking exchange rates"
        url = 'https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5'
        response = requests.get(url).json()
        UAH_USD = float(response[0]['buy'])
        UAH_EUR = float(response[1]['buy'])
        USD_EUR = round(UAH_EUR / UAH_USD, 2)
        return(UAH_USD, UAH_EUR, USD_EUR)

class USD(MONEY):
    cash = 0    
    coins = 0

    def __init__(self, cash = float, name = 'USD'):
        self.cash = cash
        self.name = name

    def exchange_USD_UAH(self) -> int:
        """exchange USD -> UAH"""
        self.cash += self.coins
        result = (self.cash*(self.exchange_rates()[0]))
        UAH.cash += int(result)
        UAH.coins += (result-int(result))
        self.cash -= self.cash

    def exchange_USD_EUR(self) -> int:
        """exchange USD -> EUR"""
        self.cash += self.coins
        result = (self.cash*(self.exchange_rates()[2]))
        EUR.cash += int(result)
        EUR.coins += (result-int(result))
        self.cash -= self.cash

class UAH(MONEY):
    cash = 0    
    coins = 0

    def __init__(self, cash = float, name = 'UAH'):
        self.cash = cash
        self.name = name

    def exchange_UAH_USD(self)  -> int:
        """exchange UAH -> USD"""
        self.cash += self.coins
        result = (self.cash/(self.exchange_rates()[0]))
        USD.cash += int(result)
        USD.coins += (result-int(result))
        self.cash -= self.cash

    def exchange_UAH_EUR(self)  -> int:
        """exchange UAH -> EUR"""
        self.cash += self.coins
        result = (self.cash/(self.exchange_rates()[1]))
        EUR.cash += int(result)
        EUR.coins += (result-int(result))
        self.cash -= self.cash

class EUR(MONEY):
    cash = 0    
    coins = 0

    def __init__(self, cash = float, name = 'EUR'):
        self.cash = cash
        self.name = name

    def exchange_EUR_UAH(self) -> int:
        """exchange EUR -> UAH"""
        self.cash += self.coins
        result = (self.cash*(self.exchange_rates()[1]))
        UAH.cash += int(result)
        UAH.coins += (result-int(result))
        self.cash -= self.cash

    def exchange_EUR_USD(self) -> int:
        """exchange EUR -> USD"""
        self.cash += self.coins
        result = (self.cash/(self.exchange_rates()[2]))
        USD.cash += int(result)
        USD.coins += (result-int(result))
        self.cash -= self.cash

# нет смысла заливать следующий код в отдельный main.py

if __name__ == '__main__':
    print('Приветствуем в приложении БАНК')
    usd = USD(1)
    uah = UAH(255)
    eur = EUR(1)
    usd.show_money()
    uah.show_money()
    eur.show_money()
    while True:
        print('---------------------------------------')
        print('Введите:\n1 - пополнить кошелек;\n2 - снять деньги;'
            '\n3 - посмотреть активный баланс;\n4 - обменять валюту'
            '\n5 - выйти')
        print('---------------------------------------')
        main_choice = input()
        print('---------------------------------------')
        if main_choice == '1':
            choice = input('Введите какой кошелек нужно пополнить:\n'
                        '1 - USD, 2 - UAH, 3 - EUR\n')
            if choice == '1':
                usd.add_cash() 
            if choice == '2':
                uah.add_cash() 
            if choice == '3':
                eur.add_cash() 

        if main_choice == '2':
            choice = input('Введите c какого кошелька нужно снять деньги:\n'
                        '1 - USD, 2 - UAH, 3 - EUR')        
            if choice == '1':
                usd.withdraw_money() 
            if choice == '2':
                uah.withdraw_money() 
            if choice == '3':
                eur.withdraw_money() 

        if main_choice == '3':
            usd.show_money()
            uah.show_money()
            eur.show_money()  

        if main_choice == '4':
            print('---------------------------------------')
            print('Выбирите схему обмена:\n1) USD -> UAH:\n2) USD -> EUR;'
                  '\n3) UAH -> USD;\n4) UAH -> EUR;\n5) EUR -> USD;'
                  '\n6) EUR -> UAH')
            print('---------------------------------------')
            choice = input()
            if choice == '1':
                usd.exchange_USD_UAH()
            if choice == '2':
                usd.exchange_USD_EUR()
            if choice == '3':
                uah.exchange_UAH_USD()
            if choice == '4':
                uah.exchange_UAH_EUR()    
            if choice == '5':
                eur.exchange_EUR_USD()    
            if choice == '6':
                eur.exchange_EUR_UAH()    

        if main_choice == '5':
            break