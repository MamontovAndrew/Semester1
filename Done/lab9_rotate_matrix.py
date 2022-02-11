# Мамонтов Андрей ИУ7-11Б
# Поворот квадратной матрицы на 90 градусов по часовой стрелке, затем на 90 градусов против часовой стрелки.
# Вывести промежуточную и итоговую матрицу.
from lab9_input_matrix import matrix_input
from lab9_print_matrix import print_matrix


# поворот матрицы
def rotate_matrix(matrix, mode):
    if mode == "left":
        return list(zip(*matrix))[::-1]
    else:
        return list(zip(*matrix[::-1]))


# ввод данных
matrix = matrix_input("square")
print_matrix(matrix)
print("""В какую сторону вы хотите повернуть матрицу?
1. По часовой
2. Против часовой
3. Выйти""")
# выбор варианта поворота
while True:
    s = input()
    match s:
        case "1":
            matrix = rotate_matrix(matrix, "right")
            print_matrix(matrix)
        case "2":
            matrix = rotate_matrix(matrix, "left")
            print_matrix(matrix)
        case "3":
            exit()
        case _:
            print("Вы неправильно ввели режим")
