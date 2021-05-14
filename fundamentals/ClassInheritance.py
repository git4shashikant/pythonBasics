from math import sqrt


class Polygon:
    _global_shape = "Polygon"

    @staticmethod
    def get_parent():
        return "Parent is a {}".format(Polygon._global_shape)

    def get_desc(self):
        pass

    def get_area(self):
        pass

    def get_perimeter(self):
        pass


class Triangle(Polygon):

    def __init__(self, length = 0):
        self._shape = "Triangle"
        self._length = length

    def get_desc(self):
        return "It is a {} of side length {}.".format(self._shape, self._length)

    def get_area(self):
        area = (sqrt(3) * self._length) / 2
        return "Area of Triangle: {}".format(area)

    def get_perimeter(self):
        perimeter = 3 * self._length
        return "Perimeter of Triangle: {} ".format(perimeter)


class Rectangle(Polygon):

    def __init__(self, length = 0):
        self._shape = "Rectangle"
        self._length = length

    def get_desc(self):
        return "It is a {} of side length {}.".format(self._shape, self._length)

    def get_area(self):
        area = (self._length * self._length)
        return "Area of Rectangle: {}".format(area)

    def get_perimeter(self):
        perimeter = 4 * self._length
        return "Perimeter of Rectangle: {} ".format(perimeter)


def main():
    polygon = Polygon()
    triangle = Triangle(10)
    rectangle = Rectangle(10)

    print(polygon.get_desc())
    print(polygon.get_area())
    print(polygon.get_perimeter())

    print(triangle.get_desc())
    print(triangle.get_area())
    print(triangle.get_perimeter())
    print(triangle.get_parent())

    print(rectangle.get_desc())
    print(rectangle.get_area())
    print(rectangle.get_perimeter())
    print(rectangle.get_parent())


if __name__ == '__main__':
    main()
