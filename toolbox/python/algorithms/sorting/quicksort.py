from random import randrange
from typing import List

""" Quicksort
====== Description =====
[Divide] 
Partition (rearrange) the array A[p....r]  into two (possibly empty) subarrays 
A[p....q-1] and A[q+1....r] such that each element of A[p....q-1] is less than or equal 
to A[q], which is, in turn, less than or equal to each element of A[q+1....r]. 
Compute the index q as part of this partitioning procedure.

[Conquer]
Sort the two sub arrays A[p...q-1] and A[q+1...r] by recursive calls to quicksort.

[Combine]
Because the sub arrays are already sorted, no work is needed to combine them: the entire 
array A[p...r]   is now sorted.

[Reference(s)] 
Introduction to Algorithms, Cormen, Leiserson, Rivest, Stein

[1, 2, 3, 4, 5, 6, 7]
"""

def swap(lst: List[object], index1:int, index2:int) -> None:
    """ Swap items <index1> and <index2> in the List <lst>.
    """
    temp = lst[index1]
    lst[index1] = lst[index2]
    lst[index2] = temp

def partition(lst:List[object], pivot:int, p:int, q:int) -> int:
    """ Partition the subarray lst[p:q] as described in the module
    docstring under the [Divide] header.
    """
    swap(lst, p, pivot)
    pivot_index = p
    for i in range(p, q):
        if lst[i] < lst[q]:
            swap(lst, i, pivot_index)
            pivot_index += 1
    swap(lst, pivot_index, q)

    return pivot_index

def sort(lst:List[object], p:int, q:int) -> None:
    """
    >>> a = [1, 5, 6, 2, 1, 2]
    >>> sort(a, 0, len(a)-1)
    >>> print(a)
    [1, 1, 2, 2, 5, 6]

    >>> a = [1, 1, 1, 1, 1, 1]
    >>> sort(a, 0, len(a)-1)
    >>> print(a)
    [1, 1, 1, 1, 1, 1]

    >>> a = [9, 8, 7, 6, 5, 4]
    >>> sort(a, 0, len(a)-1)
    >>> print(a)
    [4, 5, 6, 7, 8, 9]
    """
    if p >= q:
        return

    pivot = randrange(p, q+1)  # Choose a random pivot within lst[p:q]
    pivot_index = partition(lst, pivot, p, q)  # Partition

    # Recursively Sort the partioned subarrays
    sort(lst, p, pivot_index-1)
    sort(lst, pivot_index+1, q)
