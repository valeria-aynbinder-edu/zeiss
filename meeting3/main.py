print(f"__name__ value for executed script {__file__}: {__name__}")

from geometry.shapes import Rectangle, Triangle
from utils.input_utils import *


if __name__ == "__main__":
    print("Hello! Lets get some data for rectangle and triangle")

    height, width = get_rectangle_input()
    rectangle = Rectangle(height, width)

    sides = get_triangle_input()
    triangle = Triangle(*sides)

    rec_area = rectangle.area()
    tri_area = triangle.area()

    if rectangle.area() > triangle.area():
        print(f"Rectangle area {rec_area} is bigger than triangle area {tri_area}")
    else:
        print(f"Triangle area {tri_area} is bigger than rectangle area {rec_area}")