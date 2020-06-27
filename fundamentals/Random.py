import random

# generating index ranging from 1 to 10
print("generating index ranging from 1 to 10")
print(50 * "-")
for i in range(0, 9):
    print(str(round(1 + random.uniform(0, 1) * (10 - 1))), end = ", ")
print()
print()

# rounding up tp 2 decimals
print("rounding up tp 2 decimals")
print(50 * "-")
for i in range(0, 9):
    print(str(round(1 + random.uniform(0, 1) * (10 - 1), 2)), end= ", ")
print()
print(50 * "-")
