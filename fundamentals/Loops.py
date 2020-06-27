def while_usage(n):
    x = 0
    while x < n:
        print(x, end=', ')
        x += 1


def for_usage(n):
    for x in range(0, n):
        print(x, end=', ')


# use a for loop over a collection
def for_collection(months):
    for month in months:
        print(month)


def for_enum(months):
    for i, month in enumerate(months):
        print(i, month)


while_usage(10)
print("")
for_usage(10)
print("")
months_test = ["Jan", "Feb", "Mar", "April", "May", "June"]
for_collection(months_test)
for_enum(months_test)
