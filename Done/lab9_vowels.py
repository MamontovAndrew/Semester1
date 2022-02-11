# Мамонтов Андрей ИУ7-11Б
# Дана матрица символов. Заменить в ней все гласные английские буквы на точки.
from Done.lab9_number_check import checking_for_integer


# Замена гласных английских букв на точки
def change_vowels_to_dots(matrix):
    vowels = ["A", "E", "I", "O", "U", "Y", "a", "e", "i", "o", "u", "y"]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for k in vowels:
                if matrix[i][j] == k:
                    matrix[i][j] = "."
    return matrix


# Ввод размеров матрицы
while True:
    s = input("Введите n: ")
    if checking_for_integer(s, "natural"):
        n = int(s)
        break
    else:
        print("Вы неправильно ввели n, n - натуральное число")
while True:
    s = input("Введите m: ")
    if checking_for_integer(s, "natural"):
        m = int(s)
        break
    else:
        print("Вы неправильно ввели m, m - натуральное число")
matrix = [[0] * m for i in range(n)]
# Ввод матрицы
for i in range(n):
    for j in range(m):
        while True:
            s = input("Введите элемент {}-ой/ей строки {}-ого/его столбца\n".format(i + 1, j + 1))
            if len(s) == 1:
                matrix[i][j] = s
                break
            else:
                print("Вы ввели не символ")
# Печать исходной матрицы
print("Исходная матрица")
for i in range(len(matrix)):
    print("".join("{:^15}".format(matrix[i][j]) for j in range(len(matrix[0]))))
# Замена символов
new_matrix = change_vowels_to_dots(matrix)
# Печать итоговой матрицы
print("Получившаяся матрица")
for i in range(len(matrix)):
    print("".join("{:^15}".format(new_matrix[i][j]) for j in range(len(new_matrix[0]))))
