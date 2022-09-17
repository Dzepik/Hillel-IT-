"""
Задача
"""

coords = {}
alphabet = "abcdefgh"
count = 1
for i in range(8):
    for j in range(1, 9):
        coords[count] = alphabet[i] + str(j)
        count += 1


def calculate_wheat_chess_position(kilograms: float) -> str:
    seed_weight = 35
    seed_count = int(kilograms * 1000000 / seed_weight)
    num = 1
    step = 1
    while num < seed_count:
        if step == 1:
            num = 2
        else:
            num **= 2
        step += 1
    return coords[step]

kilograms = 0.03584

print(calculate_wheat_chess_position(kilograms))

