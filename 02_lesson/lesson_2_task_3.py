import math


def square(side):
    return math.ceil(side * side)


num_side = float(input("Сторона квадрата: "))
print(f"Площадь квадрата: {square(num_side)}")
