my_list = [1, 2, 3, 'a', 'b', 4, 5]
print(my_list[::-1])
my_list.append(77)
print(my_list[-1])
my_list.extend([7, 7, 7])
my_list.insert(2, 'blabla')
my_list.remove(3)
print(my_list)
my_list = my_list + list(range(0, 21, 2))
print(my_list)
del my_list[2:5]
print(my_list)
my_list.sort()
print(my_list)