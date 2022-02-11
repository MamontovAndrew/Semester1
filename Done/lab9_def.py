# прямоугольная целочисленная матрица, после каждого столбца, содержащего нулевые элементы, вставить столбец, который
# равен удвоенному значению предыдущего столбца
n = int(input("Введите n - кол-во строк матрицы: "))
m = int(input("Введите m - кол-во столбцов матрицы: "))
if m <= 0 or n <= 0:
    print("Матрица пустая")
    exit()
matrix = [[0 for j in range(m)] for i in range(n)]
for i in range(n):
    for j in range(m):
        a = int(input("Введите {}-й элемент {}-й строки: ".format(j + 1, i + 1)))
        matrix[i][j] = a
print("Исходная матрица")
for i in range(n):
    for j in range(m):
        print("{:^8d}".format(matrix[i][j]), end="")
    print()
j = 0
while j < m:
    for i in range(n):
        if matrix[i][j] == 0:
            m += 1
            for i2 in range(n):
                matrix[i2].append(matrix[i2][m-2])
            for i2 in range(n):
                for j2 in range(m - 2, j, -1):
                    matrix[i2][j2] = matrix[i2][j2 - 1]
                matrix[i2][j + 1] = matrix[i2][j] * 2
            j += 1
            break
    j += 1
print("Итоговая матрица")
for i in range(n):
    for j in range(m):
        print("{:^8d}".format(matrix[i][j]), end="")
    print()
