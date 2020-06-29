import math

class Apple():
    def __init__(self, f, a, s, j, c):
        self.fruitiness = f
        self.acidity = a
        self.sweetness = s
        self.juiciness = j
        self.crispiness = c
        print("created!")

class Circle():
    def __init__(self, r):
        self.radius = r
        print("created!")

    def area(self):
        return 3.14 * math.pow(self.radius, 2)

class Triangle():
    def __init__(self, b, h):
        self.base = b
        self.height = h
        print("created!")

    def area(self):
        return (self.base * self.height) / 2

class Hexagon():
    def __init__(self, s):
        self.side = s
        print("created!")

    def calculate_perimeter(self):
        return 6 * self.side

circle = Circle(15)
print(circle.area())
triangle = Triangle(10, 15)
print(triangle.area())
hexagon = Hexagon(5)
print(hexagon.calculate_perimeter())