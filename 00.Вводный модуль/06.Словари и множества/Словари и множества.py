my_dict = {'Hello':'Привет', 'World':'Мир', 'Word': 'Слово'}
print(f'Dict: {my_dict}')
print(f'Existing value: {my_dict["Hello"]}')
print(f"Not existing value: {my_dict.get('Hey','Такой ключ отсутствует')}")
my_dict.update({'Bye': 'Пока', 'Board':'Доска'})
print(f"Deleted value: {my_dict.pop('World')}")
print(f'Modified dictionary: {my_dict}')

my_set = {3, 1,4,1,5,9,2,6,5,3, "Hey"}
print(f'My set: {my_set}')
my_set |= {7,12}
my_set.discard(1)
print(f'Modified set {my_set}')
