# print(f"__name__ value for imported script {__file__}: {__name__}")

def get_rectangle_input():
    print("Please insert Rectangle data")
    height = float(input("Insert Rectangle height: "))
    width = float(input("Insert Rectangle width: "))
    return height, width


def get_triangle_input():
    print("Please insert Triangle data")
    sides = []
    for i in range(3):
        side = float(input(f"Insert Triangle side {i+1}: "))
        sides.append(side)
    return tuple(sides)