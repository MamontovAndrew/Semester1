# Программа, которая позволит с использованием меню обеспечить работу с числовыми массивами
# Мамонтов Андрей ИУ7-11Б

#Проверка на натуральное число
def checking_for_integer(s):
    if s.isdecimal() and s != "0":
        if int(s) > 0:
            return True
    else:
        return False

#Проверка на число
def checking_for_incorrect(s):
    if len(s) == 0:
        return False
    if s[0] == "-":
        s = s[1:]
    if s[len(s) - 1] == "e":
        s += "0"
    if s.count("e") == 1:
        mantissa = s[:s.index("e")]
        exponent = s[s.index("e"):]
        flagmantissa = False
        flagexponent = False
        if exponent[1].isdigit():
            exponent = exponent[1:]
            if exponent.isdecimal():
                flagexponent = True
        else:
            if (exponent.count("+") == 1 or exponent.count("-") == 1) and (exponent[1] == "+" or exponent[1] == "-"):
                exponent = exponent[2:]
                if exponent.isdecimal():
                    flagexponent = True
        if mantissa.count(".") == 1:
            mantissa = mantissa.replace(".", "")
            if mantissa.isdecimal():
                flagmantissa = True
        else:
            if mantissa.isdecimal():
                flagmantissa = True
        if flagmantissa and flagexponent:
            return True
        else:
            return False
    elif s.count("e") == 0:
        if s.count(".") == 1:
            s = s.replace(".", "")
            if s.isdecimal():
                return True
        else:
            if s.isdecimal():
                return True
            else:
                return False
    else:
        return False

#Первые n элементов списка л/р 5
def first_n(n):
    # 1 + x / 1! + 2x / 2! + 3x / 3!.... + nx/n!
    x = 1
    factorial = 1
    if checking_for_integer(n):
        n = int(n)
        arr.append(1.0)
        for i in range(1, n):
            factorial *= i
            current_state = i * x / factorial
            arr.append(current_state)
    else:
        first_n(input("Вы неправильно ввели n, введите его еще раз\n"))

#Очистить и ввести новый список
def clear_and_input():
    arr.clear()
    s = input("Введите длину списка\n")
    while True:
        if not checking_for_integer(s):
            s = input("Длина введена неправильно, введите ее еще раз\n")
        else:
            break
    s = int(s)
    for i in range(s):
        print("Введите {} элемент списка".format(i + 1))
        while True:
            n = input()
            if not checking_for_incorrect(n):
                print("Значение введено неправильно, введите еще раз {} элемент списка".format(i + 1))
            else:
                arr.append(float(n))
                break

#Добавление элемента
def add_element(ind, num):
    while True:
        if checking_for_integer(ind):
            ind = int(ind)
            while True:
                if 0 < ind <= len(arr) + 1:
                    while True:
                        if checking_for_incorrect(num):
                            num = float(num)
                            arr.insert(ind - 1, num)
                            return
                        else:
                            num = input("Вы неправильно ввели число, введите его еще раз\n")
                else:
                    ind = input(
                        "Индекс выходит за границы массива. Если вы хотите добавить элемент в пустой массив введите индекс 1\n")
                break
        else:
            ind = input("Вы неправильно ввели индекс, введите его еще раз\n")

#Удаление элемента
def delete_element(ind):
    while True:
        if checking_for_integer(ind):
            ind = int(ind)
            while True:
                if 0 < ind < len(arr) + 1:
                    if not arr:
                        ind = input("Массив пустой")
                    else:
                        del arr[ind - 1]
                        return
                else:
                    ind = input("Индекс выходит за границы массива.\n")
                    break
        else:
            ind = input("Вы неправильно ввели индекс, введите его еще раз\n")

#Поиск k-ого экстремума
def extremum(k):
    t = 0
    if not checking_for_integer(k):
        k = input("Вы неправильно ввели номер экстремума, введите его еще раз\n")
        return extremum(k)
    else:
        k = int(k)
        if len(arr) == 0:
            print("Массив пустой")
            return
        elif len(arr) == 1:
            if k > 1:
                print("Длина массива 1, а требуется {}-й элемент".format(k))
            else:
                print("1ый экстремум {}".format(arr[0]))
        elif len(arr) == 2:
            if 2 >= k > 0:
                print("{}-й экстремум {}".format(k, arr[k]))
            else:
                print("Длина массива 2, а требуется {}-й элемент".format(k))
        else:
            for i in range(1, len(arr) - 1):
                if arr[i - 1] < arr[i] > arr[i + 1] or arr[i - 1] > arr[i] < arr[i + 1]:
                    t += 1
                    if t == k:
                        print("{}-й экстремум {}".format(k, arr[i]))
                        return
            print("{}-й экстремум не найден в массиве".format(k))

#Наиболее длинная убывающая последовательность целых чётных чисел списка
def longest_decreasing_subsequence_of_even_integers():
    max_arr = []
    at_least_one_oven = False
    even = 0
    for i in range(0, len(arr)):
        current_arr = []
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[j - 1] and arr[j] % 2 == 0 and arr[j - 1] % 2 == 0:
                current_arr.append(arr[j - 1])
                if j == len(arr) - 1:
                    current_arr.append(arr[j])
            else:
                if arr[j] % 2 == 0:
                    at_least_one_oven = True
                    even = arr[j]
                if current_arr:
                    current_arr.append(arr[j - 1])
                break
        max_arr = max_arr if len(max_arr) > len(current_arr) else current_arr
    if not max_arr:
        if at_least_one_oven:
            print("Найдена последовательность длиной 1 - число ", even)
        else:
            print("Последовательность не найдена")
    else:
        print("Наиболее длинная убывающая последовательность целых чётных чисел списка: ", *max_arr)

#Выбор опций
arr = []
while True:
    print('''Введите цифру опции, которую вы хотите использовать
    1. Проинициализировать список первыми N элементами заданного в л/р 5 ряда
    2. Очистить список и ввести его с клавиатуры
    3. Добавить элемент в произвольное место списка
    4. Удалить произвольный элемент из списка (по номеру)
    5. Очистить список
    6. Найти значение K-го экстремума в списке
    7. Найти наиболее длинную убывающую последовательность целых чётных чисел''')
    option = input()
    match option:
        case '1':
            n = input("Введите N\n")
            arr.clear()
            first_n(n)
            print("Ваш массив: ", *arr)
        case '2':
            clear_and_input()
            print("Ваш массив: ", *arr)
        case '3':
            ind = input("Введите индекс\n")
            num = input("Введите число\n")
            add_element(ind, num)
            print("Ваш массив: ", *arr)
        case '4':
            ind = input("Введите индекс\n")
            delete_element(ind)
            print("Ваш массив: ", *arr)
        case '5':
            arr.clear()
            print("Ваш массив: ", *arr)
        case '6':
            k = input("Введите K\n")
            extremum(k)
            print("Ваш массив: ", *arr)
        case '7':
            longest_decreasing_subsequence_of_even_integers()
            print("Ваш массив: ", *arr)
        case _:
            print("Такой команды нет")
