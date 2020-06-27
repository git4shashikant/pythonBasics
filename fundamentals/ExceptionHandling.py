try:
    print("try")
    raise ZeroDivisionError("custom message")
except ZeroDivisionError as e:
    print("Oops! Exception: ", e.__class__, "occurred.", e.args)
except Exception as ex:
    print("Exception: ", ex.__class__)
finally:
    print("finally")

print(50 * "-")

try:
    list1 = [4, 6, 8, 9, 2]
    print(list1[5])
except IndexError as ex:
    print("Exception: ", ex.__class__)
print(50 * "-")
