import math

class Point2D:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def translate(self, dx, dy):
        self.__x += dx
        self.__y += dy

    def distance_from(self, other):
        dx = self.__x - other.__x
        dy = self.__y - other.__y
        dist = math.sqrt(dx ** 2 + dy ** 2)
        return dist

    def __str__(self):
        return f"({self.__x},{self.__y})"


    # def __eq__(self, other):
    #     print("Calling __eq__")
    #     return (self.__x, self.__y) == (other.get_x(), other.get_y())


    def __ne__(self, other):
        return (self.__x, self.__y) != (other.get_x(), other.get_y())




p1 = Point2D()
p2 = Point2D(1, 3)
p3 = Point2D(1, 3)

print(f"p1: {p1}")
print(f"p2: {p2}")
print(f"p3: {p3}")

if p2 == p3:
    print("Equals")
else:
    print("Not equals")

if p2 != p3:
    print("Not equals")
else:
    print("Equals")


# print(p1 + p2)



# print(f"id of p2: {id(p2)}")
# print(f"id of p3: {id(p3)}")

# print(f"Distance: {p1.distance_from(p2)}")
# print(f"Distance: {p2.distance_from(p1)}")

