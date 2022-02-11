""" sin(x) - ln(x ** 2) Мамонтов Андрей ИУ7-11Б"""

from math import *

eps = 1e-10

x1 = float(input('Начальное значение аргумента: '))
x2 = float(input('Конечное значение аргумента: '))
step = float(input('Шаг: '))
st = x1

if x2 >= x1 and step <= 0 or x1 >= x2 and step >= 0:
    print('Шаг задан неверно')
else:
    step = abs(step)
    if x1 > x2:
        x1, x2 = x2, x1

    it = (x2 - x1) / step
    it = trunc(it)

    mnf = mxf = sin(x1) - log(x1 ** 2 + 1)
    for i in range(it + 1):
        s1 = sin(x1) - log(x1 ** 2 + 1)
        if mxf < s1:
            mxf = s1
        if mnf > s1:
            mnf = s1
        x1 += step

    x1 = st
    xp = round(((-mnf) / (mxf - mnf)) * 120)

    print(' ' * 11, '{:20.10f}'.format(mnf), ' ' * 100, '{:20.10f}'.format(mxf))
    print(' ' * 22, '|', '-' * 120, '|', sep='', end='')
    print('->y')

    for i in range(it + 1):
        print('{:20.5g}'.format(x1), " ", end="")
        zn_x = sin(x1) - log(x1 ** 2 + 1)
        p_xng = round(((zn_x - mnf) / (mxf - mnf)) * 120)
        if mnf > 0 or mxf < 0 or abs(xp - p_xng) < eps:
            print(' ' * p_xng, '*', sep='')
        elif xp < p_xng:
            print(' ' * xp, '|', sep='', end='')
            print(' ' * (p_xng - xp), '*', sep='')
        elif xp > p_xng:
            print(' ' * p_xng, '*', sep='', end='')
            print(' ' * (xp - p_xng - 1), '|', sep='')
        x1 += step
