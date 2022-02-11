#Программа для поиска корней квадратного уравнения и отрисовки графика квадратичной функции
#Мамонтов Андрей ИУ7-11Б


import matplotlib.pyplot as plt
import numpy as np
from math import sqrt


#Поиск корней квадратного уравнения
def square_equation(a, b, c):
    d = b ** 2 - 4 * a * c
    if d < 0:
        return False
    elif d == 0:
        return [(-b - sqrt(d)) / (2 * a)]
    else:
        return [(-b - sqrt(d)) / (2 * a), (-b + sqrt(d)) / (2 * a)]

#Отрисовка квадратичной функции
def draw(a, b, c):
    x = np.linspace(-20, 20, 100)
    y = [a * i ** 2 + b * i + c for i in x]
    plt.xlim(-20, 20)
    plt.ylim(-20, 20)
    plt.title("График вашей функции")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid()
    plt.plot(x, y)
    plt.show()

#Ввод-вывод данных
print("Введите коэффициенты уравнения a, b, c через пробел")
input_data = list(map(int, input().split()))
result = square_equation(*input_data)
if not result:
    print("Корней нет")
elif len(result) == 1:
    print("Есть 1 корень: ", result[0])
else:
    print("Два корня: {:.2f} и {:.2f}".format(result[0], result[1]))
draw(*input_data)