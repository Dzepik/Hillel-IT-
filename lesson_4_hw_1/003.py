import math
radius = float(input("радиус конуса: "))
height = float(input("высота конуса: "))
def cone_square_and_volume(radius, height):
    volume = (height * math.pi * (radius ** 2)) / 3
    square = math.pi * radius * (radius + math.sqrt(radius ** 2 + height ** 2))

