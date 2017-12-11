from typing import List

""" MergeSort
* Merge sort can be slower than bubble and insertion sort for
smaller input sizes 
"""

def swap(lst: List[object], index1:int, index2:int) -> None:
    """ Swap items <index1> and <index2> in the List <lst>.
    """
    temp = lst[index1]
    lst[index1] = lst[index2]
    lst[index2] = temp

def merge(lst: List[object], p:int, q:int, r:int) -> None:
    """
    precondition: p < q < r
    """


def sort(lst: List[object], p:int, r:int) -> None:
    """"""
    if p < r:
        q = (p+r) // 2

        sort(lst, p, q)
        sort(lst, q+1, r)
        merge(lst, p, q, r)

