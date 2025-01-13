class Shape:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Shape at ({self.x}, {self.y})"


class Rectangle(Shape):
    def __init__(self, width, height, x=0, y=0):
        super().__init__(x, y)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def __str__(self):
        return f"Rectangle at ({self.x}, {self.y}), width: {self.width}, height: {self.height}"


class Square(Rectangle):
    def __init__(self, side, x=0, y=0):
        super().__init__(side, side, x, y)
        self._side = side

    @property
    def width(self):
        return self._side

    @width.setter
    def width(self, value):
        self._side = value
        if self.height != value:
            self.height = value

    @property
    def height(self):
        return self._side

    @height.setter
    def height(self, value):
        self._side = value
        if self.width != value:
            self.width = value

    @property
    def side(self):
        return self._side

    @side.setter
    def side(self, value):
        self._side = value

    def __str__(self):
        return f"Square at ({self.x}, {self.y}), side: {self.side}"


def increase_width(rect):
    rect.width *= 2


rect = Rectangle(2, 4)
print(rect)
increase_width(rect)
print(rect)

square = Square(2)
print(square)
increase_width(square)
print(square.height, square.width)


square.side = 5
print(square)
print(square.height, square.width)

square.height = 3
print(square)
print(square.height, square.width)

rect = Rectangle(2, 4)
print(f"Rectangle area: {rect.area()}")

square = Square(2)
print(f"Square area: {square.area()}")
