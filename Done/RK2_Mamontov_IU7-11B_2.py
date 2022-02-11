n = int(input("Введите n\n"))
m = int(input("Введите m\n"))
matrix = [[""] * m for i in range(n)]
for i in range(n):
    for j in range(m):
        print("Введите {}-ый/ой/ий элемент {}-ой/ей".format(i + 1, j + 1))
        matrix[i][j] = input()
res = []

for j in range(m):
    t = []
    for i in range(n):
        if ord(matrix[i][j]) >= 48 and ord(matrix[i][j]) <= 57:
            t.append(int(matrix[i][j]))
    if t:
        res.append(sum(t)/len(t))
    else:
        res.append("Нет цифр в столбце")
print("Средние арифмитические по столбцам")
for j in range(m):
    print(res[j])
used = []
for i in range(n):
    for j in range(m):
        if ord(matrix[i][j]) >= 65 and ord(matrix[i][j]) <= 90:
            used.append(i)
            used.append(j)
for u in range(len(used)):
    if u % 2 == 0:
        for j in range(m):
            matrix[used[u]][j] = "#"
    else:
        for i in range(n):
            matrix[i][used[u]] = "#"
for i in range(n):
    print(*matrix[i])