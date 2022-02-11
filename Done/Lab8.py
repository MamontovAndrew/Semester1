# Мамонтов Андрей ИУ7-11Б
# Программа для работы с целочисленными матрицами

# Проверка на простое число
def isPrime(a):
    if a % 2 == 0:
        return a == 2
    divider = 3
    while divider * divider <= a and a % divider != 0:
        divider += 2
    return divider * divider > a


# Проверка на целое/натуральное число
def checking_for_integer(s, mode="integer"):
    if mode == "natural":
        if s.isdecimal():
            if int(s) > 0:
                return True
            else:
                return False
        else:
            return False
    else:
        if len(s) >= 2:
            if s[0] == "-":
                s = s[1:]
        if s.isdecimal():
            return True
        else:
            return False


# Ввод матрицы
def matrix_input():
    global n, m, matrix
    while True:
        s = input("Введите n\n")
        if checking_for_integer(s, "natural"):
            n = int(s)
            break
        else:
            print("Вы неправильно ввели n, n - натуральное число")
    while True:
        s = input("Введите m\n")
        if checking_for_integer(s, "natural"):
            m = int(s)
            break
        else:
            print("Вы неправильно ввели m, m - натуральное число")
    matrix = [[0] * m for i in range(n)]
    for i in range(n):
        for j in range(m):
            while True:
                s = input("Введите элемент {}-ой/ей строки {}-ого/его столбца\n".format(i + 1, j + 1))
                if checking_for_integer(s):
                    matrix[i][j] = int(s)
                    break
                else:
                    print("Введённое число не целое")


# Добавление строки
def append_string(mode="smart_way"):
    global n, m, matrix
    while True:
        s = input("Введите номер новой строки\n")
        if checking_for_integer(s, "natural"):
            ins = int(s)
            if ins < 1 or ins > n + 1:
                print("Вы неправильно ввели номер строки, номер в диапазоне {}-{}".format(1, n + 1))
            else:
                n += 1
                break
        else:
            print("Вы неправильно ввели номер строки, это натуральное число")
    if n == 1:
        print("Вы добавляете строчку в пустой массив")
        while True:
            s = input("Введите m\n")
            if checking_for_integer(s, "natural"):
                m = int(s)
                break
            else:
                print("Вы неправильно ввели m, m - натуральное число")
    new_string = []
    for j in range(m):
        while True:
            s = input("Введите {}-ой/ый/ий элемент новой строки\n".format(j + 1))
            if checking_for_integer(s):
                new_string.append(int(s))
                break
            else:
                print("Введённое число не целое")
    if mode == "algorithmic_way":
        matrix.append([])
        for i in range(n - 1, ins - 1, -1):
            matrix[i] = matrix[i - 1]
        matrix[ins - 1] = new_string
    else:
        matrix.insert(ins - 1, new_string)


# Удаление строки
def delete_string(mode="smart_way"):
    global n, m, matrix
    while True:
        s = input("Введите номер строки, которую вы хотите удалить\n")
        if checking_for_integer(s, "natural"):
            del_ind = int(s)
            if n == 0:
                print("Массив пустой")
                return
            elif del_ind < 1 or del_ind > n + 1:
                print("Вы неправильно ввели номер строки, номер в диапазоне {}-{}".format(1, n))
            else:
                n -= 1
                break
        else:
            print("Вы неправильно ввели номер строки, это натуральное число")
    if mode == "algorithmic_way":
        for i in range(del_ind - 1, n - 1):
            matrix[i] = matrix[i + 1]
        del matrix[n - 1]
    else:
        matrix.remove(matrix[del_ind - 1])


# Добавление столбца
def append_column(mode="smart_way"):
    global n, m, matrix
    while True:
        s = input("Введите номер нового столбца\n")
        if checking_for_integer(s, "natural"):
            ins = int(s)
            if ins < 1 or ins > m + 1:
                print("Вы неправильно ввели номер столбца, номер в диапазоне {}-{}".format(1, n + 1))
            else:
                m += 1
                break
        else:
            print("Вы неправильно ввели номер столбца, это натуральное число")
    if m == 1:
        print("Вы добавляете столбец в пустой массив")
        while True:
            s = input("Введите n\n")
            if checking_for_integer(s, "natural"):
                n = int(s)
                break
            else:
                print("Вы неправильно ввели n, n - натуральное число")
    new_column = []
    for i in range(n):
        while True:
            s = input("Введите {}-ой/ый/ий элемент нового столбца\n".format(i + 1))
            if checking_for_integer(s):
                new_column.append(int(s))
                break
            else:
                print("Введённое число не целое")
    if mode == "algorithmic_way":
        for i in range(n):
            matrix[i].append(0)
            for j in range(m - 1, ins - 1, -1):
                matrix[i][j] = matrix[i][j - 1]
            matrix[i][ins - 1] = new_column[i]
    else:
        for i in range(n):
            matrix[i].insert(ins - 1, new_column[i])


# Удаление столбца
def delete_column(mode="smart_way"):
    global n, m, matrix
    while True:
        s = input("Введите номер столбца, который вы хотите удалить\n")
        if checking_for_integer(s, "natural"):
            del_ind = int(s)
            if m == 0:
                print("Массив пустой")
                return
            elif del_ind < 1 or del_ind > m:
                print("Вы неправильно ввели номер столбца, номер в диапазоне {}-{}".format(1, m))
            else:
                m -= 1
                break
        else:
            print("Вы неправильно ввели номер столбца, это натуральное число")
    if mode == "algorithmic_way":
        for i in range(n):
            for j in range(del_ind - 1, m - 1):
                matrix[i][j] = matrix[i][j + 1]
            del matrix[i][m - 1]
    else:
        for i in range(n):
            matrix[i].remove(matrix[i][del_ind - 1])


# Назождение строки с наибольшим количеством четных элементов
def find_the_string_that_has_the_most_even_elements():
    global n, m, matrix
    if n == 0:
        print("Недостаточно строк в матрице")
        return
    max_even = 0
    a = []
    for i in range(n):
        t = 0
        for j in range(m):
            if matrix[i][j] % 2 == 0:
                t += 1
        if t > max_even:
            max_even = t
            a = matrix[i]
    if max_even == 0:
        print("Нет чётных элементов ни в одной строке")
    else:
        print("В этой строке наибольшее количество чётных элементов - ", max_even)
        print("".join("{:^15d}".format(a[j]) for j in range(m)))


# Поменять местами строки с наибольшим и наименьшим количеством отрицательных элементов
def swap_lines_with_the_highest_and_lowest_count_of_negative_elements():
    global n, m, matrix
    if n < 2:
        print("Недостаточно строк в матрице")
        return
    lowest_count = m
    biggest_count = 0
    lowest_ind = 0
    biggest_ind = 0
    for i in range(n):
        t = 0
        for j in range(m):
            if matrix[i][j] < 0:
                t += 1
        if t > biggest_count:
            biggest_count = t
            biggest_ind = i
        if t < lowest_count:
            lowest_count = t
            lowest_ind = i
    matrix[lowest_ind], matrix[biggest_ind] = matrix[biggest_ind], matrix[lowest_ind]
    print("Поменяны местами строки:")
    print("".join("{:^15d}".format(matrix[lowest_ind][j]) for j in range(m)))
    print("".join("{:^15d}".format(matrix[biggest_ind][j]) for j in range(m)))


# Нахождение столбца с наибольшим количеством простых чисел
def find_the_column_with_the_most_primes():
    global n, m, matrix
    if m == 0:
        print("Недостаточно столбцов в массиве")
    most_prime = 0
    column_with_most_prime = []
    for j in range(m):
        t = 0
        for i in range(n):
            if isPrime(matrix[i][j]):
                t += 1
        if t > most_prime:
            most_prime = t
            column_with_most_prime = [matrix[i][j] for i in range(n)]
    if most_prime == 0:
        print("Нет ни одного простого числа")
        return
    print("Искомый столбец")
    for i in column_with_most_prime:
        print("{:^15d}".format(i))


# Поменять местами столбцы с наибольшей и наименьшей суммой элементов
def swap_the_columns_with_the_maximum_and_minimum_sum_of_elements():
    global n, m, matrix
    if m < 2:
        print("Недостаточно столбцов в массиве")
    max_sum = 0
    min_sum = sum([matrix[i][0] for i in range(n)])
    max_ind = 0
    min_ind = 0
    for j in range(m):
        t = 0
        for i in range(n):
            t += matrix[i][j]
        if t > max_sum:
            max_sum = t
            max_ind = j
        if t <= min_sum:
            min_sum = t
            min_ind = j
    print("Поменяли местами столбцы")
    for i in range(n):
        print("{:^15d}{:^15d}".format(matrix[i][min_ind], matrix[i][max_ind]))
        matrix[i][min_ind], matrix[i][max_ind] = matrix[i][max_ind], matrix[i][min_ind]


# Вывод матрицы
def print_matrix():
    for i in range(n):
        print("".join("{:^15d}".format(matrix[i][j]) for j in range(m)))


# Основная часть программы
n = 0
m = 0
matrix = []
while True:
    print('''Выберите функцию для работы с целочисленными матрицами:
    1. Ввести матрицу
    2. Добавить строку
    3. Удалить строку
    4. Добавить столбец
    5. Удалить столбец
    6. Найти строку, имеющую наибольшее количество чётных элементов
    7. Переставить местами строки с наибольшим и наименьшим количеством
    отрицательных элементов
    8. Найти столбец, имеющий наибольшее количество простых чисел
    9. Переставить местами столбцы с максимальной и минимальной суммой
    элементов
    10. Вывести текущую матрицу''')
    option = input()
    match option:
        case "1":
            matrix_input()
        case "2":
            print('''Каким способом вставить строку?
            1. Средствами Python
            2. Алгоритмически''')
            ins_option = input()
            match ins_option:
                case "1":
                    append_string()
                case "2":
                    append_string("algorithmic_way")
                case _:
                    print("Такого варианта нет")
        case "3":
            print('''Каким способом удалить строку?
            1. Средствами Python
            2. Алгоритмически''')
            ins_option = input()
            match ins_option:
                case "1":
                    delete_string()
                case "2":
                    delete_string("algorithmic_way")
                case _:
                    print("Такого варианта нет")
        case "4":
            print('''Каким способом вставить столбец?
            1. Средствами Python
            2. Алгоритмически''')
            ins_option = input()
            match ins_option:
                case "1":
                    append_column()
                case "2":
                    append_column("algorithmic_way")
                case _:
                    print("Такого варианта нет")
        case "5":
            print('''Каким способом удалить столбец?
                        1. Средствами Python
                        2. Алгоритмически''')
            ins_option = input()
            match ins_option:
                case "1":
                    delete_column()
                case "2":
                    delete_column("algorithmic_way")
                case _:
                    print("Такого варианта нет")
        case "6":
            find_the_string_that_has_the_most_even_elements()
        case "7":
            swap_lines_with_the_highest_and_lowest_count_of_negative_elements()
        case "8":
            find_the_column_with_the_most_primes()
        case "9":
            swap_the_columns_with_the_maximum_and_minimum_sum_of_elements()
        case "10":
            print_matrix()
        case _:
            print("Такой команды нет")
