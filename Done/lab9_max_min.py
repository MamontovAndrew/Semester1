# Мамонтов Андрей ИУ7-11Б
# Найти максимальное значение над главной диагональю и минимальное - под побочной диагональю.
from lab9_input_matrix import matrix_input
from lab9_print_matrix import print_matrix


def max_min_matrix(matrix):
    # Подсчет значений
    maximum = min(matrix[0])
    minimum = max(matrix[0])
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix[0])):
            if matrix[i][j] > maximum:
                maximum = matrix[i][j]
    for i in range(len(matrix)):
        for j in range(len(matrix[0]) - len(matrix) + i, len(matrix[0])):
            if matrix[i][j] < minimum:
                minimum = matrix[i][j]
    print("Максимальное значение над главной диагональю: ", maximum)
    print("Минимальное значение под побочной диагональю: ", minimum)


# Ввод матрицы
print("Ввод матрицы")
matrix = matrix_input("square")
max_min_matrix(matrix)
print_matrix(matrix)
