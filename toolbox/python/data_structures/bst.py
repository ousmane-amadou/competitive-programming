"""

"""
class bst:
    def __init__(self, i):
        self.key = i
        self.p = None
        self.l = None
        self.r = None

    def insert(self, i):
        """ (bst, int) -> None
        Inserts an element with key i, into a binary search tree

        >>> a = bst(6)
        >>> a.insert(5)
        >>> a.insert(10)
        >>> a.l.key
        5
        >>> a.r.key
        10
        """
        if self.key < i:
            if self.r is None:
                self.r = bst(i)
            else:
                self.r.insert(i)

        if self.key >= i:
            if self.l is None:
                self.l = bst(i)
            else:
                self.l.insert(i)

    def minimum(self):
        if self.l is None:
            return self.key
        else:
            return self.l.minimum()

    def search(self, k):
        """ (bst, int) -> int
             Searches a binary search tree for key k. If key k in bst, return
             True. Retrun False Otherwise.

            >>> a = bst(6)
            >>> a.l = bst(3)
            >>> a.l.l = bst(2)
            >>> a.l.r = bst(4)
            >>> a.r = bst(8)
            >>> a.search(8)
            True

            >>> a = bst(6)
            >>> a.l = bst(3)
            >>> a.l.l = bst(2)
            >>> a.l.r = bst(4)
            >>> a.r = bst(8)
            >>> a.search(9)
            False

            >>> a = bst(6)
            >>> a.l = bst(3)
            >>> a.l.l = bst(2)
            >>> a.l.r = bst(4)
            >>> a.r = bst(8)
            >>> a.search(2)
            True
        """
        if self.key == k:
            return True

        if self.key < k:
            if self.r is not None:
                return self.r.search(k)
        else:
            if self.l is not None:
                return self.l.search(k)

        return False

    def getInOrder(self):
        """ (bst) -> Object[]
            Returns an array of the elements in this binary search tree
            (not including parent), in a sorted fasion.

            >>> a = bst(6)
            >>> a.l = bst(3)
            >>> a.l.l = bst(2)
            >>> a.l.r = bst(4)
            >>> a.r = bst(8)
            >>> a.getInOrder()
            [2, 3, 4, 6, 8]

            >>> a = bst(8)
            >>> a.insert(3)
            >>> a.insert(1)
            >>> a.insert(4)
            >>> a.insert(10)
            >>> a.insert(9)
            >>> a.getInOrder()
            [1, 3, 4, 8, 9, 10]
        """
        ordrp = []                              # Ordered Representation
        if self.key is not None:
            ordrp = []
            if self.l is not None:
                lrp = self.l.getInOrder()        # Left Arry Representation
                for k in lrp:
                    ordrp.append(k)

            ordrp.append(self.key)

            if self.r is not None:
                rrp = self.r.getInOrder()        # Right Array Representation
                for k in rrp:
                    ordrp.append(k)

        else:
            ordrp = None

        return ordrp

if __name__ == '__main__':
    import doctest
    doctest.testmod()
