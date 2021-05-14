def func_operator(func):
    def wrapper(x, y):
        print(f"called function: {func.__name__} for {x}, {y}")
        if func.__name__ == "divide":
            if y == 0:
                print("Can't divide by zero")
                return
        elif func.__name__ == "subtract":
            if y > x:
                print(f"Can't subtract {y} from {x}")
                return

        func(x, y)
    return wrapper


@func_operator
def add(x, y):
    print(x + y)


@func_operator
def subtract(x, y):
    print(x - y)


@func_operator
def divide(x, y):
    print(x/y)


def main():
    add(10, 20)
    subtract(10, 20)
    subtract(10, -20)
    divide(10, 5)
    divide(10, 0)


if __name__ == '__main__':
    main()
