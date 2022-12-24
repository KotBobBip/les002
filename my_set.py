my_set = set([1,2,3,3,4,5,5,30,90])
print(my_set)
other_set = {5,5,3,2,1,22,4}
print(other_set)
print('Объединение', my_set | other_set)
print('Пересечение', my_set & other_set)
print('Вычитание', my_set - other_set)