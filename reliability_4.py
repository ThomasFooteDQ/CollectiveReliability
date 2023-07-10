# Collective Reliability Demo - 4
import time
from random import random


# Create a random set of individual reliabilities
def make_set(num_elements: int):
    element_set = []
    for a in range(num_elements):
        element_set.append(random())
    return element_set


# Collective Reliability - Recursive with 5 rules + MEMOIZATION
def coll_rel(element_set, target: int, memory):
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
    if target == 1:  # One target rule
        total = 1.0
        for value in element_set:
            total = total * (1.0 - value)
        return 1.0 - total
    # Check memory
    problem = (size_of_set, target)
    if problem in memory:
        return memory.get(problem)
    # Simplification rule
    elements_copy = element_set.copy()
    value = elements_copy[0]
    elements_copy.pop(0)
    reliability: float = value * coll_rel(elements_copy, target - 1, memory) \
                         + (1.0 - value) * coll_rel(elements_copy, target, memory)
    memory[problem] = reliability
    return reliability


# Main test loop
for size in range(100, 5001, 100):
    elements = make_set(size)
    start_time = time.time()
    result = coll_rel(elements, size // 2, {})
    complete_time = time.time() - start_time
    print("Size = {}, Time = {:.2f}".format(size, complete_time))

print("The program has finished!")

