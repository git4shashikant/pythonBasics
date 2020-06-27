import queue
import random
from heapq import heapify, heappush, heappop

# stack example
print("stack put:")
lifoStack = queue.LifoQueue()
for index in range(0, 9):
    print(index, end=", ")
    lifoStack.put_nowait(index)
print()

print("stack get:")
while not lifoStack.empty():
    print(lifoStack.get_nowait(), end = ", ")
print()

# queue example
print("simple queue put:")
simpleQ = queue.SimpleQueue()
for index in range(0, 9):
    print(index, end = ", ")
    simpleQ.put_nowait(index)
print()

print("simple queue get:")
while not simpleQ.empty():
    print(simpleQ.get_nowait(), end = ", ")
print()

# priority queue (max heap)
priorityQ = queue.PriorityQueue()
print("priority queue (min heap) put:")
for index in range(0, 9):
    num = round(1 + random.uniform(0, 9) * (9 - 0))
    print(num, end=", ")
    priorityQ.put_nowait(num)
print()

print("priority queue (min heap) get:")
while not priorityQ.empty():
    print(priorityQ.get_nowait(), end = ", ")
print()


# min heap using heapq
heapQ = []
heapify(heapQ)

print("min heap put:")
for index in range(0, 9):
    num = round(1 + random.uniform(0, 9) * (9 - 0))
    print(num, end=", ")
    heappush(heapQ, num)
print()

print("min heap get:")
while heapQ:
    print(str(heappop(heapQ)), end = ", ")
print()

# max heap
heapQ = []
heapify(heapQ)

print("max heap put:")
for index in range(0, 9):
    num = round(1 + random.uniform(0, 9) * (9 - 0))
    print(num, end=", ")
    heappush(heapQ, -1 * num)
print()

print("max heap get:")
while heapQ:
    print(str(heappop(heapQ) * -1), end = ", ")
print()
