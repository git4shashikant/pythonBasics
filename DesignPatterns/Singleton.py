class singleton:
    _instance = None

    def __init__(self, _instance = None):
        if _instance is None:
            _instance = singleton()

    def __get__(self, _instance=None):
        if _instance:
            return _instance
        else:
            _instance = singleton()
            return _instance


test1 = singleton(None)
test2 = singleton(None)
print(test1)
print(test2)
print(test1 == test2)
