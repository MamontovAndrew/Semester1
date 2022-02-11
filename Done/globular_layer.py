#Программа, которая по заданным высотам шарового сегмента и радиусу шара определяет объём шарового слоя,
#площадь его полной, боковой поверхности и радиусы сечения шара плоскостями
#Мамонтов Андрей группа ИУ7-11Б

#Подключение функций из библиотеки
from math import pi, sqrt

#Ввод данных
print("Введите через пробел три числа: высоты шаровых сегментов, радиус шара")
h1, h2, R = map(float, input().split())
#Поиск объема шарового слоя
sphere_volume = 4 / 3 * pi * R ** 3
globural_segment1_volume = pi * h1 ** 2 * (R - h1 / 3)
globural_segment2_volume = pi * h2 ** 2 * (R - h2 / 3)
globular_layer_volume = sphere_volume - globural_segment1_volume - globural_segment2_volume
#Поиск радиусов сечений
r1 = sqrt(R ** 2 - (R - h1) ** 2)
r2 = sqrt(R ** 2 - (R - h2) ** 2)
#Поиск площади боковой и полной поверхности
lateral_surface_area = 2 * pi * R * (2 * R - h1 - h2)
total_surface_area = lateral_surface_area + pi * r1 ** 2 + pi * r2 ** 2
#Вывод данных
print("Объём шарового слоя {:.2f}".format(globular_layer_volume))
print("Объём боковой поверхности {:.2f}".format(lateral_surface_area))
print("Объём полной поверхности {:.2f}".format(total_surface_area))
print("Радиусы сечения: {:.2f} {:.2f}".format(r1, r2))