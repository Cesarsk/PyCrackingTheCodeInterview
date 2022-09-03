from stack import Stack


class MinStack(Stack):
    def __init__(self):
        super(MinStack, self).__init__()
        self.minvals = Stack()  # stack of min values

    def push(self, value):
        super().push(value)
        if not self.minvals or value <= self.min():
            self.minvals.push(value)  # push the min if it's a new min

    def pop(self):
        value = super().pop()
        if value == self.min():
            self.minvals.pop()
        return value

    def min(self):
        return self.minvals.peek()

def test_min_stack():
    newstack = MinStack()
    assert newstack.min() is None

    newstack.push(5)
    assert newstack.min() == 5

    newstack.push(6)
    assert newstack.min() == 5

    newstack.push(3)
    assert newstack.min() == 3

    newstack.push(7)
    assert newstack.min() == 3

    newstack.push(3)
    assert newstack.min() == 3

    newstack.pop()
    assert newstack.min() == 3

    newstack.pop()
    assert newstack.min() == 3

    newstack.pop()
    assert newstack.min() == 5

    newstack.push(1)
    assert newstack.min() == 1


if __name__ == "__main__":
    test_min_stack()
