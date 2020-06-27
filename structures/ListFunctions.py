list_temp = [1, 2.0, 'python']
for var in list_temp:
    print(var)

list_ints = [1, 4, 6, 8, 9, 3]
print("initial list: ", list_ints)
# update
list_ints[0] = 2
print("after adding 2 at index 0: ", list_ints)

# update last element
list_ints[-1] = 1
print("after adding 1 to the last element: ", list_ints)

# add
list_ints.append(7)
print("after appending 7: ", list_ints)

print("Sum: " + str(sum(list_ints)))
print("Mean: " + str(round(sum(list_ints)/len(list_ints))))
print("Max: " + str(max(list_ints)))
print("Min: " + str(min(list_ints)))
print("Length: {}".format(len(list_ints)))
print("Sorted: {}".format(sorted(list_ints)))
print("Reversed: {}".format(reversed(list_ints)))


# delete
list_ints.pop(-1)
print("after removing last element: ", list_ints)
index = list_ints.index(4)
list_ints.remove(4)
print("after removing 4: {}", list_ints)
list_ints.insert(index, 4)
print("after inserting 4: {}", list_ints)
list_ints.__delitem__(1)
print("after del index 1", list_ints)

list_ints.sort()
print("After sort: ", list_ints)
list_ints.sort(reverse=True)
print("After reverse sort: ", list_ints)

# enumerate for range in list
for index, ele in enumerate(list_ints[3:5]):
    print("index: {} value: {}".format(index, list_ints[index]))

# comprehensions
square_list = [2 ** ele for ele in list_ints]
print("List of squares: ", square_list)

# returning tuples from list comprehension
square_tuples = [(ele, 2 ** ele) for ele in list_ints]
print("List of tuples of squares: ", square_tuples)

# returning tuples from list comprehension
square_dict = [{ele : 2 ** ele} for ele in list_ints]
print("List of dict of squares: ", square_dict)


def result(argument):
    return argument * 2


# map function on eah element
results = map(result, list_ints)
for result in results:
    print(result)

# abs function
print(abs(-10))
print(abs(-25.00))
print(abs(10 + 20j))
