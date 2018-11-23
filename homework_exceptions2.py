documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
    {"type": "id", "number": "123456"}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}


def people(command):  # команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;
    doc_number = str(input('Введите номер документа, чтобы узнать имя:'))
    for data in command:
        if doc_number == data['number']:
            print(data['name'])
        else:
            print('Документа не существует')


command = input('Доступные команды: p, l, s, a, n \n Введите команду')


def docs_list(
        command):  # команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";
    for data in command:
        print(data['type'], data['number'], data['name'])


def shelf(command):  # команда, которая спросит номер документа и выведет номер полки, на которой он находится;
    doc_number = str(input('Введите номер документа, чтобы узнать полку:'))
    for key, value in command.items():
        if doc_number in value:
            print(key)
        else:
            print('Документа нет на полке')


def add_doc(
        command):  # команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться.
    type_input = input(str("Введите тип документа: "))
    number_input = input(str("Введите номер документа: "))
    name_input = input(str("Введите имя и фамилию: "))
    shelf_input = input(str("На какую полку положить?"))
    documents.append({"type": type_input, "number": number_input, "name": name_input})
    print(documents)
    if shelf_input in command:
        directories[shelf_input].append(number_input)
        print(directories)
    else:
        directories[shelf_input] = [number_input]
        print(directories)


def names_list(
        command):  # команда для нового домашнего задания по исключениям: выведет всех по ключу 'name', а если 'name' нет, то выведет предупреждение вместо KeyError
    try:
        for data in command:
            print(data['name'])
    except KeyError:
        print('Для документа не указано имя')


if command == 'p':
    people(documents)
elif command == 'l':
    print('Список всех документов')
    docs_list(documents)
elif command == 's':
    shelf(directories)
elif command == 'a':
    add_doc(directories)
elif command == 'n':
    print('Список всех имен')
    names_list(documents)
else:
    print('Команда не существует')


