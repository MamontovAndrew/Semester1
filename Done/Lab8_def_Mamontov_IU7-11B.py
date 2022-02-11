# Найти в квадратной символьной матрице количество диагоналей, параллельных главной, в которых встречаются согласные латинские буквы
n = int(input("Введите n: "))
if n == 1:
    print("Так как в матрице 1 элемент, диагоналей параллельных главной не будет, значит их колчиество 0")
    exit()
matrix = [[" " for j in range(n)] for i in range(n)]
for i in range(n):
    for j in range(n):
        matrix[i][j] = input("Введите {}-й элемент {}-й строки: ".format(i + 1, j + 1))

res = 0
vowels = ["a", "i", "o", "u", "y", "e", "A", "I", "O", "U", "Y", "E"]
letters = [chr(i) for i in range(97, 123)] + [chr(j) for j in range(65, 91)]

# Проход от левого края по диагонали
for k in range(n):
    i = k
    j = -1
    while i < n - 1:
        i += 1
        j += 1
        if matrix[i][j] in letters and not matrix[i][j] in vowels:
            res += 1
            break

# Проход от верхнего края по диагонали
for k in range(n):
    i = -1
    j = k
    while j < n - 1:
        i += 1
        j += 1
        if matrix[i][j] in letters and not matrix[i][j] in vowels:
            res += 1
            break
print("Количество диагоналей в квадратной матрице, параллельных главной, в которых встречаются согласные латинские буквы: ", res)