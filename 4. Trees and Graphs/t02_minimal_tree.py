class Node:
    def __init__(self, item):
        self.left = None
        self.right = None
        self.val = item


def array_to_binary_tree(array, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    root = Node(array[mid])
    root.left = array_to_binary_tree(array, start, mid - 1)
    root.right = array_to_binary_tree(array, mid + 1, end)
    return root


if __name__ == "__main__":
    test_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 18, 22, 43, 144, 515, 4123]
    print(array_to_binary_tree(test_array, 0, len(test_array) - 1))
