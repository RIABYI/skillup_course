# lesson3.5

# 1. Написать функцию date, принимающую 3 аргумента — день, месяц и год. 
# Вернуть True, если такая дата есть в нашем календаре, и False иначе.

# (*)2. XOR-шифрование (*)
# Написать функцию XOR_cipher, принимающая 2 аргумента: строку, которую
# нужно зашифровать, и ключ шифрования, которая возвращает строку, зашифрованную 
# путем применения функции XOR (^) над символами строки с ключом. Написать также 
# функцию XOR_uncipher, которая по зашифрованной строке и ключу восстанавливает 
# исходную строку.

# Ф-ции собрать в модуль services.py
# и показать его возможности в файле main.py

from datetime import datetime, date
 
DAYS = ('понедельник', 'вторник', 'среда', 'четверг', 'пятница', 
        'суббота', 'воскресенье')

def i_date(u_date) -> str:
    """checks if the entered date is correct"""
    try:
        wd=date.weekday(datetime.strptime(u_date, "%d.%m.%Y"))
        print(f'Есть такая дата, это {DAYS[wd]}!')
    except:
        # На любой случай, если модуль datetime даст ошибку 
        print('Нет такой даты')   


def XOR_cipher( text, key ) -> str: 
    """encoding and decoding string"""
    encoded_str = ""
    if key.isdigit():
        key=int(key)
    else:
        return('Ключ должен быть целым числом!')
    for symbol in text:
        encoded_str += chr((ord(symbol) ^ key))
    return encoded_str  
