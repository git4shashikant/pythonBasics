def function1(x, y=2):
    return x - y


# multiple argument
def function2(*args):
    print(args)


def function_conditions(x, y):
    if x == y:
        print("Equal number")
    elif x < y:
        print("x is lesser number")
    else:
        print("x is greater numbers")


def switch_example(argument):
    switcher = {
        0: "This is Case Zero ",
        1: "This is Case One ",
        2: "This is Case Two ",
    }
    return switcher.get(argument, "nothing")


def keyword_arg_example():
    example(Buffy='meow', Zilla='grr', Angel='rawr')


# keyword arguments
def example(**kwargs):
    if len(kwargs):
        for k in kwargs:
            print("{} says {}".format(k, kwargs[k]))


print(function1(2))
print(function1(2, 5))
print(function1(x=2, y=3))
print(function1(y=4, x=2))
print(function2(1, 2, 3, 4))
function_conditions(4, 6)
function_conditions(6, 4)
function_conditions(6, 6)
print(switch_example(2))
print(switch_example(3))
keyword_arg_example()
