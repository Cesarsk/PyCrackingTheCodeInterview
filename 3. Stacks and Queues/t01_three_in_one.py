class TripleStackFixedSize:
    def __init__(self, stack_size):
        self.number_of_stacks = 3
        self.array = [0] * (stack_size * self.number_of_stacks)
        self.sizes = [0] * self.number_of_stacks
        self.stack_size = stack_size

    def index_of_top(self, stack_num):
        return stack_num * self.stack_size + self.sizes[stack_num] - 1

    def push(self, value, stack_num):
        if self.is_full(stack_num):
            raise Exception(f"Push failed because stack {stack_num} is full")
        self.sizes[stack_num] += 1
        self.array[self.index_of_top(stack_num)] = value

    def pop(self, stack_num):
        if self.is_empty(stack_num):
            raise Exception(f"Push failed because stack {stack_num} is empty")
        self.sizes[stack_num] -= 1
        value = self.array[self.index_of_top(stack_num)]
        self.array[self.index_of_top(stack_num)] = 0
        return value

    def peek(self, stack_num):
        return self.array[self.index_of_top(stack_num)]

    def is_full(self, stack_num):
        return self.sizes[stack_num] == self.stack_size

    def is_empty(self, stack_num):
        return self.sizes[stack_num] == 0

if __name__ == "__main__":
    newstack = TripleStackFixedSize(3)
    print(newstack.is_empty(1))
    newstack.push(3, 1)
    print(newstack.is_empty(1))
    newstack.push(2, 1)
    print(newstack.pop(1))
    newstack.push(3, 1)
