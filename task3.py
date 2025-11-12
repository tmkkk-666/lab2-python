import math

class Figure: 
    def area(self):
        raise NotImplementedError("Subclasses must implement the area() method")

    def perimeter(self):
        raise NotImplementedError("Subclasses must implement the perimeter() method")

    def compare_area(self, other):
        return compare_area(self, other)

    def compare_perimeter(self, other):
        return compare_perimeter(self, other)

    def __repr__(self):
        return f"{self.__class__.__name__}()"


class Square(Figure):
    def __init__(self, side):
        if side <= 0:
            raise ValueError("Side length of square must be positive")
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side

    def __repr__(self):
        return f"Square(side={self.side})"

class Rectangle(Figure):
    def __init__(self, width, height):
        if width <= 0 or height <= 0:
            raise ValueError("Width and height of rectangle must be positive")
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def __repr__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

class Triangle(Figure):
    def __init__(self, a, b, c):
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("All sides of triangle must be positive")
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("Triangle does not satisfy the triangle inequality")
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def perimeter(self):
        return self.a + self.b + self.c

    def __repr__(self):
        return f"Triangle(a={self.a}, b={self.b}, c={self.c})"

class Circle(Figure):
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Radius of circle must be positive")
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius

    def __repr__(self):
        return f"Circle(radius={self.radius})"

def compare_area(fig1, fig2):
    if not isinstance(fig1, Figure) or not isinstance(fig2, Figure):
        raise TypeError("Parameters must be instances of Figure or its subclasses")

    a1 = fig1.area()
    a2 = fig2.area()

    if math.isclose(a1, a2):
        return 0
    elif a1 > a2:
        return 1
    else:
        return -1


def compare_perimeter(fig1, fig2):
    if not isinstance(fig1, Figure) or not isinstance(fig2, Figure):
        raise TypeError("Parameters must be instances of Figure or its subclasses")

    p1 = fig1.perimeter()
    p2 = fig2.perimeter()

    if math.isclose(p1, p2):
        return 0
    elif p1 > p2:
        return 1
    else:
        return -1


def main():
    # Create figure objects
    sq = Square(4)           # Square with side length 4
    rect = Rectangle(3, 5)   # Rectangle with width 3 and height 5
    tri = Triangle(3, 4, 5)  # Right triangle
    circ = Circle(2)         # Circle with radius 2

    print("Figure Information:")
    for fig in [sq, rect, tri, circ]:
        print(f"{fig}: Area={fig.area():.2f}, Perimeter={fig.perimeter():.2f}")

    print("Area Comparison:")
    result = sq.compare_area(rect)
    if result == 1:
        print(f"{sq}'s area > {rect}'s area")
    elif result == 0:
        print(f"{sq}'s area == {rect}'s area")
    elif result == -1:
        print(f"{sq}'s area < {rect}'s area")

    print("Perimeter Comparison:")
    result = sq.compare_perimeter(circ)
    if result == 1:
        print(f"{sq}'s perimeter > {circ}'s perimeter")
    elif result == 0:
        print(f"{sq}'s perimeter == {circ}'s perimeter")
    elif result == -1:
        print(f"{sq}'s perimeter < {circ}'s perimeter")

if __name__ == "__main__":
    main()
