# Мамонтов Андрей ИУ7-11Б
# Сформировать матрицу C путём построчного перемножения матриц A и B
# одинаковой размерности (элементы в i-й строке матрицы A умножаются на
# соответствующие элементы в i-й строке матрицы B), потом сложить все
# элементы в столбцах матрицы C и записать их в массив V.
from lab9_input_matrix import matrix_input
from lab9_print_matrix import print_matrix


def A_B_C_V(a, b):
    # Создание матрицы C
    c = []
    for i in range(len(a)):
        c.append([])
        for j in range(len(a[0])):
            c[i].append(a[i][j] * b[i][j])
    # Создание массива V
    v = []
    for j in range(len(c[0])):
        v.append(sum(c[i][j] for i in range(len(c))))
    # Выод матрицы и массива
    print("Матрица c")
    print_matrix(c)
    print("Массив v")
    print("".join("{:^15f}".format(v[i]) for i in range(len(v))))


# Ввод матриц
a = matrix_input()
b = matrix_input()
print("Исходный массив a")
print_matrix(a)
print("Исходный массив b")
print_matrix(b)
A_B_C_V(a, b)
