# Программа, которая для заданных целочисленных координат вершин треугольника и целочисленных координат точки выводит
# стороны треугольника, длину медианы, проведенной из наибольшего угла, определяет является ли треугольник прямоугольным
# проверяет, лежит ли точка внутри треугольника, и если лежит, находит расстояние до ближайшей стороны треугольника или
# её продолжения
# Мамонтов Андрей ИУ7-11Б

# Импортируем команду квадратного корня из библиотеки
from math import sqrt

#Определяем эпсилон для сравнения чисел
eps = 10 ** -5

# Ввод данных
print("Введите координаты точки A через пробел")
ax, ay = map(int, input().split())
print("Введите координаты точки B через пробел")
bx, by = map(int, input().split())
print("Введите координаты точки C через пробел")
cx, cy = map(int, input().split())

# Находим длины сторон треугольника
ab = sqrt((ax - bx) ** 2 + (ay - by) ** 2)
bc = sqrt((bx - cx) ** 2 + (by - cy) ** 2)
ac = sqrt((ax - cx) ** 2 + (ay - cy) ** 2)
print("Длина стороны AB: {:.2f}, BC: {:.2f}, AC: {:.2f}".format(ab, bc, ac))

# Находим длину медианы из наибольшего угла
max_side = max(ab, bc, ac)
if max_side == ab:
    m = sqrt((2 * bc ** 2 + 2 * ac ** 2 - ab ** 2) / 4)
elif max_side == bc:
    m = sqrt((2 * ab ** 2 + 2 * ac ** 2 - bc ** 2) / 4)
else:
    m = sqrt((2 * ab ** 2 + 2 * bc ** 2 - ac ** 2) / 4)
print("Длина медианы, проведенной из наибольшего угла: {:.2f}".format(m))

#Определяем, прямоугольный ли треугольник
if (abs(ab ** 2 + bc ** 2 - ac ** 2) < eps) or (abs(ab ** 2 + ac ** 2 - bc ** 2) < eps) or \
        (abs(bc ** 2 + ac ** 2 - ab ** 2) < eps):
    print("Треугольник прямоугольный")
else:
    print("Треугольник не прямоугольный")

# Ввод координат точки
print("Введите координаты точки D")
dx, dy = map(int, input().split())

# Определяем, принадлежит ли точка треугольнику
ad = sqrt((dx - ax) ** 2 + (dy - ay) ** 2)
bd = sqrt((dx - bx) ** 2 + (dy - by) ** 2)
cd = sqrt((dx - cx) ** 2 + (dy - cy) ** 2)
p_triangle = (ab + bc + ac) / 2
s_triangle = sqrt(p_triangle * (p_triangle - ab) * (p_triangle - bc) * (p_triangle - ac))
p1 = (ad + bd + ab) / 2
s1 = sqrt(p1 * (p1 - ad) * (p1 - bd) * (p1 - ab))
p2 = (bd + cd + bc) / 2
s2 = sqrt(p2 * (p2 - bd) * (p2 - cd) * (p2 - bc))
p3 = (ad + cd + ac) / 2
s3 = sqrt(p3 * (p3 - ad) * (p3 - cd) * (p3 - ac))
flag = False
if abs(s1 + s2 + s3 - s_triangle) < eps:
    print("Точка внутри треугольника")
    # Ищем расстояние от точки до ближайшей стороны или ее продолжения, если точка внутри треугольника
    distance_ab = 2 * s1 / ab
    distance_bc = 2 * s2 / bc
    distance_ac = 2 * s3 / ac
    min_distance = min(distance_ab, distance_bc, distance_ac)
    if min_distance == distance_ab:
        print("Наименьшее расстояние от точки до стороны треугольника (до AB) или её продолжения: {:.2f}".format(distance_ab))
    elif min_distance == distance_bc:
        print("Наименьшее расстояние от точки до стороны треугольника (до BC) или её продолжения: {:.2f}".format(distance_bc))
    else:
        print("Наименьшее расстояние от точки до стороны треугольника (до AC) или её продолжения: {:.2f}".format(distance_ac))
else:
    print("Точка лежит вне треугольника")