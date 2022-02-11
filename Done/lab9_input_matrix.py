from Done.lab9_number_check import checking_for_integer, checking_for_float
def matrix_input(mode = "rectangle"):
    while True:
        s = input("Введите n: ")
        if checking_for_integer(s, "natural"):
            n = int(s)
            break
        else:
            print("Вы неправильно ввели n, n - натуральное число")
    if mode != "square":
        while True:
            s = input("Введите m: ")
            if checking_for_integer(s, "natural"):
                m = int(s)
                break
            else:
                print("Вы неправильно ввели m, m - натуральное число")
    else:
        m = n
    matrix = [[0] * m for i in range(n)]
    for i in range(n):
        for j in range(m):
            while True:
                s = input("Введите элемент {}-ой/ей строки {}-ого/его столбца\n".format(i + 1, j + 1))
                if checking_for_float(s):
                    matrix[i][j] = float(s)
                    break
                else:
                    print("Вы ввели не число")
    return matrix