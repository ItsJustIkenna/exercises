class Shape():
    def __init__(self, s):
        self.side = s
        print("created!")

    def calculate_perimeter(self):
        return 4 * self.side

    def what_am_i(self):
        print("I am a shape")

    def change_size(self, n):
        self.side += n

class Square(Shape):
    pass

class Rectangle(Shape):
    def __init__(self, l, w):
        self.len = l
        self.width = w
        print("created!")

    def calculate_perimeter(self):
        return 2 * (self.len + self.width)

class Horse():
    def __init__(self, n, b ,r):
        self.name = n
        self.breed = b
        self.rider = r

class Rider():
    def __init__(self, n):
        self.name = n

rectangle = Rectangle(10, 15)
print(rectangle.calculate_perimeter())
square = Square(6)
print(square.calculate_perimeter())
square.change_size(6)
print(square.side)
square.change_size(-24)
print(square.side)
kennedy = Rider("Kennedy Road")
secretariat = Horse("secretariat", "American Thoroughbred",kennedy)
print(secretariat.rider.name)
square.what_am_i()
rectangle.what_am_i()