def print_params(a=1, b='string', c=True):
    print(a, b, c)
    
# 1 функция с параметрами по умолчанию
print_params() # без аргументов
print_params(3, 8, 4) # все три аргумента
print_params(3, 1) # два аргумента
print_params(b=25)
print_params(c=[1, 2, 3])

# 2 распаковка параметров
values_list = ['snake', 45, False]
values_dict = {'a': 'hey', 'b': False, 'c':[1, 2]}
print_params(*values_list)
print_params(**values_dict)

# 3 распаковка + отдельные параметры
values_list_2 = [[3, 7], 'Fristailo']
print_params(*values_list_2, 42)
