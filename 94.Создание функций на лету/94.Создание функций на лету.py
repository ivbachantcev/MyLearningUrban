from random import choice

def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'a', encoding='utf-8') as file:
            for x in data_set:
                # наверное тут подразумевалось то, что надо преобразовать в строку
                file.write(str(x) + '\n')
    return write_everything

class MysticBall:
    def __init__(self, *words):
        self.words = words
    
    def __call__(self):
        return choice(self.words)
# 1 lambda функция
first = 'Мама мыла раму'
second = 'Рамена мало было'
print(list(map(lambda x, y: x == y, first, second)))

# 2 замыкание
write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

# 3 метод __call__
first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())