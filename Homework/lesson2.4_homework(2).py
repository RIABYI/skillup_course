# lesson2.4

# Задание 2.1
# Создайте программу, хранящую информацию о великих баскетболистах. Нужно
# хранить ФИО баскетболиста и его рост. Требуется реализовать возможность 
# добавления, удаления, поиска, замены данных. Используйте словарь для 
# хранения информации.

# Сделана более узкая программа с выводом словаря, в котором хранятся
# имена легендарных баскетболистов Майами Хитс с закрепленными номерами

# Как говорится, я художник - я так вижу :)

main_dict = {
    10:['Timothy Duane Hardaway', '183 cm'],
    32:["Shaquille Rashaun O'Neal", '216 cm'],
    33:['Alonzo Harding Mourning', '208 cm'],
    3:['Dwyane Tyrone Wade', '193 cm'],  
    }

print('---------------------------------------------------------------------')
print('Легендарные игроки Майами Хит с закреплёнными номерами:')
print('---------------------------------------------------------------------')
for key, value in main_dict.items():
    print(key, ': ', ', '.join(str(num) for num in value), sep='')
print('---------------------------------------------------------------------')

a=5
while a>1:

    print('Возможные действия:\n1) добавить игрока; 2) удалить игрока;' 
        ' 3) заменить игрока; 4) найти игрока; 5) выйти')
    print('---------------------------------------------------------------------')

    main_choice = int(input('Введите номер нужного действия: '))
    print('---------------------------------------------------------------------')

    if main_choice == 1:
        number = input('Введите номер игрока: ')
        name = input('Введите имя и фамилию игрока: ')
        height = str(input('Введите рост игрока в см: '))+' см'
        print('---------------------------------------'
        '------------------------------')
        print(f'{number}, {name}, {height}')
        choice_1=input('Вы уверенны? (y/n): ')
        print('---------------------------------------'
        '------------------------------')
        if choice_1 == 'y':
            main_dict[number]=[name, height]
            for key, value in main_dict.items():
                print(key, ': ', ', '.join(str(num) for num in value), sep='')
        else: 
            exit

    elif main_choice == 2:
        remove = int(input('Введите номер игрока, которого необходимо удалить: '))
        print('---------------------------------------'
        '------------------------------')
        print(*main_dict[remove], sep=', ')
        choice_2=input('Вы уверенны? (y/n): ')
        print('---------------------------------------'
        '------------------------------')
        if choice_2 == 'y':
            del main_dict[remove]
            for key, value in main_dict.items():
                print(key, ': ', ', '.join(str(num) for num in value), sep='')
        else: 
            exit

    elif main_choice == 3:
        replace = int(input('Введите номер игрока, которого необходимо заменить: '))
        print('---------------------------------------'
        '------------------------------')
        print(*main_dict[replace], sep=', ')
        choice_3=input('Вы уверенны? (y/n): ')
        print('---------------------------------------'
        '------------------------------')
        if choice_3 == 'y':
            name = input(f'Введите имя и фамилию игрока с номером {replace}: ')
            height = str(input(f'Введите рост {name} в см: '))+' см'
            print('---------------------------------------'
            '------------------------------')
            print(f'{replace}, {name}, {height}')
            choice_4=input('Вы уверенны? (y/n): ')
            print('---------------------------------------'
            '------------------------------')
            if choice_4 == 'y':
                main_dict[replace]=[name, height]
                for key, value in main_dict.items():
                    print(key, ': ', ', '.join(str(num) for num in value), sep='')
            else:
                exit
        else:
            exit


    elif main_choice == 4:
        search =input('Введите поисковый запрос: ')
        if search.isdigit() == True:
            search=int(search)
        # Реализовано с условием ввода пользователем точного
        # значения номера, имени или веса, например: '187 см', а не '187',
        # c целью экономии времени, но не проблема сделать :)
        for key, value in main_dict.items():
            if key == search or search in value:
                print(key, ': ', ', '.join(str(num) for num in value), sep='')
            else:
                print('Нет совпадений')

    elif main_choice == 5:
        break

    else:
        print('error')