# Collective Reliability Demo - 5
import time
import random


# Create a random set of individual reliabilities
def make_set(num_elements: int):
    element_set = []
    random.seed(0)
    for a in range(num_elements):
        element_set.append(round(random.random(), 2))
    return element_set


# Collective Reliability - Lattice Weave (focused)
def coll_rel(element_set, target: int):
    if target == 0:  # Zero target rule
        return 1.0
    size_of_set = len(element_set)
    if target > size_of_set:  # High target rule
        return 0.0
    if target == size_of_set:  # Equal target rule
        total = 1.0
        for value in element_set:
            total = total * value
        return total
    failures = []
    for value in element_set:
        failures.append(1.0 - value)
    if target == 1:  # One target rule
        total = 1.0
        for value in failures:
            total = total * value
        return 1.0 - total
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
    slack = size_of_set - target
    while element_index <= size_of_set:
        low_target = max(1, element_index - slack)
        high_target = min(target, element_index)
        for index in range(low_target, high_target + 1):
            workspace[dst][index] = round(element_set[element_index] * workspace[src][index - 1] \
                                          + failures[element_index] * workspace[src][index], 3)
        src = 1 - src
        dst = 1 - dst
        element_index = element_index + 1
    return workspace[src][target]


# Main test loop
for size in range(100, 5001, 100):
    elements = make_set(size)
    start_time = time.time()
    result = coll_rel(elements, size // 2)
    complete_time = time.time() - start_time
    print("Size = {}, Time = {:.2f}".format(size, complete_time))
