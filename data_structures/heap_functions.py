import math


def parent(A, i):
    return A[math.floor(i/2)]


def right(A, i):
    return A[2*i]


def left(A, i):
    return A[2*i + 1]


def max_heapify(A, i):
    l = left(A, i)
    r = right(A, i)

    if A[l] > A[i]:
        largest = l
    else:
        largest = i

    if A[r] > A[largest]:
        largest = r

    if not largest == i:
        temp = A[i]
        A[i] = A[largest]
        A[largest] = A[temp]
        max_heapify(A, largest)
