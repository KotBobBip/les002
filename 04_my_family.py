#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = ['Andrey', 'Anna', 'Artem']


# список списков приблизителного роста членов вашей семьи
my_family_height = [
    # ['имя', рост],
    [my_family[0], 178],
    [my_family[1], 175],
    [my_family[2], 66],
]

# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см
print('Мой рост', my_family_height[0][1])
print('Рост Ани', my_family_height[1][1])
print('Рост Тёмы', my_family_height[2][1])
# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см
print('Общий рост семьи', my_family_height[0][1] + my_family_height[1][1] + my_family_height[2][1])
