# Мамонтов Андрей ИУ7-11Б
# Задана матрица D и массив I, содержащий номера строк, для которых
# необходимо определить максимальный элемент. Значения максимальных
# элементов запомнить в массиве R. Определить среднее арифметическое
# вычисленных максимальных значений. Напечатать матрицу D, массивы I и R, среднее арифметическое значение.
from lab9_input_matrix import matrix_input
from lab9_list_input import list_input
from lab9_print_matrix import print_matrix


def print_matrix_D_I_R(d, i_arr):
    # заполнение массива r
    r = []
    for i in i_arr:
        r.append(max(d[int(i) - 1]))
    average = 0
    if r:
        average = sum(r) / len(r)
    # вывод матрицы и массивов i, r
    print("Матрица d")
    print_matrix(d)
    print("Массив i")
    print("".join("{:^15d}".format(int(i_arr[i])) for i in range(len(i_arr))))
    print("Массив r")
    print("".join("{:^15f}".format(r[i]) for i in range(len(r))))
    print("Среднее арифметическое значение")
    print(average)


# ввод матрицы и массива
print("Ввод матрицы d")
d = matrix_input()
print("Ввод массива i")
while True:
    i_arr = list_input()
    flag = True
    for i in i_arr:
        if i < 1 or i > len(d):
            flag = False
    if flag:
        break
    else:
        print("Неправильный индекс в массиве i")
print_matrix_D_I_R(d, i_arr)
