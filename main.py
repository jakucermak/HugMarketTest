import os
from typing import List
import argparse

CLI=argparse.ArgumentParser()
CLI.add_argument("--list", nargs="*", default=[-1, 1, 3], help="pass list to program like: --list -1 1 3 ", type=int)

def solution_slow(a: List[int]) -> int:
    sorted_copy = list(sorted(a))
    # Validation of an inpout list
    if sorted_copy[0] < -100_000:
        raise Exception("Input number is lower than the -100 000")
    if sorted_copy[-1] > 100_000:
        raise Exception("Input number is higher than the 100 000")

    pos_sorted = list(filter(lambda i: (i > 0), sorted_copy))
    result: int = None

    i = 1

    while True:
        if i not in pos_sorted:
            return i
        i += 1


def solution_fast(a: List[int]) -> int:
    """
    Finds the smallest positive integer that does not appear in the list. The function is optimized
    by using a dictionary to store positive integers from the input list, which allows for constant-time
    lookup. This is significantly faster than a linear search in a list, especially for
    large datasets, because searching in a dictionary does not require iterating over all elements like in a list.

    :param a: List of integers within the range -100_000 and 100_000
    :return: int: An integer representing the missing number in the list
    :raise: Exception: If the input contains numbers outside the allowed range (-100_000 to 100_000).

    """

    sorted_copy = list(sorted(a))
    # Validation of input list
    if sorted_copy[0] < -100_000:
        raise Exception("Input number is lower than the -100 000")
    if sorted_copy[-1] > 100_000:
        raise Exception("Input number is higher than the 100 000")

    pos_sorted = {val: key for key, val in enumerate(sorted_copy) if val > 0}

    i = 1

    while True:
        if i not in pos_sorted:
            return i
        i += 1


if __name__ == '__main__':
    try:
        args = CLI.parse_args()
        res = solution_slow(args.list)
        print(res)
    except SystemExit as e:
        print(str(e))
        exit(1)

