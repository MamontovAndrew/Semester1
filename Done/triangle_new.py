from math import sqrt
print("Введите координаты точки A")
ax, ay = map(int, input().split())
print("Введите координаты точки B")
bx, by = map(int, input().split())
print("Введите координаты точки C")
cx, cy = map(int, input().split())
ab = sqrt((bx - ax) ** 2 + (by - ay) ** 2)
bc = sqrt((cx - bx) ** 2 + (cy - by) ** 2)
ac = sqrt((cx - ax) ** 2 + (cy - ay) ** 2)
min_side = min(ab, bc, ac)
if min_side == ab:
    bc_ac = bc / ac
    lx = (ax + bc_ac * bx) / (1 + bc_ac)
    ly = (ay + bc_ac * by) / (1 + bc_ac)
    print("Длина биссектрисы: {:.2f}".format(sqrt((lx - cx) ** 2 + (ly - cy) ** 2)))
elif min_side == bc:
    ac_ab = ac / ab
    lx = (bx + ac_ab * cx) / (1 + ac_ab)
    ly = (by + ac_ab * by) / (1 + ac_ab)
    print("Длина биссектрисы: {:.2f}".format(sqrt((lx - ax) ** 2 + (ly - ay) ** 2)))
else:
    ab_bc = ab / bc
    lx = (ax + ab_bc * cx) / (1 + ab_bc)
    ly = (ay + ab_bc * cy) / (1 + ab_bc)
    print("Длина биссектрисы: {:.2f}".format(sqrt((lx - bx) ** 2 + (ly - by) ** 2)))