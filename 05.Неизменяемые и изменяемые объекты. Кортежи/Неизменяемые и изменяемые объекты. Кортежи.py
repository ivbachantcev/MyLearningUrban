immutable_var = (3, 1, 4, "Hi", .5)
print(f'Immutable tuple: {immutable_var}')
# кортежи неизменяемый тип данных,
# но если в качестве элемента кортежа будет
# например список, то его элементы можно будет поменять
mutable_list = [3, 1, 4, "Hi", .5]
mutable_list[3] = 'Bye'
print(f'Mutable list: {mutable_list}')
