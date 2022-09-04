#   функція, що відповідає на питання, чи перетинають два заданих кола на площині


from math import sqrt


def circles_interception(x1, y1, r1, x2, y2, r2):
    cen_dist = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    if not cen_dist:
        return "Нет" if r1 != r2 else "Да"
    else:
        return "Нет" if cen_dist > r1 + r2 else "Да"


data = []
while True:
    line = input()
    if not line:
        break
    data.append(float(line))

print(circles_interception(*data))
