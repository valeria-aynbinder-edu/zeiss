from abc import ABC, abstractmethod
from math import sqrt

from meeting3.geometry.exceptions import InvalidTriangleException

print(f"__name__ value for imported script {__file__}: {__name__}")

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Rectangle(Shape):

    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        return self.height * self.width

    def perimeter(self):
        return 2 * (self.height + self.width)



class Triangle(Shape):

    def __init__(self, side1, side2, side3):
        self.sides = (side1, side2, side3)

    def area(self):
        s = sum(self.sides) / 2
        return sqrt(s * (s-self.sides[0]) * (s-self.sides[1]) * (s))

    def perimeter(self):
        return sum(self.sides)

    @staticmethod
    def validate_triangle(side1: float, side2: float, side3: float) -> None:
        """
        Given 3 sides of a triangle, return if these sides can
        construct a valid triangle according to the following rule:
        The sum of the length of any two sides of a triangle must be
        greater than the length of the third side.
        For example, [3, 4, 5] is a proper triangle since:
            3+4>5, 3+5>4, 4+5>3.
        However, [8, 2, 3] is not a triangle since
            2+3<8

        Otherwise, raise InvalidTriangleException

        :param side1: length of side 1
        :param side2: length of side 2
        :param side3: length of side 3

        """
        if side1 + side2 > side3 and \
            side1 + side3 > side2 and \
                side2 + side3 > side1:
            pass
        else:
            raise InvalidTriangleException(
                f"Triangle with sides {(side1, side2, side3)} is invalid")



class Circle(Shape):
    def area(self):
        pass

    def perimeter(self):
        pass