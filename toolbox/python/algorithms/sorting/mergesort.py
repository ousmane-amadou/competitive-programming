""" MergeSort
* Merge sort can be slower than bubble and insertion sort for
smaller input sizes
"""

from typing import List


def swap(lst: List[object], index1: int, index2: int) -> None:
    """ Swap items <index1> and <index2> in the List <lst>.
    """
    temp = lst[index1]
    lst[index1] = lst[index2]
    lst[index2] = temp


def merge(lst: List[object], start: int, mid: int, end: int) -> None:
    """ merges A[start:mid] and A[mid:end] into a new A[start:end]. (That
    is sorted)

    >>> a = [1, 3, 5, 2, 6, 8]
    >>> merge(a, 0, 3, 6)
    >>> print(a)
    [1, 2, 3, 5, 6, 8]

    >>> a = [1, 3, 9, 2, 6, 8]
    >>> merge(a, 0, 3, 6)
    >>> print(a)
    [1, 2, 3, 6, 8, 9]
    """
    temp = []

    i = start
    j = mid

    while i < mid and j < end:
        if lst[i] <= lst[j]:
            temp.append(lst[i])
            i += 1
        else:
            temp.append(lst[j])
            j += 1

    temp.extend(lst[i:mid])       # adds any remaining elements
    temp.extend(lst[j:end])       # adds any remaining elements

    for i in range(len(temp)):
        lst[start + i] = temp[i]


def sort(lst: List[object], start: int, end: int) -> None:
    """ Sorts lst[start:end]
    """
    if (start - end) <= 1:
        return
    else:
        mid = (start+end) // 2
        sort(lst, start, mid)
        sort(lst, mid, end)
        merge(lst, start, mid, end)
