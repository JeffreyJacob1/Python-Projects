from timeit import Timer
from random import choice


# bubble-sort algorithm
def bubbleSort(items):
    # i := [n - 1, n - 2, ..., 0]
    for i in range(len(items) - 1, 0, -1):
        # j := [0, 1, 2, ..., i - 1]
        for j in range(i):
            # check if items are out of order
            if items[j] > items[j + 1]:
                # swap when items are out of order
                items[j], items[j + 1] = items[j + 1], items[j]
            

# selection-sort algoirthm
def selectionSort(items):
    # i := [0, 1, 2, ..., n - 1]
    for i in range(len(items)):
        # stores the index of the minimum 
        # element in remaining items
        min_index = i
        # j := [i + 1, i + 2, ..., n - 1]
        for j in range(i + 1, len(items)):
            # check if jth element is smaller
            if items[j] < items[min_index]:
                min_index = j
        # swap the ith element with minimum
        items[i], items[min_index] = items[min_index], items[i]





# insertion-sort algorithm
def insertionSort(items):
    # i := [1, 2, 3..., n - 1]
    for i in range(1, len(items)):
        # element to be placed
        key = items[i]
        # find the position of the element
        j = i - 1
        while (j >= 0 and key < items[j]):
            items[j + 1] = items[j]
            j = j - 1
        # place key at its position
        items[j + 1] = key




list_ = list(range(0, 500))
# the sizes we have to test
sizes = [10, 20, 50, 100, 200, 500]
# algorithms we have
algorithms = ['bubbleSort', 'selectionSort', 'insertionSort']


# print the header
print("{:>5s}".format("Size"), end='')
for algorithm in algorithms:
    print("{:>15s}".format(algorithm), end='')
print()

# iterate through each size
for size in sizes:
    # create an items of given size
    data = [choice(list_) for i in range(size)]
    # print the size
    print("{:>5d}".format(size), end='')
    # test out all algorithms
    for algorithm in algorithms:
        # take a copy of the original items
        d = data.copy()
        # sort the items
        t1 = Timer(f"{algorithm}({d})", f"from __main__ import {algorithm}")
        print("{:>15f}".format(t1.timeit(number=1)), end='')
    # print the newline
    print()
