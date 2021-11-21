# Создать класс Point, описывающий точку на плоскости.
#
# Определить метод для инициализации объекта при создании, методы позволяющие:
#
# складывать две точки,
# вычитать,
# отображать текущее состояние объекта.
#
# Так же, определить класс Triangle (треугольник). Вершины треугольника определить как объекты класса Point
# (НИКАКОГО НАСЛЕДОВАНИЯ). В классе создать методы для:
#
# инициализации объекта при создании
# метод для определения площади треуголььника (ссылка1 и ссылка2)
# метод для определения периметра треугольника (ссылка3)
# методы для изменения координат вершин

class Point:

    def __init__(self, x_coord, y_coord):
        for coord in [x_coord, y_coord]:
            if not isinstance(coord, int | float):
                raise TypeError

        self.x = x_coord
        self.y = y_coord

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return Point(x, y)

    def __str__(self):
        return f'point ({round(self.x, 2)}; {round(self.y, 2)})'

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_coords(self):
        return self.x, self.y


class Triangle:

    def __init__(self, point_a, point_b, point_c):
        for point in [point_a, point_b, point_c]:
            if not isinstance(point, Point):
                raise TypeError

        self.apex_a = point_a
        self.apex_b = point_b
        self.apex_c = point_c

    def square(self):
        '''
        Returns the square of the triangle rounded to two decimal places

        :return: square of the triangle
        :rtype: float
        '''

        res = abs(0.5 * ((self.apex_a.x - self.apex_c.x) * (self.apex_b.y - self.apex_c.y) - (
                self.apex_b.x - self.apex_c.x) * (self.apex_a.y - self.apex_c.y)))

        return round(res, 2)

    def perimeter(self):
        """
        Returns the perimeter of the triangle rounded to two decimal places

        :return: perimeter of the triangle
        :rtype: float
        """
        ab = ((self.apex_b.x - self.apex_a.x) ** 2 + (self.apex_b.y - self.apex_a.y) ** 2) ** 0.5
        bc = ((self.apex_c.x - self.apex_b.x) ** 2 + (self.apex_c.y - self.apex_b.y) ** 2) ** 0.5
        ac = ((self.apex_c.x - self.apex_a.x) ** 2 + (self.apex_c.y - self.apex_a.y) ** 2) ** 0.5

        res = ab + bc + ac

        return round(res, 2)

    def change_coord(self, apex, x=None, y=None):
        """
        Change one or both coordinates of the apex in triangle.

        :param apex: name of apex (A, B or C)
        :type apex: str
        :param x: new coordinate x or None for to leave the current coordinate
        :type x: int | float | None
        :param y: new coordinate y or None for to leave the current coordinate
        :type y: int | float | None
        """
        for coord in [x, y]:
            if not isinstance(coord, int | float | None):
                raise TypeError

        if not isinstance(apex, str):
            raise TypeError
        elif apex.upper() not in ['A', 'B', 'C']:
            raise ValueError
        elif apex == 'A':
            self.apex_a = Point(x if x else self.apex_a.x, y if y else self.apex_a.y)
        elif apex == 'B':
            self.apex_b = Point(x if x else self.apex_b.x, y if y else self.apex_b.y)
        elif apex == 'C':
            self.apex_c = Point(x if x else self.apex_c.x, y if y else self.apex_c.y)


# Initialization of the points:
a = Point(3, 2)
b = Point(2.1, 2)

# String representation of the points:
print(f'String representation: {str(a)}, {str(b)}')

# Addition and subtraction:
print(f'a + b = {a + b}')
c = a - b
print(f'c = a - b = {c}')

# Getting one or both coordinates:
x = a.get_x()
y = a.get_y()
coords = a.get_coords()
print(f'x = {x}, y = {y}, coords = {coords}')

# Initialization of the triangle:
my_triangle = Triangle(a, b, Point(4, 6.1))

# Square of the triangle:
print(f'Square = {my_triangle.square()}')

# Perimeter of the triangle:
p = my_triangle.perimeter()
print(f'Perimeter = {p}')

# Changing coordinates of the apexes in different ways:
my_triangle.change_coord('A', 6)  # changing only x
my_triangle.change_coord('B', y=8)  # changing only y
my_triangle.change_coord('C', 3, 2.5)

new_apexes = {
    'a': (None, 2),
    'B': (2, None),
    'c': (4, 5)
}
for apex, (x, y) in new_apexes.items():
    my_triangle.change_coord(apex, x, y)

print(my_triangle.apex_a)
print(my_triangle.apex_b)
print(my_triangle.apex_c)
