x = 3


class oopsConcepts:
    # x is a class variable and shared across all instances of the class
    _internal_array = [1, 2, 3]

    # using kwargs for passing variables, this way we can pass vars in any order using key value pair
    # this is similar to constructor
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
        print(f"method-1 of superclass: ", self._name)

    def methodTest2(self, string):
        print(f"method-2 of superclass: ", self._name, string)

    @classmethod
    def get_internal_array(cls):
        return oopsConcepts._internal_array


class childClass(oopsConcepts):

    # overloaded method
    def methodTest1(self, string):
        print(f"method-1 (overloaded ) of subclass: ", self._name)

    # overridden method
    def methodTest2(self, string):
        print(f"method-2 (Overridden) of subclass: ", self._name, string)

    def methodTest3(self):
        print(f"method-3 of subclass: ", self._name)


def main():
    parent = oopsConcepts(name="oopsConcepts")
    parent.methodTest1()
    parent.methodTest2(" complete.")

    child = childClass(name = "childClass")
    child.methodTest1("first parameter")
    child.methodTest2("first parameter")
    child.methodTest3()

    default_parent = oopsConcepts()
    default_parent.methodTest1()
    print(f"New name is set to default: ", default_parent.name("newParent"))
    default_parent.methodTest2("complete.")
    for i in oopsConcepts.get_internal_array():
        print(i)


if __name__ == "__main__":
    main()
