# Мамонтов Андрей ИУ7-11Б
# База данных в текстовом файле


# Выбрать файл
def choose_file(file_name):
    try:
        f = open(file_name)
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
        f = open(file_name, "w")
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
        print("|{:^129s}|".format("Шахматисты на чемпионате мира 2021 по рапиду и блицу в Варшаве"))
        print("-" * 131)
        print("|{:<25s}|{:<25s}|{:<25s}|{:<25s}|{:<25s}|".format("Имя", "Фамилия", "Год рождения", "Рейтинг в рапид", "Рейтинг в блиц"))
        print("-" * 131)
        with open(db_name) as database:
            for line in database:
                print(line, end="")
        print("-" * 131)
    else:
        print("База данных не инициализирована")


# Добавить запись в БД
def add_record_to_database(db_name):
    if db_name:
        with open(db_name, "a") as database:
            while True:
                field1 = input("Введите имя шахматиста: ")
                if not field1:
                    print("Неверный ввод")
                else:
                    database.write("|" + field1 + " " * (25 - len(field1)))
                    break
            while True:
                field2 = input("Введите фамилию шахматиста: ")
                if not field2:
                    print("Неверный ввод")
                else:
                    database.write("|" + field2 + " " * (25 - len(field2)))
                    break
            while True:
                field3 = input("Введите год рождения шахматиста : ")
                if not field3.isdigit():
                    print("Неверный ввод")
                else:
                    database.write("|" + field3 + " " * (25 - len(field3)))
                    break
            while True:
                field4 = input("Введите рейтинг шахматиста в рапид: ")
                if not field4.isdigit():
                    print("Неверный ввод")
                else:
                    database.write("|" + field4 + " " * (25 - len(field4)))
                    break
            while True:
                field5 = input("Введите рейтинг шахматиста в блиц: ")
                if not field5.isdigit():
                    print("Неверный ввод")
                else:
                    database.write("|" + field5 + " " * (25 - len(field5)) + "|" + "\n")
                    break
    else:
        print("База данных не инициализирована")


# Поиск по одному полю
def search_by_one_field(db_name):
    if db_name:
        field_for_search = input("Введите значение поля: ")
        print("\n", "-" * 131, sep="")
        print("|{:^129s}|".format("Шахматисты на чемпионате мира 2021 по рапиду и блицу в Варшаве"))
        print("-" * 131)
        print("|{:<25s}|{:<25s}|{:<25s}|{:<25s}|{:<25s}|".format("Имя", "Фамилия", "Год рождения", "Рейтинг в рапид",
                                                                 "Рейтинг в блиц"))
        print("-" * 131)
        with open(db_name) as db:
            for line in db:
                if "|" + field_for_search + " " in line or "|" + field_for_search + "|" in line:
                    print(line, end="")
        print("-" * 131)
    else:
        print("База данных не инициализирована")


# Поиск по двум полям
def search_by_two_fields(db_name):
    if db_name:
        field_for_search1 = input("Введите значение 1-го поля: ")
        field_for_search2 = input("Введите значение 2-го поля: ")
        print("\n", "-" * 131, sep="")
        print("|{:^129s}|".format("Шахматисты на чемпионате мира 2021 по рапиду и блицу в Варшаве"))
        print("-" * 131)
        print("|{:<25s}|{:<25s}|{:<25s}|{:<25s}|{:<25s}|".format("Имя", "Фамилия", "Год рождения", "Рейтинг в рапид",
                                                                 "Рейтинг в блиц"))
        print("-" * 131)
        with open(db_name) as database:
            for line in database:
                if ("|" + field_for_search1 + " " in line or "|" + field_for_search1 + "|" in line) and \
                        ("|" + field_for_search2 + " " in line or "|" + field_for_search2 + "|" in line):
                    print(line, end="")
        print("-" * 131)
    else:
        print("База данных не инициализирована")


# Основная программа
file = None
db = None
while True:
    print("""    1. Выбрать существующий файл для работы
    2. Инициализировать базу данных (создать новый файл или перезаписать старый)
    3. Вывести содержимое базы данных
    4. Добавить запись в базу данных
    5. Поиск по одному полю
    6. Поиск по двум полям
    7. Выход из программы""")
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
            search_by_one_field(db)
        case "6":
            search_by_two_fields(db)
        case "7":
            exit()
        case _:
            print("Такой команды нет")
