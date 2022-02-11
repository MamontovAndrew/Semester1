''' Мамонтов Андрей ИУ7-11Б '''
from math import *

eps = 1e-10
eps0 = 1e-20

# Введение функции

# Оформление для таблицы значений
line = '=' * 93
table_title = '|        аргумент      |      значение f1     |'
table_title += '      значение f2     |      значение f3     |'

# Ввод значений для таблицы
x1 = float(input('Начальное значение аргумента: '))
x2 = float(input('Конечное значение аргумента: '))
step = float(input('Шаг: '))
st = x1

# Проверка, можно ли составить таблицу
if (x1 <= x2 and step <= 0) or (x1 >= x2 and step >= 0):
    print('Неверно задан шаг, невозможно построить таблицу значений')
else:
    # Вывод таблицы значений
    print(line)
    print(table_title)
    print(line)
    i = 1
    mnf = mxf = x1 * x1 * x1 + 6.1 * x1 * x1 - 35.4 * x1 - 25.7

    # Вычисление количества итераций цикла
    it = (x2 - x1) / step
    it = trunc(it)

    # Вывод таблицы
    counter = 0
    while counter < it + 1:
        if abs(x1) >= 1e8 or eps >= abs(x1) > eps0:
            print('| {:20.10e}'.format(x1), end='')
        else:
            print('| {:20.10f}'.format(x1), end='')
        s1 = x1 ** 3 - 6.5 * x1 ** 2 - 31.3 * x1 + 2.32
        if abs(s1) >= 1e8 or eps >= abs(s1) > eps0:
            print(' | {:20.10e}'.format(s1), end='')
        else:
            print(' | {:20.10f}'.format(s1), end='')
        s2 = x1 ** 2 - sin(pi * x1)
        if abs(s2) >= 1e8 or eps >= abs(s2) > eps0:
            print(' | {:20.10e}'.format(s2), end='')
        else:
            print(' | {:20.10f}'.format(s2), end='')
        s3 = sqrt(s1 ** 2 + s2 ** 2)
        if abs(s3) >= 1e8 or eps >= abs(s3) > eps0:
            print(' | {:20.10e}'.format(s3), '|')
        else:
            print(' | {:20.10f}'.format(s3), '|')
        if mxf < s1:
            mxf = s1
        if mnf > s1:
            mnf = s1
        x1 += step
        counter += 1
    print(line, '\n\n')

    x1 = st

    # Ввод количества засечек
    notch = int(input('Введите количество засечек на графике: '))
    if notch <= 1:
        print('Количество засечек должно быть больше 1')

    # Сортировка координат по оси OX
    if x1 > x2:
        x1, x2 = x2, x1
    step = abs(step)
    # Вычисление вспомогательных величин, для построения графика
    num = 120
    xp = round(((-mnf) / (mxf - mnf)) * num)

    # Определение расстояния между засечками
    sh_z = num / (notch - 1)
    sh_z = round(sh_z)

    # Определение шага графика по оси OY
    sh_gr = (mxf - mnf) / (notch - 1)

    print(' ' * 17, end='')

    # Вывод засечек
    counter = 0
    while counter < notch:
        zn_y = mnf + i * sh_gr
        if abs(zn_y) >= 1e8 or eps >= abs(zn_y) > eps0:
            print('{:15.10e}'.format(zn_y), end='')
        else:
            print('{:15.10f}'.format(zn_y), end='')
        print(' ' * (sh_z - 15 + 1), end='')
        counter += 1
    print()

    # Вывод оси OY
    print(' ' * 21, '-|', sep='', end='')
    counter = 0
    while counter < notch - 1:
        print('-' * sh_z, '|', sep='', end='')
        counter += 1
    print('->y')

    # Построение графика построчно
    counter = 0
    while counter < it + 1:
        if abs(x1) >= 1e8 or eps >= abs(x1) > eps0:
            print('{:20.10e}'.format(x1), ' ', end='')
        else:
            print('{:20.10f}'.format(x1), ' ', end='')
        zn_x = x1 * x1 * x1 + 6.1 * x1 * x1 - 35.4 * x1 - 25.7
        p_xng = round(((zn_x - mnf) / (mxf - mnf)) * num)
        # Вычисление нахождения точки графика относительно оси OX
        if mnf > 0 or mxf < 0 or abs(xp - p_xng) < eps:
            print(' ' * p_xng, '*', sep='')
        elif xp < p_xng:
            print(' ' * xp, '|', sep='', end='')
            print(' ' * (p_xng - xp), '*', sep='')
        elif xp > p_xng:
            print(' ' * p_xng, '*', sep='', end='')
            print(' ' * (xp - p_xng - 1), '|', sep='')
        x1 += step
        counter += 1
