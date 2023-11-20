# the linear search algorithm.
# Given an array of  elements, search a given element x in array.

def linear_search(arr, x):
    for i in range(len(arr)):

        if arr[i] == x:
            return i

    return -1


# -----------------------------------------------------------------
# the binary search algorithm.

def binary_search(arr, low, high, x):
    if high >= low:

        mid = (high + low) // 2

        if arr[mid] == x:
            return mid

        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)

        else:
            return binary_search(arr, mid + 1, high, x)

    else:
        return -1



