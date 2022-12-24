my_box = {}
my_box['el'] = 'elethant'
my_box['car'] = 'renault'
print(my_box)
my_shelf = {'book': '1994', 'comics': 'dead pool'}
print(my_shelf)
print('book' in my_shelf)
print(my_box.get('table', 'book'))
print(my_box.get('car', 'book'))
print(my_box.setdefault('CPU', 'Ryzen'))
print(my_box)
print(my_box.setdefault('car', 'lada'))
print(my_box)