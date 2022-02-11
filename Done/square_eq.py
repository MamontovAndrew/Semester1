#Программа для нахождения корней квадратного уравнения ax^2 + bx + c = 0 по заданым коэффициентам a, b, c
#Мамонтов Андрей ИУ7-11Б

from math import sqrt

#Ввод данных
a, b, c = map(float, input().split())
#Проверка функции по коэффициентам и нахождение корней, вывод данных
if a == 0:
    if b == 0:
        if c == 0:
            print("х - любой")
        else:
            print("Корней нет")
    else:
        x = -c / b
        print("1 корень {:.2f}".format(x))
else:
    d = b ** 2 - 4 * a * c
    if d < 0:
        print("Нет действительных корней")
    else:
        if d == 0:
            x = (-b - sqrt(d)) / (2 * a)
            print("1 корень: {:.2f}".format(x))
        else:
            x1 = (-b - sqrt(d)) / (2 * a)
            x2 = (-b + sqrt(d)) / (2 * a)
            print("2 корня: {:.2f} {:.2f}".format(x1, x2))