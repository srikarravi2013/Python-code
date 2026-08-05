class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)



rectangle = Rectangle(5, 3)


print(f"Length: {rectangle.length}")
print(f"Width: {rectangle.width}")
print(f"Area: {rectangle.area()}")
print(f"Perimeter: {rectangle.perimeter()}")