#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть значение радиуса круга
radius = 42

# Выведите на консоль значение прощади этого круга с точностю до 4-х знаков после запятой
# подсказки:
#       формулу можно подсмотреть в интернете,
#       пи возьмите равным 3.1415926
#       точность указывается в функции round()
PI = 3.1415926
s_circle = round(PI * radius ** 2, 4)
print(s_circle)


# Далее, пусть есть координаты точки
point = (23, 34)
# где 23 - координата х, 34 - координата у

# Если точка point лежит внутри того самого круга (radius = 42), то выведите на консоль True,
# Или False, если точка лежит вовне круга.
# подсказки:
#       нужно определить расстояние от этой точки до начала координат (0, 0)
#       формула так же есть в интернете
#       квадратный корень - это возведение в степень 0.5
#       операции сравнения дают булевы константы True и False
point1_x = point[0]
point1_y = point[1]
print('Circle includes point 1 =', point1_x ** 2 + point1_y ** 2 <= radius ** 2)

# Аналогично для другой точки
point_2 = (30, 30)
# Если точка point_2 лежит внутри круга (radius = 42), то выведите на консоль True,
# Или False, если точка лежит вовне круга.
point2_x = point_2[0]
point2_y = point_2[1]
print('Circle includes point 2 =', point2_x ** 2 + point2_y ** 2 <= radius ** 2)

# Пример вывода на консоль:
#
# 77777.7777
# False
# False


