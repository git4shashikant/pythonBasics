def print_fn(string):
    def print_fn_inner():
        print(string)

    return print_fn_inner


def main():
    result = print_fn("Hello")
    result()


if __name__ == '__main__':
    main()

