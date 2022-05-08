# print(f"__name__ value for imported script {__file__}: {__name__}")
from meeting3.geometry.exceptions import GeometryException, InvalidTriangleException
from meeting3.geometry.shapes import Triangle
from meeting3.utils.validators import validate_side_format


def get_single_input(prompt):
    while True:
        try:
            return validate_side_format(input(prompt))
        except GeometryException as exc:
            print(f"{exc}\nPlease try again:")


def get_rectangle_input():
    print("Please insert Rectangle data")
    height = get_single_input("Insert Rectangle height: ")
    width = get_single_input("Insert Rectangle width: ")
    return height, width


def get_triangle_input():
    while True:
        print("Please insert Triangle data")
        sides = []
        for i in range(3):
            side = get_single_input(f"Insert Triangle side {i+1}: ")
            sides.append(side)
        sides = tuple(sides)
        try:
            Triangle.validate_triangle(*sides)
            break
        except InvalidTriangleException as exc:
            print(f"{exc}\nPlease try again")

    return sides