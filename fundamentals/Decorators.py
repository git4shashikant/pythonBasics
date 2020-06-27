import time


def f1(f):
    def f2():
        print("Before func call.")
        f()
        print("After func call.")

    return f2


def f3():
    print("f3 func call.")


f3 = f1(f3)
f3()
print("------------------------------------------")


# This is decorator annotation doing same thing as above
@f1
def f4():
    print("f4 func call.")


f4()


# Example, use @elapsed_time annotation to print the time required to run the function
def elapsed_time(f):
    def wrapper():
        t1 = time.time()
        f()
        t2 = time.time()
        print(f'Elapsed time: {t2-t1} secs')
    return wrapper()



