# Мамонтов Андрей ИУ7-11Б
# Даны массивы D и F. Сформировать матрицу A по формуле ajk = sin(dj+fk).
# Определить среднее арифметическое положительных чисел каждой строки
# матрицы и количество элементов, меньших среднего арифметического.
# Результаты записать соответственно в массивы AV и L. Напечатать матрицу A в
# виде матрицы и рядом столбцы AV и L.
from math import sin
from lab9_list_input import list_input


def print_matrix_AV_L(d, f):
    # создание матрицы и массивов
    matrix = []
    n = len(d)
    m = len(f)
    positive = []
    for i in range(n):
        matrix.append([])
        positive.append([])
        for j in range(m):
            matrix[i].append(sin(d[i] + f[j]))
            if sin(d[i] + f[j]) > 0:
                positive[i].append(sin(d[i] + f[j]))
    print(" " * 8 * m + "D" + " " * 8 * m + "AV" + " " * 8 + "L")
    # вывод
    for i in range(n):
        l = 0
        print("".join("{:^15f}".format(matrix[i][j]) for j in range(m)), end=" ")
        if len(positive[i]) != 0:
            av = sum(positive[i]) / len(positive[i])
            for j in range(m):
                if matrix[i][j] < av:
                    l += 1
            print("{:^15f}".format(av), end=" ")
        else:
            av = "_"
            l = "_"
            print("{:^15}".format(av), end=" ")
        print(l)


# Ввод матрицы
print("Ввод массива d")
d = list_input()
print("Ввод массива f")
f = list_input()
print_matrix_AV_L(d, f)
