# the first simple variant, but the printing is bad...

import math
import random
import time

_default_compare = lambda x, y: x - y
_default_key = lambda a: a

def is_sorted(lst, compare=_default_compare, key=_default_key, ascending=False):
    for i in range(len(lst) - 1):
        if 0 < compare(key(lst[i]), key(lst[i + 1])) * (-1 if ascending else 1):
            return False
    return True

def bubble_sort(lst, compare=_default_compare, key=_default_key, ascending=False):
    n = len(lst)
    for i in range(n):
        for j in range(0, n - i - 1):
            if compare(key(lst[j]), key(lst[j + 1])) > 0:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

def selection_sort(lst, compare=_default_compare, key=_default_key, ascending=False):
    n = len(lst)
    for i in range(n):
        max_idx = 0
        for j in range(1, n - i):
            if compare(key(lst[j]), key(lst[max_idx])) > 0:
                max_idx = j
        if max_idx != n - i - 1:
            lst[max_idx], lst[n - i - 1] = lst[n - i - 1], lst[max_idx]

def insert_sort(lst, compare=_default_compare, key=_default_key, ascending=False):
    for i in range(1, len(lst)):
        j = i - 1
        tmp = lst[i]
        while j >= 0 and compare(key(lst[j]), tmp) > 0:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = tmp

def quick_sort(lst, compare=_default_compare, key=_default_key, ascending=False):
    if len(lst) <= 1:
        return lst
    pivot = lst[len(lst) // 2]
    left = [x for x in lst if compare(key(x), key(pivot)) < 0]
    middle = [x for x in lst if compare(key(x), key(pivot)) == 0]
    right = [x for x in lst if compare(key(x), key(pivot)) > 0]
    return quick_sort(left) + middle + quick_sort(right)

def merge_sort(lst, compare=_default_compare, key=_default_key, ascending=False):
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def heap_sort(lst, compare=_default_compare, key=_default_key, ascending=False):
    n = len(lst)

    def drain(i, l, r):
        nonlocal lst
        nonlocal compare
        nonlocal key

        drain_need = True
        tmp = lst[i]

        while 2 * (i - l) + 1 + l <= r:
            j = 2 * (i - l) + 1 + l
            if j + 1 <= r and compare(key(lst[j]), key(lst[j + 1])) < 0:
                j += 1
            if compare(tmp, key(lst[j])) < 0:
                lst[i] = lst[j]
                i = j
            else:
                lst[i] = tmp
                i = r
                drain_need = False

        if drain_need:
            lst[i] = tmp

    for i in range(n // 2 - 1, -1, -1):
        drain(i, 0, n - 1)

    for i in range(n - 1, 0, -1):
        lst[0], lst[i] = lst[i], lst[0]
        drain(0, 0, i - 1)

def run_sort_algorithm(algorithm, lst):
    # Clone the list before sorting to keep the original intact
    original_lst = lst.copy()

    # Measure the time taken to sort the list
    start_time = time.time()
    algorithm(lst)
    elapsed_time = time.time() - start_time

    # Check if the list is sorted and print the result
    result = "Sorted" if is_sorted(lst) else "Not Sorted"
    print(f"{algorithm.__name__} - {result} in {elapsed_time:.5f} seconds")


def main():
    # Specify the range of elements to test
    start_e = 2
    max_e = 16

    for e in range(start_e, max_e + 1):
        # Create a list with 2^e elements and shuffle it
        lst = list(range(2**e))
        random.shuffle(lst)

        # Run each sorting algorithm and measure the time
        run_sort_algorithm(bubble_sort, lst.copy())
        run_sort_algorithm(selection_sort, lst.copy())
        run_sort_algorithm(insert_sort, lst.copy())
        run_sort_algorithm(quick_sort, lst.copy())
        run_sort_algorithm(merge_sort, lst.copy())
        run_sort_algorithm(heap_sort, lst.copy())

if __name__ == "__main__":
    main()

