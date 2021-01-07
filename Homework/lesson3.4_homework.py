# lesson3.4

# Задание 1
# Дано два текстовых файла. Выяснить, совпадают ли их строки. 
# Если нет, то вывести несовпадающую строку из каждого файла.

# Задание 2
# Дан текстовый файл. Необходимо создать новый файл и записать
# в него следующую статистику по исходному файлу:
# ■ Количество символов;
# ■ Количество строк;
# ■ Количество гласных букв;
# ■ Количество согласных букв; 
# ■ Количество цифр.

# Задание 3
# Дан текстовый файл. Удалить из него последнюю строку. 
# Результат записать в другой файл.

# Задание 4
# Дан текстовый файл. Найти длину самой длинной строки.

# Задание 5
# Дан текстовый файл. Посчитать сколько раз в нем 
# встречается заданное пользователем слово.

# Задание 6
# Дан текстовый файл. Найти и заменить в нем заданное слово.
# Что искать и на что заменять определяется пользователем.

# EDIT 1

with open("1.txt", "r") as file1, open("2.txt", "r") as file2:
    lines1=file1.readlines()
    lines2=file2.readlines()
    if lines1==lines2:
        print('Файлы совпадают')
    else:
        print('В файлах не совпадают следующие строки:')
        list1=[i for i in lines1 if i not in lines2 and i!='\n']
        list2=[c for c in lines2 if c not in lines1 and c!='\n']
        print(''.join(list1+list2), end='')

# EDIT 2

def statistics():
    try: 
        with open("1.txt", "r") as stream, open("result-file.txt", "w") as result:
            lines = stream.readlines()
            line=("".join(lines)).replace('\n', '').replace(' ', '')
            vowels = ['A', 'E', 'I', 'O', 'U', 'Y']
            vowels_in_line=[i for i in line.upper() if i in vowels]
            digits_in_line=[i for i in line if i.isdigit()]
            consonants_in_line=[i for i in line.upper() if i not in vowels 
                                and i not in digits_in_line and i!='']
            result.write(f'Количество строк: {len(lines)}\n'
                         f'Общее к-во символов: {len(line)}\n'
                         f'Общее к-во гласных: {len(vowels_in_line)}\n'
                         f'Общее к-во согласных: {len(consonants_in_line)}\n'
                         f'Общее к-во цифр: {len(digits_in_line)}')
    except FileNotFoundError:
        print('File not faund')


statistics()

# EDIT 3

def delete_last():
    try: 
        with open("1.txt", "r") as stream, open("update-file.txt", "w") as result:
            lines = stream.readlines()
            result.write(''.join(lines[:-1]))
    except FileNotFoundError:
        print('File not faund')


delete_last()

# EDIT 4

def maximal_line():
    try: 
        with open("1.txt", "r") as stream:
            list1 = []
            for i in stream:
                list1.append(len(i.replace('\n', '')))
            print(f'Максимальная длина строки: {max(list1)} символ(-a; -ов)')
    except FileNotFoundError:
        print('File not faund')


maximal_line()

# EDIT 5

def finder(word):
    try: 
        with open("1.txt", "r") as file:
            words = []
            for i in file:
                i = i.replace('\n','').replace(' ', '')
                words.append(i)
            print(f'Запрос "{word}" встречается в файле {words.count(word)} раз(а)')
    except FileNotFoundError:
        print('File not faund')


finder('88')

# EDIT 6

def replacer(word, new_word):
    try:
        with open("1.txt", "r") as stream:
            lines = stream.read().replace(word, new_word)
        with open("1.txt", "w") as stream:
            stream.write(lines)
    except FileNotFoundError:
        print('File not faund')


replacer('22', '88')