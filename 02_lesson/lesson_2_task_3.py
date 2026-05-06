import math


def square(s):
    return math.ceil(s * s)


ss = float(input("Введите сторону квадрата"))

print(f'Площаль квадрата равна{square(ss)}')
