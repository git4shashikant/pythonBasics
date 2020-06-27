x = 3


class oopsConcepts:
    # x is a class variable and shared across all instances of the class
    x = [1, 2, 3]

    # using kwargs for passing variables, this way we can pass vars in any order using key value pair
    def __init__(self, **kwargs):
        self._name = kwargs['name'] if 'name' in kwargs else 'default_name'

    # this is a common setter and getter
    # its basic standard to use _ to recognize private variables as there is no private variable in python
    def name(self, n = None):
        if n:
            self._name = n
        try:
            return self._name
        except AttributeError:
            return None

    def methodTest1(self):
        print("method-1 of " + self._name)

    def methodTest2(self, string):
        print("method-2 of " + self._name + ", " + string)


class childClass(oopsConcepts):
    def __init__(self, _name):
        self._name = _name

    # method can be overloaded
    def methodTest2(self, string1, string2):
        print("method-2 of " + self._name + ", " + string1 + ", " + string2)

    def methodTest3(self):
        print("method-3 of " + self._name)


def main():
    c = oopsConcepts(name="oopsConcepts")
    c.methodTest1()
    c.methodTest2(" complete.")

    d = childClass("chileClass")
    d.methodTest2("from child class", " second parameter")
    d.methodTest3()

    e = oopsConcepts()
    e.methodTest1()
    e.name("newName")
    print("New changed name: ".format(e.name()))
    e.methodTest2("complete.")


if __name__ == "__main__":
    main()
