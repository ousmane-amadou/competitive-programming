# My implementation of a Queue
class queue:
    def __init__(self):
        self.items = []

    def enqueue(i):
        """ (Object) -> None
            Add item to the top of the stack.
        """
        self.items.append(i)

    def dequeue(i):
        """ (Object) -> Object
             Return and remove the top element in a stack.
        """
        rmvd = self.items.pop(0)
        return rmvd
