list1 = ['shashi', 'kant', 'sharma']
# tuple declaration
print(50 * '-')
tuple0 = ()
tuple1 = ('shashi', )
print('Declaring and printing tuple: ' + tuple1[0])

# tuple slicing
print(50 * '-')
tup1 = ('Robert', 'Carlos', '1965', 'Terminator 1995', 'Actor', 'Florida');
tup2 = (1, 2, 3, 4, 5, 6, 7)
print("first tuple element: " + tup1[0])
print("slicing tuple: " + str(tup2[1:4]))  # second argument is excluded

print(50 * '-')
# tuple packing/unpacking
x = ("nasdaq", 35, "Software Engineer")  # tuple packing
(company, age, profile) = x  # tuple unpacking
print("Company: %s, age: %d, profile: %s" % (company, age, profile))

print(50 * '-')
# comparing tuples: compare first then second elements and so on un till condition satisfy
# case 1
a = (5, 6)
b = (1, 4)
if a > b:
    print("a is bigger")
else:
    print("b is bigger")

# case 2
a = (5, 6)
b = (5, 4)
if a > b:
    print("a is bigger")
else:
    print("b is bigger")

# case 3
a = (5, 6)
b = (6, 4)
if a > b:
    print("a is bigger")
else:
    print("b is bigger")

# Tuples are immutable and cannot be deleted.
# You cannot delete or remove items from a tuple. But deleting tuple entirely is possible by using the keyword del
# Tuples and dictionary
# Dictionary can return the list of tuples by calling items, where each tuple is a key value pair
a = {'x': 100, 'y': 200}
b = a.items()
print(b)

for k, v in a.items():
    print("key: {}, value: {}".format(k, v))

for item in a.items():
    print("key: {}, value: {}".format(item[0], item[1]))

