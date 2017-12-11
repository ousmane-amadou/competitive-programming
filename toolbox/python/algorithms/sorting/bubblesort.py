from typing import List
""" Bubble Sort
* Also refferred to as sinking sort.
* Worst case occurs when array is reverse sorted. (O(n^2))
"""

def swap(lst: List[object], index1:int, index2:int) -> None:
    """ Swap items <index1> and <index2> in the List <lst>.
    """
    temp = lst[index1]
    lst[index1] = lst[index2]
    lst[index2] = temp

def sort(lst: List[object]) -> None:
    """
    >>> a = [1, 5, 6, 2, 1, 2]
    >>> sort(a)
    >>> print(a)
    [1, 1, 2, 2, 5, 6]

    >>> a = [1, 1, 1, 1, 1, 1]
    >>> sort(a)
    >>> print(a)
    [1, 1, 1, 1, 1, 1]

    >>> a = [9, 8, 7, 6, 5, 4]
    >>> sort(a)
    >>> print(a)
    [4, 5, 6, 7, 8, 9]
    """
    for i in range(len(lst) - 1):
        for j in range(len(lst) - 1, 0, -1):
            if lst[j] < lst[j-1]:
                swap(lst, j, j-1)
