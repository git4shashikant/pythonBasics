import random
import timeit

print("The time taken to run stmt: ", timeit.timeit(stmt='a=10;b=10;sum=a+b'))

import_module = "import random"
test_code = ''' 
def test(): 
    return random.randint(10, 100)
'''
print("Time taken to run method test(): ", timeit.timeit(stmt=test_code, setup=import_module))


def test():
    return random.randint(10, 100)


start_time = timeit.default_timer()
print("The start time is :", start_time)
test()
print("The time difference is :", timeit.default_timer() - start_time)


test_code = ''' 
def test(): 
    return random.randint(10, 100)
'''
print("Time taken in each repeat: ", timeit.repeat(stmt=test_code, setup=import_module, repeat=5))
