# lesson4.1

# 1. Создать генератор, который возвращает значение умноженное на 2 с
# указанного дапазону (2, 20) -> 4, 6, ...

def double(a, b):
    if a > b:
        a, b = b, a
    for i in range(a, b+1):
        yield i*2 

for result in double(5, 8):
    print(result)

# ***2. Написать ф-цию, которая просматривает файлы в указанном каталоге. 
#       реализовать с помощью генераторов следующие компоненты:
#      - генерация множества имен файлов
#      - генерация всех строк из всех файлов
#      - фильтрация строк на основе сопоставления с абзацем

import glob, os

os.chdir("/home/super_user/test")

# EDIT 2.1
def files():
    for file in glob.glob("*.txt"):
        yield(file)

# EDIT 2.2        
def strings():
    for file in glob.glob("*.txt"):
        filetext = open(file)
        text = filetext.readlines()
        if text != []:
            yield(text)

# EDIT 2.3 - in future :)      
def search(keyword):
    for line in strings():
        for word in line:
            if keyword in word:
                yield(word.rstrip('\n'))