#   функція, що відповідає на питання, чи перетинають два заданих кола на площині


from math import sqrt


def circles_interception(x1, y1, r1, x2, y2, r2):
    cen_dist = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    if cen_dist > r1 + r2:
        return True
    return False

data = []
while True:
    line = input('Введите точки координат и радиус: ')
    if not line:
        break
    data.append(float(line))


print(circles_interception(*data))
