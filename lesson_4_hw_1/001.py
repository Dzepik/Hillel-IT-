import math


def degrees2radians(degrees):
    n_rad = (float(degrees)*math.pi)/180
    return (n_rad)


a = degrees2radians(60)
b = degrees2radians(45)
c = degrees2radians(40)

print(math.cos(a), math.cos(b) ,math.cos(c))







    