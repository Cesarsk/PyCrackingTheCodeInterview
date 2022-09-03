from stack import Stack


class SortedStack(Stack):
    def __init__(self):
        super(SortedStack, self).__init__()
        self.temp_stack = Stack()

    def push(self, item):
        if self.is_empty() or item < self.peek():
            super().push(item)
        else:
            # reverse the stack
            while self.peek() is not None and item > self.peek():
                self.temp_stack.push(self.pop())
            # push the item in the stack
            super().push(item)

            # reverse the stack again
            while not self.temp_stack.is_empty():
                super().push(self.temp_stack.pop())
