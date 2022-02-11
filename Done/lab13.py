import struct
from struct import *


# Выбрать файл
def choose_file(file_name):
    try:
        f = open(file_name, "rb")
    except FileNotFoundError:
        print("Такого файла нет")
        return None
    except OSError:
        print("Ошибочный синтаксис поиска файла")
        return None
    else:
        f.close()
        return file_name


# Создание файла
def create_file(file_name):
    try:
        f = open(file_name, "wb")
    except OSError:
        print("Неверный синтаксис создания файла")
        return None
    else:
        f.close()
        return file_name


# Инициализировать базу данных
def initialize_database(file):
    while True:
        if not file:
            print("Файл ещё не выбран. Создайте новый файл")
            new_file = input("Введите название нового файла: ")
            new_file = create_file(new_file)
            if new_file:
                return new_file
        else:
            creation = input("Файл уже существует, уверены, что хотите его перезаписать? Y/N: ")
            if creation.lower() == "y":
                new_file = create_file(file)
                print("Файл был перезаписан")
                if new_file:
                    return new_file
            elif creation.lower() == "n":
                return file


# Вывести БД
def print_data_from_database(db_name):
    if db_name:
        print("\n", "-" * 131, sep="")
        print("|{:^129s}|".format("Шахматисты на турнире Tata Steel Chess в Вейк-ан-Зее"))
        print("-" * 131)
        print("|{:<25s}|{:<25s}|{:<25s}|{:<25s}|{:<25s}|".format("Имя", "Фамилия", "Год рождения", "Рейтинг в рапид",
                                                                 "Рейтинг в блиц"))
        print("-" * 131)
        with open(db_name, "rb") as database:
            data = bytes()
            for line in database:
                data += line
            for i in range(0, len(data), 62):
                name, surname, year, rapid, blitz = struct.unpack("=25s25siii", data[i:i+62])
                name = name.decode().replace("\x00", "")
                surname = surname.decode().replace("\x00", "")
                print("|{:<25s}|{:<25s}|{:<25d}|{:<25d}|{:<25d}|".format(str(name), str(surname), year, rapid, blitz))
        print("-" * 131)
    else:
        print("База данных не инициализирована")


# Добавить запись в БД
def add_record_to_database(db_name):
    if db_name:
        with open(db_name, "ab") as database:
            while True:
                field1 = input("Введите имя шахматиста (не длиннее 25 символов): ")
                if not field1 or len(field1) > 25:
                    print("Неверный ввод")
                else:
                    break
            while True:
                field2 = input("Введите фамилию шахматиста(не длиннее 25 символов): ")
                if not field2 or len(field2) > 25:
                    print("Неверный ввод")
                else:
                    break
            while True:
                field3 = input("Введите год рождения шахматиста: ")
                if not field3.isdigit():
                    print("Неверный ввод")
                else:
                    break
            while True:
                field4 = input("Введите рейтинг шахматиста в рапид: ")
                if not field4.isdigit():
                    print("Неверный ввод")
                else:
                    break
            while True:
                field5 = input("Введите рейтинг шахматиста в блиц: ")
                if not field5.isdigit():
                    print("Неверный ввод")
                else:
                    break
            database.write(struct.pack("=25s25siii", field1.encode("utf-8"), field2.encode("utf-8"), int(field3), int(field4), int(field5)))
    else:
        print("База данных не инициализирована")


def delete_record_by_number(db_name):
    if db_name:
        data = bytes()
        with open(db_name, "rb") as database:
            for line in database:
                data += line
        records = len(data)//62
        if records == 1:
            with open(db_name, "wb") as database:
                database.truncate(0)
        while True:
            delete_position = int(input(f"Введите номер записи, которую необходимо удалить (от 1 до {records}): "))
            if delete_position <= records and delete_position > 0:
                break
            else:
                print("Некорректный номер")
        data_lines = []
        for i in range(0, len(data), 62):
            data_lines.append(data[i:i + 62])
        for i in range(delete_position, records):
            data_lines[i], data_lines[i - 1] = data_lines[i - 1], data_lines[i]
        with open(db_name, "wb") as database:
            for i in data_lines:
                database.write(i)
            database.truncate(len(data) - 62)
# Поиск по одному полю
def search_by_one_field(db_name):
    if db_name:
        field_for_search = input("Введите значение поля: ")
        print("\n", "-" * 131, sep="")
        print("|{:^129s}|".format("Шахматисты на турнире Tata Steel Chess в Вейк-ан-Зее"))
        print("-" * 131)
        print("|{:<25s}|{:<25s}|{:<25s}|{:<25s}|{:<25s}|".format("Имя", "Фамилия", "Год рождения", "Рейтинг в рапид",
                                                                 "Рейтинг в блиц"))
        print("-" * 131)
        with open(db_name, "rb") as database:
            data = bytes()
            for line in database:
                data += line
            for i in range(0, len(data), 62):
                print(len(data[i:i + 62]))
                print(data[i:i + 62])
                name, surname, year, rapid, blitz = struct.unpack("<25s25siii", data[i:i + 62])
                name = name.decode().replace("\x00", "")
                surname = surname.decode().replace("\x00", "")
                one_record = [name, surname, str(year), str(rapid), str(blitz)]
                if field_for_search in one_record:
                    print("|{:<25s}|{:<25s}|{:<25d}|{:<25d}|{:<25d}|".format(str(name), str(surname), year, rapid, blitz))
        print("-" * 131)
    else:
        print("База данных не инициализирована")


# Поиск по двум полям
def search_by_two_fields(db_name):
    if db_name:
        field_for_search1 = input("Введите значение 1-го поля: ")
        field_for_search2 = input("Введите значение 2-го поля: ")
        print("\n", "-" * 131, sep="")
        print("|{:^129s}|".format("Шахматисты на турнире Tata Steel Chess в Вейк-ан-Зее"))
        print("-" * 131)
        print("|{:<25s}|{:<25s}|{:<25s}|{:<25s}|{:<25s}|".format("Имя", "Фамилия", "Год рождения", "Рейтинг в рапид",
                                                                 "Рейтинг в блиц"))
        print("-" * 131)
        with open(db_name, "rb") as database:
            data = bytes()
            for line in database:
                data += line
            for i in range(0, len(data), 62):
                name, surname, year, rapid, blitz = struct.unpack("<25s25siii", data[i:i + 62])
                name = name.decode().replace("\x00", "")
                surname = surname.decode().replace("\x00", "")
                one_record = [name, surname, str(year), str(rapid), str(blitz)]
                if field_for_search1 in one_record and field_for_search2 in one_record and field_for_search1 != field_for_search2:
                    print("|{:<25s}|{:<25s}|{:<25d}|{:<25d}|{:<25d}|".format(str(name), str(surname), year, rapid, blitz))
        print("-" * 131)
    else:
        print("База данных не инициализирована")


file = None
db = None
while True:
    print("""    1. Выбрать существующий файл для работы
    2. Инициализировать базу данных (создать новый файл или перезаписать старый)
    3. Вывести содержимое базы данных
    4. Добавить запись в базу данных
    5. Удалить запись из базы данных
    6. Поиск по одному полю
    7. Поиск по двум полям
    8. Выход из программы""")
    option = input("    Введите номер команды: ")
    match option:
        case "1":
            file_name = input("Выберите имя файла для работы: ")
            file = choose_file(file_name)
            db = file
        case "2":
            db = initialize_database(file)
        case "3":
            print_data_from_database(db)
        case "4":
            add_record_to_database(db)
        case "5":
            delete_record_by_number(db)
        case "6":
            search_by_one_field(db)
        case "7":
            search_by_two_fields(db)
        case "8":
            exit()
        case _:
            print("Такой команды нет")
