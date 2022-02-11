from Done.lab9_number_check import checking_for_integer, checking_for_float
def list_input():
    arr = []
    while True:
        s = input("Введите n\n")
        if checking_for_integer(s, "natural"):
            n = int(s)
            break
        else:
            print("Вы неправильно ввели n, n - натуральное число")
    for i in range(n):
        while True:
            s = input("Введите {}-й элемент: ".format(i + 1))
            if checking_for_float(s):
                arr.append(float(s))
                break
            else:
                print("Вы ввели не число")
    return arr