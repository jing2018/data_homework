import random
import time

from q1_method_1 import find_smallest_difference_v1
from q1_method_2 import find_smallest_difference


def main():
    '''
    Example output
    ------------------ Method 1 ------------------
    Downloaded the tutorial in 0.1064 seconds
    element_a: 295163, element_b: 295157, diff: 6
    ------------------ Method 2 ------------------
    Downloaded the tutorial in 0.0009 seconds
    element_a: 295163, element_b: 295157, diff: 6

    :return:
    '''

    random .seed()
    a = random.sample(range(1, 10000000), 1000)
    b = random.sample(range(1, 10000000), 1000)
    print("------------------ Method 1 ------------------")
    start = time.perf_counter()
    element_a, element_b, diff = find_smallest_difference_v1(a, b)
    stop = time.perf_counter()
    print(f"Downloaded the tutorial in {stop - start:0.4f} seconds")
    print(f"element_a: {element_a}, element_b: {element_b}, diff: {diff}")

    print("------------------ Method 2 ------------------")
    start = time.perf_counter()
    element_a, element_b, diff = find_smallest_difference(a, b)
    stop = time.perf_counter()
    print(f"Downloaded the tutorial in {stop - start:0.4f} seconds")
    print(f"element_a: {element_a}, element_b: {element_b}, diff: {diff}")


if __name__ == '__main__':
    main()
