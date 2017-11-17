# My implementation of a Stack
class stk:
    def __init__(self):
        self.top = -1
        self.items = []

    def push(i):
        """ (Object) -> None
            Add item to the top of the stack.
        """
        self.top += 1
        self.items.append(i)

    def pop(i):
        """ (Object) -> Object
             Return and remove the top element in a stack.
        """
        self.top -= 1
        rmvd = self.items.pop()
        return rmvd
