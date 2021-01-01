# lesson3.3

# 1. Написать функцию-декоратор, которая подносит к квадрату значения,
#  которое возвращает функция, к которой декоратор применяется.
# 2. Реализовать декоратор подключения драйвера к принтеру

import requests

# ----------------------------------------------------------------------------
#                            EDIT 1
# ----------------------------------------------------------------------------

def decorator_function(func):
    def square():
        print(f'-------({func()})-squared--------')
        print('{:*^24}'.format(func()**2))
        print('---------------------------')
    return square


@decorator_function
def squared():
    return(-9) 


squared()

# ----------------------------------------------------------------------------
#                            EDIT 2
# ----------------------------------------------------------------------------
# PS Я художник - я так вижу :)

printers = {1: 'https://habr.com/',
            2: 'https://brewhfksnfls.com/',
            }
            # словарь с номером принтера и IP

def driver_connection(func):
    def checking(printer_id):
        main_ip='https://www.google.com'
        #Пусть это будет условным IP главного сервера предприятия :)
        print('--------------------------------')
        try:
            requests.get(main_ip)
            # Проверяем соединение с главным сервером
            try:
                requests.get(printers[printer_id]) 
                # Проверяем соединение с принтером
                func()
            except:
                print('No connection. Check printer.')
        except:
            print('No connection. Check network.')
        print('--------------------------------')
    return(checking)


@driver_connection
def hp_printer():
    print('Hello! HP successfully connected!')


@driver_connection
def epson_printer():
    print('Hello! EPSON successfully connected!')


hp_printer(1)
epson_printer(2)