# bubble sort algorithm.

def bubble_sort(arr):
    n = len(arr)
    swapped = False
    for i in range(n - 1):
        for j in range(0, n - i - 1):

            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

        if not swapped:
            return


# ---------------------------------------------------------------------------
# merge sort algorithm.

def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    l_arr = [0 for i in range(n1)]
    r_arr = [0 for i in range(n2)]

    for i in range(0, n1):
        l_arr[i] = arr[l + i]

    for j in range(0, n2):
        r_arr[j] = arr[m + 1 + j]

    i = j = 0
    k = l

    while i < n1 and j < n2:
        if l_arr[i] <= r_arr[j]:
            arr[k] = l_arr[i]
            i += 1
        else:
            arr[k] = r_arr[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = l_arr[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = r_arr[j]
        j += 1
        k += 1


def merge_sort(arr, l, r):
    if l < r:
        m = l + (r - l) // 2
        merge_sort(arr, l, m)
        merge_sort(arr, m + 1, r)
        merge(arr, l, m, r)


# ---------------------------------------------------------------------------
# quicksort algorithm.

def partition(array, low, high):
    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])

    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1


def quick_sort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quick_sort(array, low, pi - 1)
        quick_sort(array, pi + 1, high)


