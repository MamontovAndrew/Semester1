# Мамонтов Андрей ИУ7-11Б
# Транспонирование квадратной матрицы
from lab9_print_matrix import print_matrix
from lab9_input_matrix import matrix_input


# транспонирование матрицы
def transpose_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix[0])):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


# ввод данных
print("Ввод матрицы")
matrix = matrix_input("square")
transpose_matrix(matrix)
print_matrix(matrix)
