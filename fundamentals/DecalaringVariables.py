# a variable can be assigned/reassigned any value type
print(50 * "-")
a = 10
print("a (int type): " + str(a))

a = 10.00
print("a (float type): " + str(a))

a = "shashi"
print("a (string type): " + a)

print(50 * "-")
# variable concatenation requires to define string type
b = 23

print("string concatenation: " + a + str(b))

print(50 * "-")


# global and local variables
def function():
    print("Example to declare global and local variables:")
    global a
    print("global variable a: " + a)
    a = "changed a"
    b = 45;
    print("Value of b inside function call: " + str(b))


function()

print("Value of b after function call: " + str(b))
print("global variable a after function call: " + a)
print(50 * "-")

# delete variables
del a
del b
print("variables deleted")
print(50 * "-")
