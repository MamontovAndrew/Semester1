def func(x):
    return x ** 2


def prim_func(x):
    return x ** 3 / 3


def calc_integral(a, b, n):
    step = (b - a) / n
    result = 0
    for i in range(n):
        result += step * (func(a + step * i) + func(a + step * (i + 1))) / 2
    return result

a = int(input("Введите значение начала отрезка: "))
b = int(input("Введите значение конца отрезка: "))
n = int(input("Введите количество участков разбиения: "))
print("Истинное значение: ", prim_func(b) - prim_func(a))
print("Значение методом трапеций: ", calc_integral(a, b, n))
