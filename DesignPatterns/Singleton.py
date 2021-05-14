import functools


def singleton(cls):
    @functools.wraps(cls)
    def wrapper(*args, **kwargs):
        if not wrapper.instance:
            print("inside wrapper.")
            wrapper.instance = cls(*args, **kwargs)
            print("return from wrapper.")
        return wrapper.instance

    wrapper.instance = None
    print("return from outer singleton.")
    return wrapper


@singleton
class singletonCls:
    pass


c1 = singletonCls()
c2 = singletonCls()
print(c1)
print(c2)
print(c1 == c2)
print(c1 is c2)
