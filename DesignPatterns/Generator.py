def count():
    i = 0
    print(i)
    yield i
    i = i + 1
    print(i)
    yield i
    i = i + 1
    print(i)
    yield i


def main():
    count_fn = count()
    print("count function start")
    next(count_fn)
    next(count_fn)
    next(count_fn)
    print("count function end")
    range_list = range(6)
    # generator expression
    range_generator_fn = (x + 10 for x in range_list)
    # if not using for loop then elements are yield one by one on next() call
    for c in range_generator_fn:
        print(c)


if __name__ == '__main__':
    main()
