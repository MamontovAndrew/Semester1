from Done import lab9_number_check as my


# Подынтегральная функция
def func(x):
    return x ** 2


def calc_integral_right_rect(a: float, b: float, n: int):
    result = 0
    h = (b - a) / n  # шаг
    for i in range(1, n + 1):
        result += func(a + h * i)
    result *= h
    return result


def calc_integral_3_8(a: float, b: float, n: int):
    h = (b - a) / n
    result = func(a) + func(b)

    for i in range(1, n):
        if i % 3 == 0:
            result += 2 * func(a + i * h)
        else:
            result += 3 * func(a + i * h)
    return result * (3 * h / 8)


# Первообразная подынтегральной функции
def prim_func(x):
    return x ** 3 / 3


# Функция main
def main():
    # Ввод и проверка значений
    while True:
        while True:
            a = input("Введите начало отрезка: ")
            if my.checking_for_float(a):
                a = float(a)
                print()
                break
            else:
                print("Неверный ввод", end="\n\n")

        while True:
            b = input("Введите конец отрезка: ")
            if my.checking_for_float(b):
                b = float(b)
                print()
                break
            else:
                print("Неверный ввод", end="\n\n")

        if a != b:
            break
        else:
            print("Начало и конец отрезка не должны совпадать", end="\n\n")

    while True:
        N1 = input("Введите первое количество участков разбиения больше 0): ")
        if N1.isdigit() and int(N1) > 0:
            N1 = int(N1)
            print()
            break
        else:
            print("Неверный ввод", end="\n\n")

    while True:
        N2 = input("Введите второе количество участков разбиения больше 0): ")
        if N2.isdigit() and int(N2) > 0:
            N2 = int(N2)
            print()
            break
        else:
            print("Неверный ввод", end="\n\n")

    # Проверка значений начала и конца отрезка
    if b < a:
        a, b = b, a

    # Таблица значений
    print("-" * 61)
    print("|", end="")
    print(" " * 19, end="")
    print("|", end="")
    print("N1", end="")
    print(" " * 17, end="")
    print("|", end="")
    print("N2", end="")
    print(" " * 17, end="")
    print("|")
    print("-" * 61)
    print("|", end="")
    print("Метод 1", end="")
    print(" " * 12, end="")
    print("|", end="")
    print("{:<12.3g}".format(calc_integral_right_rect(a, b, N1)), end="")
    print(" " * 7, end="")
    print("|", end="")
    print("{:<12.3g}".format(calc_integral_right_rect(a, b, N2)), end="")
    print(" " * 7, end="")
    print("|")
    print("-" * 61)
    print("|", end="")
    print("Метод 2", end="")
    print(" " * 12, end="")
    print("|", end="")
    print("{:<12.3g}".format(calc_integral_3_8(a, b, N1)), end="")
    print(" " * 7, end="")
    print("|", end="")
    print("{:<12.3g}".format(calc_integral_3_8(a, b, N2)), end="")
    print(" " * 7, end="")
    print("|")
    print("-" * 61, end="\n\n")

    # Истинное значение интеграла
    real_val = prim_func(b) - prim_func(a)

    # Ввод N для проверки точности методов
    while True:
        N = input(
            "Введите количество участков разбиения для сравнения двух методов и больше 0): ")
        if N.isdigit() and int(N) > 0:
            N = int(N)
            print()
            break
        else:
            print("Неверный ввод", end="\n\n")

    # Ветвление для разных случаев
    if abs(real_val - calc_integral_3_8(a, b, N)) < abs(real_val - calc_integral_right_rect(a, b, N)):
        print("Наиболее точен метод 3/8")
        print("Абсолютная погрешность: {:.3g}".format(abs(real_val - calc_integral_3_8(a, b, N))))
        print("Относительная погрешность: {:.3g}".format(
            abs(real_val - calc_integral_3_8(a, b, N)) / abs(calc_integral_3_8(a, b, N))),
              end="\n\n")

        # Ввод точности для вычисления количества участков разбиения 2-м методом
        while True:
            eps = input("Введите точность для вычисления количества участков разбиения 2-м методом: ")
            if my.checking_for_float(eps) and float(eps) > 0:
                eps = float(eps)
                break
            else:
                print("Неверный ввод", end="\n\n")

        # Поиск нужного N
        N = 1
        I1 = calc_integral_right_rect(a, b, 1)
        I2 = calc_integral_right_rect(a, b, 2 * N)
        while abs(I1 - I2) > eps:
            I1 = I2
            N *= 2
            I2 = calc_integral_right_rect(a, b, 2 * N)
        print("Необходимое количество участков разбиения:", N)

    elif abs(real_val - calc_integral_3_8(a, b, N)) > abs(real_val - calc_integral_right_rect(a, b, N)):
        print("Наиболее точен метод правых прямоугольников")
        print("Абсолютная погрешность: {:.3g}".format(abs(real_val - calc_integral_right_rect(a, b, N))))
        print("Относительная погрешность: {:.3g}".format(
            abs(real_val - calc_integral_right_rect(a, b, N)) / abs(calc_integral_right_rect(a, b, N))), end="\n\n")

        # Ввод точности для вычисления количества участков разбиения 2-м методом
        while True:
            eps = input("Введите точность для вычисления количества участков разбиения 2-м методом: ")
            if my.checking_for_float(eps) and float(eps) > 0:
                eps = float(eps)
                break
            else:
                print("Неверный ввод", end="\n\n")
    else:
        print("Оба метода одинаково точны при заданном N")


# Вызов функции main при условии, что __name__ == "__main__"
if __name__ == "__main__":
    main()
