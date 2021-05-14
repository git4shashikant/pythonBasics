import time


def wrapperFunction(func):
    def wrapper():
        print("Before testFunction() call.")
        func()
        print("After testFunction() call.")

    return wrapper


# Example, use @elapsed_time annotation to print the time required to run the function
def elapsed_time(f):
    def wrapper():
        t1 = time.time()
        print(f"Time before warpAnnotatedFunction() call: {t1}")
        f()
        t2 = time.time()
        print(f"Time after warpAnnotatedFunction() call: {t2}")
        print(f'Elapsed time: {t2-t1} secs')
    return wrapper()


def testFunction():
    print("testFunction called.")


test = wrapperFunction(testFunction)
test()
print("------------------------------------------")


# This is decorator annotation doing same thing as above
@elapsed_time
@wrapperFunction
def warpAnnotatedFunction():
    time.sleep(2)
    print("warpAnnotatedFunction called.")


warpAnnotatedFunction






