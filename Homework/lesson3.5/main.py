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

from services import i_date, XOR_cipher

while True:  
    print('--------------------------------------------------------')
    print('Введите номер действия:\n1. Проверить дату на валидность;'
        '\n2. Кодировать/декодировать строку;\n3. Выйти.')
    main_choice=int(input())
    print('--------------------------------------------------------')
    if main_choice == 1:
        user_date = input('Введите дату в формате ДД.ММ.ГГГГ: ')
        i_date(user_date)
    if main_choice == 2:
        text = input('Введите строку, которую нужно кодировать(декодировать):\n')
        key = input('Введите ключ шифрования:\n')
        print(XOR_cipher(text, key))
    if main_choice == 3:
        break