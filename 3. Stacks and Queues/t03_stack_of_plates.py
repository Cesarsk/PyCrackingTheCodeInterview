from stack import Stack


class SetOfStacks:
    def __init__(self, threshold):
        self.threshold = threshold
        self.stacks = [Stack()]

    def push(self, value):
        if len(self.stacks):
            if len(self.stacks[-1]) < self.threshold:
                self.stacks[-1].push(value)
            else:
                new_stack = Stack()
                self.stacks.append(new_stack)
                new_stack.push(value)
        else:
            raise Exception("error")

    def pop(self):
        if len(self.stacks):
            value = self.stacks[-1].pop()
            if len(self.stacks[-1]) == 0:
                self.stacks.pop(-1)
            return value
        else:
            raise Exception("error")

    def print(self):
        print(self.stacks)


if __name__ == '__main__':
    ss = SetOfStacks(3)
    ss.push(5)
    ss.print()
    ss.push(5)
    ss.print()
    ss.push(5)
    ss.print()
    ss.push(5)
    ss.print()
    ss.push(5)
    ss.print()
    ss.push(5)
    ss.print()
    ss.push(5)
    ss.print()
    ss.push(5)
    ss.print()
    ss.pop()
    ss.print()
    ss.pop()
    ss.print()
    ss.pop()
    ss.print()
    ss.pop()
    ss.print()
    ss.pop()
    ss.print()
    ss.pop()
    ss.print()
    ss.pop()
    ss.print()
    ss.pop()
    ss.print()

