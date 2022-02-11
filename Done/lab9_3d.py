# Мамонтов Андрей ИУ7-11Б
# Ввести трёхмерный массив (массив матриц размера X*Y*Z), вывести из него i-й срез по второму индексу.
from Done.lab9_number_check import checking_for_integer


def i_slice_3d():
    # ввод размеров трёхмерной матрицы
    while True:
        s = input("Введите X: ")
        if checking_for_integer(s, "natural"):
            x = int(s)
            break
        else:
            print("Вы неправильно ввели n, n - натуральное число")
    while True:
        s = input("Введите Y: ")
        if checking_for_integer(s, "natural"):
            y = int(s)
            break
        else:
            print("Вы неправильно ввели n, n - натуральное число")
    while True:
        s = input("Введите Z: ")
        if checking_for_integer(s, "natural"):
            z = int(s)
            break
        else:
            print("Вы неправильно ввели n, n - натуральное число")
    # Ввод номера среза
    while True:
        s = input("Введите номер среза: ")
        if checking_for_integer(s, "natural"):
            i_slice = int(s)
            if i_slice < 1 or i_slice > y:
                print("Индекс в интервале: {} - {}".format(1, y))
            else:
                break
        else:
            print("Вы неправильно ввели n, n - натуральное число")
    # Ввод трёхмерного массива
    arr = []
    for i in range(x):
        matrix = []
        for j in range(y):
            matrix.append([])
            for k in range(z):
                print("Введите элемент с координатами {} {} {}: ".format(i, j, k))
                matrix[j].append(float(input()))
        arr.append(matrix)
    # Вывод среза
    print("i-ый срез по второму индексу:")
    for i in range(x):
        print("".join("{:^15f}".format(arr[i][i_slice - 1][k]) for k in range(z)))


print("Ввод трёхмерного массива")
i_slice_3d()
