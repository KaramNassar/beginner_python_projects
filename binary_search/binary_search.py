import random
import time


def binarySearch(needle: int, haystack: list[int]) -> int:
    if list(haystack) != sorted(haystack):
        raise ValueError("Haystack must be sorted in an ascending order")

    left, right = 0, len(haystack) - 1

    while left <= right:
        middle = (left + right) >> 1

        if haystack[middle] == needle:
            return middle

        if haystack[middle] > needle:
            right = middle - 1

        else:
            left = middle + 1

    return -1


if __name__ == "__main__":
    length = 10_000
    sorted_list = set()

    while len(sorted_list) < length:
        sorted_list.add(random.randint(-30_000, 30_000))

    sorted_list = sorted(sorted_list)

    start = time.time()
    for target in sorted_list:
        binarySearch(target, sorted_list)

    end = time.time()
    print("Binary Search time: ", end - start, " seconds.")
