class square:
    def __init__(self, side):
        self._side = side

    @property
    def side(self):
        return self._side

    @property
    def area(self):
        return self._side ** 2

    @side.setter
    def side(self, value):
        self._side = value

    @classmethod
    def unit(cls):
        return 1


if __name__ == "__main__":
    s = square(5)
    print(s.area)
