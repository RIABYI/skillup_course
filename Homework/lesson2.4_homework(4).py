# lesson2.4

# Задание 2.3
# Создайте программу «Фирма». Нужно хранить информацию о человеке: 
# ФИО, телефон, рабочий email, название должности, номер кабинета, 
# skype. Требуется реализовать возможность добавления, удаления, 
# поиска, замены данных. Используйте словарь для хранения информации.

main_dict = {
    1001:['Kulikov S.V.', 'director', '937-99-92', 'kulikov.firma@mail.com', '1', 'boss'],
    1002:['Petrov O.P.', 'lawyer', '937-99-93', 'petrov.firma@mail.com', '2', 'lawyer993'],
    1003:['Vasilcheno K.T.', 'accountant', '937-99-94', 'vasilchenko.firma@mail.com', '3', 'accountanе885'],
    1004:['Glushkov D. V.', 'seller', '937-99-95', 'glushkov.firma@mail.com', '4', 'prodavec004'],  
    }

print('---------------------------------------------------------------------')
print("Программа 'Фирма'. Версия 1.0.0")
print('---------------------------------------------------------------------')
print('ФОРМАТ:\nНомер личного дела: ФИО, должность, телефон, почта, номер кабинета, скайп')
for key, value in main_dict.items():
    print(key, ': ', ', '.join(str(num) for num in value), sep='')
print('---------------------------------------------------------------------')

a=5
while a>1:

    print('Возможные действия:\n1) добавить работника; 2) удалить информацию о работнике;' 
        ' 3) редактировать информацию о работнике; 4) найти работника; 5) выйти')
    print('---------------------------------------------------------------------')

    main_choice = int(input('Введите номер нужного действия: '))
    print('---------------------------------------------------------------------')

    if main_choice == 1:
        number = input('Введите номер личного дела нового работника: ')
        name = input('Введите фамилию и инициалы работника: ')
        position = input('Введите должность работника: ')
        phone = input('Введите номер телефона работника: ')
        mail = input('Введите почту работника: ')
        kab = input('Введите номер кабинета работника: ')
        skype = input('Введите никнейм работника в Skype: ')
        print('---------------------------------------'
        '------------------------------')
        print(f'Номер личного дела: {number}, ФИО: {name}, должность: {position},'
              f'телефон: {phone}, почта: {mail}, кабинет № {kab}, скайп: {skype}')
        choice_1=input('Вы уверенны? (y/n): ')
        print('---------------------------------------'
        '------------------------------')
        if choice_1 == 'y':
            main_dict[number]=[name, position, phone, mail, kab, skype]
            for key, value in main_dict.items():
                print('ФОРМАТ:\nНомер личного дела: ФИО, должность,' 
                    'телефон, почта, номер кабинета, скайп')
                print(key, ': ', ', '.join(str(num) for num in value), sep='')
        else: 
            exit

    elif main_choice == 2:
        remove = int(input('Введите номер личного дела работника, информацию'
                           ' которого необходимо удалить: '))
        print('---------------------------------------'
        '------------------------------')
        print(*main_dict[remove], sep=', ')
        choice_2=input('Вы уверенны? (y/n): ')
        print('---------------------------------------'
        '------------------------------')
        if choice_2 == 'y':
            del main_dict[remove]
            for key, value in main_dict.items():
                print('ФОРМАТ:\nНомер личного дела: ФИО, должность,' 
                    'телефон, почта, номер кабинета, скайп')
                print(key, ': ', ', '.join(str(num) for num in value), sep='')
        else: 
            exit

    elif main_choice == 3:
        replace = int(input('Введите номер личного дела работника, информацию'
                            ' которого необходимо редактировать: '))
        print('---------------------------------------'
        '------------------------------')
        print(*main_dict[replace], sep=', ')
        choice_3=input('Вы уверенны? (y/n): ')
        print('---------------------------------------'
        '------------------------------')
        if choice_3 == 'y':
            print('Введите какую информацию необходимо редактировать:\n'
                  '1) номер ЛД; 2) ФИО; 3) должность; 4) телефон;\n'
                  '5) почта; 6) номер кабинета; 7) скайп')
            choice_4 = int(input())
            if choice_4 == 1:
                nld=input(f'Введите корректный номер личного дела {main_dict[replace][0]}: ')
                print('---------------------------------------'
                '------------------------------')
                print(nld, ' - ', ', '.join(main_dict[replace]))
                choice_5=input('Вы уверенны? (y/n): ')
                print('---------------------------------------'
                '------------------------------')
                if choice_5 == 'y':
                    main_dict[nld]=main_dict.pop(replace)
                    print('ФОРМАТ:\nНомер личного дела: ФИО, должность,' 
                              'телефон, почта, номер кабинета, скайп')
                    for key, value in main_dict.items():
                        print(key, ': ', ', '.join(str(num) for num in value), sep='')

            elif choice_4 == 2:
                name=input(f'Введите корректное ФИО {main_dict[replace][0]}: ')
                print('---------------------------------------'
                '------------------------------')
                print(f'{main_dict[replace][0]} сменить на {name}?')
                choice_5=input('Вы уверенны? (y/n): ')
                print('---------------------------------------'
                '------------------------------')
                if choice_5 == 'y':
                    main_dict[replace][0]=name
                    print('ФОРМАТ:\nНомер личного дела: ФИО, должность,' 
                              'телефон, почта, номер кабинета, скайп')
                    for key, value in main_dict.items():
                        print(key, ': ', ', '.join(str(num) for num in value), sep='')

            elif choice_4 == 2:
                name=input(f'Введите корректное ФИО {main_dict[replace][0]}: ')
                print('---------------------------------------'
                '------------------------------')
                print(f'{main_dict[replace][0]} сменить на {name}?')
                choice_5=input('Вы уверенны? (y/n): ')
                print('---------------------------------------'
                '------------------------------')
                if choice_5 == 'y':
                    main_dict[replace][0]=name
                    print('ФОРМАТ:\nНомер личного дела: ФИО, должность,' 
                              'телефон, почта, номер кабинета, скайп')
                    for key, value in main_dict.items():
                        print(key, ': ', ', '.join(str(num) for num in value), sep='')

            elif choice_4 == 3:
                position=input(f'Введите должность {main_dict[replace][0]}: ')
                print('---------------------------------------'
                '------------------------------')
                print(f'{main_dict[replace][1]} сменить на {position}?')
                choice_5=input('Вы уверенны? (y/n): ')
                print('---------------------------------------'
                '------------------------------')
                if choice_5 == 'y':
                    main_dict[replace][1]=position
                    print('ФОРМАТ:\nНомер личного дела: ФИО, должность,' 
                              'телефон, почта, номер кабинета, скайп')
                    for key, value in main_dict.items():
                        print(key, ': ', ', '.join(str(num) for num in value), sep='')

            elif choice_4 == 4:
                phone=input(f'Введите телефон {main_dict[replace][0]}: ')
                print('---------------------------------------'
                '------------------------------')
                print(f'{main_dict[replace][2]} сменить на {phone}?')
                choice_5=input('Вы уверенны? (y/n): ')
                print('---------------------------------------'
                '------------------------------')
                if choice_5 == 'y':
                    main_dict[replace][2]=phone
                    print('ФОРМАТ:\nНомер личного дела: ФИО, должность,' 
                              'телефон, почта, номер кабинета, скайп')
                    for key, value in main_dict.items():
                        print(key, ': ', ', '.join(str(num) for num in value), sep='')
            
            elif choice_4 == 5:
                mail=input(f'Введите почту {main_dict[replace][0]}: ')
                print('---------------------------------------'
                '------------------------------')
                print(f'{main_dict[replace][3]} сменить на {mail}?')
                choice_5=input('Вы уверенны? (y/n): ')
                print('---------------------------------------'
                '------------------------------')
                if choice_5 == 'y':
                    main_dict[replace][3]=mail
                    print('ФОРМАТ:\nНомер личного дела: ФИО, должность,' 
                              'телефон, почта, номер кабинета, скайп')
                    for key, value in main_dict.items():
                        print(key, ': ', ', '.join(str(num) for num in value), sep='')
            
            elif choice_4 == 6:
                kab=input(f'Введите номер кабинета {main_dict[replace][0]}: ')
                print('---------------------------------------'
                '------------------------------')
                print(f'{main_dict[replace][4]} сменить на {kab}?')
                choice_5=input('Вы уверенны? (y/n): ')
                print('---------------------------------------'
                '------------------------------')
                if choice_5 == 'y':
                    main_dict[replace][4]=kab
                    print('ФОРМАТ:\nНомер личного дела: ФИО, должность,' 
                              'телефон, почта, номер кабинета, скайп')
                    for key, value in main_dict.items():
                        print(key, ': ', ', '.join(str(num) for num in value), sep='')

            elif choice_4 == 7:
                skype=input(f'Введите скайп {main_dict[replace][0]}: ')
                print('---------------------------------------'
                '------------------------------')
                print(f'{main_dict[replace][5]} сменить на {skype}?')
                choice_5=input('Вы уверенны? (y/n): ')
                print('---------------------------------------'
                '------------------------------')
                if choice_5 == 'y':
                    main_dict[replace][5]=skype
                    print('ФОРМАТ:\nНомер личного дела: ФИО, должность,' 
                              'телефон, почта, номер кабинета, скайп')
                    for key, value in main_dict.items():
                        print(key, ': ', ', '.join(str(num) for num in value), sep='')    
            else:
                exit

    elif main_choice == 4:
        search =input('Введите поисковый запрос: ')
        if search.isdigit() == True:
            search=int(search)
        # Реализовано с условием ввода пользователем точного
        # значения, например: 'Kulikov S.V.', а не 'Kulikov',
        # c целью экономии времени, но не проблема сделать :)
        for key, value in main_dict.items():
            if key == search or search in value:
                print('ФОРМАТ:\nНомер личного дела: ФИО, должность,' 
                      'телефон, почта, номер кабинета, скайп')
                print('---------------------------------------'
                '------------------------------')      
                print(key, ': ', ', '.join(str(num) for num in value), sep='')
                print('---------------------------------------'
                '------------------------------')
                break
            else:
                print('Нет совпадений')

    elif main_choice == 5:
        break

    else:
        print('error')
        print('---------------------------------------------------------------------')