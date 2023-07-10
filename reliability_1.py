# Collective Reliability Demo - 1
import time
from random import random


# Create a random set of individual reliabilities
def make_set(num_elements: int):
    element_set = []
    for a in range(num_elements):
        element_set.append(random())
    return element_set


# Collective Reliability - Four steps method
def coll_rel(element_set, target: int):
    size_of_set = len(element_set)
    num_outcomes = 2 ** size_of_set
    collective_reliability = 0.0
    for outcome in range(num_outcomes):
        outcome_binary = bin(outcome)[2:].zfill(size_of_set)
        this_outcome = []
        count_success = 0
        for bit_index in range(0, size_of_set):
            bit = outcome_binary[bit_index: bit_index + 1]
            if bit == '0':
                this_outcome.append(element_set[bit_index])
                count_success = count_success + 1
            else:
                this_outcome.append(1.0 - element_set[bit_index])
        if count_success >= target:
            outcome_reliability = 1.0
            for index in range(0, size_of_set):
                outcome_reliability = outcome_reliability * this_outcome[index]
            collective_reliability = collective_reliability + outcome_reliability
    return collective_reliability


# Main test loop
for size in range(1, 51):
    elements = make_set(size)
    start_time = time.time()
    result = coll_rel(elements, size // 2)
    complete_time = time.time() - start_time
    print("Size = {}, Time = {:.2f}".format(size, complete_time))
