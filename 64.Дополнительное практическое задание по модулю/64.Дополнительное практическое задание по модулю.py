from math import pi
class Figure:
    sides_count = 0
    field = False

    def __init__(self, color, *sides):
        self.__sides = []
        self.__color = []
        self.set_color(*color)
        self.set_sides(sides)

    def get_color(self):
        return self.__color
    
    def __is_valid_color(self, r, g, b):
        return all(0 <= x <= 255 and isinstance(x, int) for x in [r, g, b])
    
    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]
    
    def __is_valid_sides(self, *args):
        return all(isinstance(x, int) and x > 0 for x in args) and (len(args) == self.sides_count)
    
    def set_sides(self, *new_sides):
        if self.__is_valid_sides(new_sides):
            self.__sides = new_sides
        else:
            self.__sides = [1] * self.sides_count
    
    def get_sides(self):
        return self.__sides
    
    def __len__(self):
        return sum(self.__sides)
    

class Circle(Figure):
    sides_count = 1
    def __init__(self, color, side):
        __sides = []
        super().__init__(color, side)
        self.__radius = self.get_sides()[0] / (2 * pi)
    def get_square(self):
        return self.get_sides()[0] ** 2 / 4 * pi
    
class Triangle(Figure):
    sides_count = 3
    __sides = []
    def get_square(self):
        p = len(self) / 2
        a, b, c = self.get_sides()
        return (p * (p - a) * (p - b) * (p - c)) ** .5

class Cube(Figure):
    sides_count = 12
    def __init__(self, color, sides):
        self.__sides = []
        self.set_color(*color)
        self.set_sides(sides)
        # super().__init__(color, [sides] * self.sides_count)
    
    def __is_valid_sides(self, *args):
        print(args[0])
        return (len(args) == 1) and isinstance(args[0], int)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(new_sides):
            self.__sides = [new_sides[0]] * 12
        else:
            self.__sides = [1] * 12

    def get_sides(self):
        return self.__sides

    def get_volume(self):
        return self.get_sides()


circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())