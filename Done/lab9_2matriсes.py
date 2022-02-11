# Мамонтов Андрей ИУ7-11Б
# Подсчитать в каждой строке матрицы D количество элементов, превышающих
# суммы элементов соответствующих строк матрицы Z. Разместить эти
# количества в массиве G, умножить матрицу D на максимальный элемент
# массива G. Напечатать матрицу D до и после преобразования, а также массив G.
from lab9_input_matrix import matrix_input
from lab9_print_matrix import print_matrix


def print_matrix_D_G(d, z):
    # заполнение массива g
    g = []
    for i in range(len(min(d, z))):
        sum_of_elements = sum(z[i])
        t = 0
        for j in range(len(d[0])):
            if d[i][j] > sum_of_elements:
                t += 1
        g.append(t)
    maximum = max(g)
    # умножение матрицы
    for i in range(len(d)):
        for j in range(len(d[0])):
            d[i][j] *= maximum
    # вывод матрицы и массива
    print("Конечная матрица d")
    print_matrix(d)
    print("Массив g")
    print(*g)


# ввод матриц
print("Ввод матрицы d")
d = matrix_input()
print("Исходная матрица d")
print_matrix(d)
print("Ввод матрицы z")
z = matrix_input()
print_matrix_D_G(d, z)
