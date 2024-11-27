def custom_write(file_name, strings):
    r = dict()
    f = open(file_name, 'w', encoding='utf-8')
    for num, s in enumerate(strings, 1):
        r[(num, f.tell())] = s
        f.write(s + '\n')
    f.close()
    return r


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)