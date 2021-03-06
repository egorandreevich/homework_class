# Задание
# мне нужно отыскать файл среди десятков других
# я знаю некоторые части этого файла (на память или из другого источника)
# я ищу только среди .sql файлов
# 1. программа ожидает строку, которую будет искать (input())
# после того, как строка введена, программа ищет её во всех файлах
# выводит список найденных файлов построчно
# выводит количество найденных файлов
# 2. снова ожидает ввод
# поиск происходит только среди найденных на этапе 1
# 3. снова ожидает ввод
# ...
# Выход из программы программировать не нужно.
# Достаточно принудительно остановить, для этого можете нажать Ctrl + C

# Пример на настоящих данных

# python3 find_procedure.py
# Введите строку: INSERT
# ... большой список файлов ...
# Всего: 301
# Введите строку: APPLICATION_SETUP
# ... большой список файлов ...
# Всего: 26
# Введите строку: A400M
# ... большой список файлов ...
# Всего: 17
# Введите строку: 0.0
# Migrations/000_PSE_Application_setup.sql
# Migrations/100_1-32_PSE_Application_setup.sql
# Всего: 2
# Введите строку: 2.0
# Migrations/000_PSE_Application_setup.sql
# Всего: 1

# не забываем организовывать собственный код в функции

import os
import glob

migrations = 'Migrations'
current_dir = os.path.dirname(os.path.abspath(__file__))

if __name__ == '__main__':
    # ваша логика

    os.chdir(migrations)
    def sql_files_search(): #поиск по .sql файлам в папке
        search_list = os.listdir('./')
        search_list_2 = []
        indicator = 0
        while True:
            search = str(input())
            for file in search_list:
                if '.sql' in file: #только по .sql файлам
                    f = open(file, 'r')
                    if search in f.read():
                        print(file)
                        indicator += 1
                        search_list_2.append(file)
                search_list = search_list_2 #переназначаю список
            print('Найдено {} файла(ов)'.format(indicator))
            search_list_2 = []
            indicator = 0
            # print(search_list)

    sql_files_search() #запускаю функцию
