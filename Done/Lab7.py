# Программа, которая позволит с использованием меню обеспечить работу с текстовыми массивами
# Мамонтов Андрей ИУ7-11Б

# Вывод элементов списка
def print_list():
    print("Ваш список")
    for i in arr:
        print(i)

# Проверка на натуральное число
def checking_for_integer(s):
    if s.isdecimal():
        if int(s) > 0:
            return True
    else:
        return False


# Очистить и ввести новый список
def clear_and_input():
    n = input("Введите количество элементов списка\n")
    while True:
        if checking_for_integer(n):
            n = int(n)
            arr = [""] * n
            for i in range(n):
                arr[i] = input("Введите {} элемент списка\n".format(i + 1))
            return arr
        else:
            n = input("Длина введена неправильно, введите ее еще раз\n")


# Добавление элемента
def add_element():
    while True:
        ind = input("Введите индекс\n")
        if checking_for_integer(ind):
            ind = int(ind)
            if 1 <= ind <= len(arr) + 1:
                arr.append("")
                elem = input("Введите элемент\n")
                for i in range(len(arr) - 1, ind - 1, -1):
                    arr[i] = arr[i - 1]
                arr[ind - 1] = elem
                return arr
            else:
                print("Неправильный индекс, для текущего массива он может быть в диапазоне {}-{}".format(1, len(arr) + 1))
        else:
            print("Индекс должен быть целым числом")


# Удаление элемента
def delete_element():
    while True:
        ind = input("Введите индекс\n")
        if checking_for_integer(ind):
            ind = int(ind)
            if 1 <= ind <= len(arr):
                for i in range(ind - 1, len(arr) - 1):
                    arr[i] = arr[i + 1]
                del arr[len(arr) - 1]
                return arr
            else:
                print("Неправильный индекс, для текущего массива он может быть в диапазоне {}-{}".format(1, len(arr)))
        else:
            print("Индекс должен быть целым числом")


# Поиск элемента с наибольшим числом подряд идущих цифр
def find_element_with_the_largest_number_of_consecutive_digits():
    max_num_of_digits = 0
    element_with_the_largest_number_of_consecutive_digits = ""
    for i in arr:
        t = 0
        for j in i:
            if j.isdigit():
                t += 1
            else:
                if t > max_num_of_digits:
                    max_num_of_digits = t
                    element_with_the_largest_number_of_consecutive_digits = i
                t = 0
        if t > max_num_of_digits:
            max_num_of_digits = t
            t = 0
            element_with_the_largest_number_of_consecutive_digits = i
    return element_with_the_largest_number_of_consecutive_digits


# Замена всех строчных гласных английских букв элемента на заглавные
def change_all_lowcase_vowels_to_uppercase():
    vowels = ["a", "o", "u", "i", "e", "y"]
    while True:
        ind = input("Введите индекс\n")
        if checking_for_integer(ind):
            ind = int(ind)
            if 1 <= ind < len(arr) + 1:
                arr[ind - 1] = list(arr[ind - 1])
                for i in range(len(arr[ind - 1])):
                    if arr[ind - 1][i] in vowels:
                        arr[ind - 1][i] = chr(ord(arr[ind - 1][i]) - 32)
                arr[ind - 1] = ''.join(arr[ind - 1])
                return arr[ind - 1]
            else:
                print("Неправильный индекс, для текущего массива он может быть в диапазоне {}-{}".format(1, len(arr)))
        else:
            print("Индекс должен быть целым числом")


arr = []
while True:
    print('''Введите цифру опции, которую вы хотите использовать
    1. Очистить список и ввести его с клавиатуры
    2. Добавить элемент в произвольное место списка
    3. Удалить произвольный элемент из списка (по номеру)
    4. Очистить список
    5. Поиск элемента с наибольшим числом подряд идущих цифр
    6. Замена всех строчных гласных английских букв элемента на заглавные''')
    option = input()
    match option:
        case '1':
            arr = clear_and_input()
            print_list()
        case '2':
            arr = add_element()
            print_list()
        case '3':
            arr = delete_element()
            print_list()
        case '4':
            arr.clear()
            print_list()
        case '5':
            print("Элемент с наибольшим числом подряд идущих цифр: ",
                  find_element_with_the_largest_number_of_consecutive_digits())
        case '6':
            print("Элемент с заменой всех строчных гласных английских букв на заглавные: ",
                  change_all_lowcase_vowels_to_uppercase())
        case _:
            print("Такой команды нет")
