# Collective Reliability Demo - 6
import time
import random


# Create a random set of individual reliabilities
def make_set(num_elements: int):
    element_set = []
    random.seed(0)
    for a in range(num_elements):
        element_set.append(round(random.random(), 2))
    return element_set


# Collective Reliability - Lattice weave (spectrum)
def coll_rel(element_set):
    size_of_set = len(element_set)
    failures = []
    for value in element_set:
        failures.append(1.0 - value)
    workspace = [[0 for i in range(size_of_set + 1)] for j in range(2)]
    workspace[0][0] = 1.0
    workspace[1][0] = 1.0
    src = 0
    dst = 1
    element_set.insert(0, 0)  # Just to set elements & failures to 1-base indexing
    failures.insert(0, 0)
    workspace[src][1] = round(1.0 - (failures[1] * failures[2]), 3)
    workspace[src][2] = round(element_set[1] * element_set[2], 3)
    element_index = 3
    while element_index <= size_of_set:
        low_target = 1
        high_target = element_index
        for index in range(low_target, high_target + 1):
            workspace[dst][index] = round(element_set[element_index] * workspace[src][index - 1] \
                                          + failures[element_index] * workspace[src][index], 3)
        src = 1 - src
        dst = 1 - dst
        element_index = element_index + 1
    return workspace[src]


# Main test loop
# for size in range(100, 5001, 100):
#    elements = make_set(size)
#    start_time = time.time()
#    result = coll_rel(elements)
#    complete_time = time.time() - start_time
#    print("Size = {}, Time = {:.2f}".format(size, complete_time))

elements = [.9, .6, .25, .77, .55, .12, .84]
print(coll_rel(elements))
