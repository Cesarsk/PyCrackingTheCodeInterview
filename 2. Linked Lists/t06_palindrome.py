from linked_list import LinkedList


def is_palindrome_stack(ll):
    fast = slow = ll.head
    stack = []

    while fast and fast.next:
        stack.append(slow.value)
        slow = slow.next
        fast = fast.next.next

    if fast:
        slow = slow.next  # in case of odd list

    while slow:
        if stack.pop() != slow.value:
            return False

        slow = slow.next

    return True


def is_palindrome_constant_space(ll):
    def reverse(node):
        prev = None
        while node:
            next = node.next
            node.next = prev
            prev = node
            node = next  # move pointer
        return prev

    # compare the first half of the normal list with the first half of the reversed list
    slow = ll.head

    if not slow or not slow.next:
        return True

    # find middle of the list via the fast pointer (runner) technique
    fast = slow.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # unlink left and right halves of the list
    right_head = slow.next
    slow.next_node = None

    # reverse the right half of the list
    tail = reverse(right_head)

    # iterate over nodes from the outside in
    left, right = ll.head, tail
    result = True

    while left and right:
        if left.value != right.value:
            result = False
            break

        left = left.next
        right = right.next

    reverse(tail)
    slow.next_node = right_head
    return result


def is_palindrome_recursive(ll):
    def get_len(node):
        if not node:
            return 0
        else:
            return 1 + get_len(node.next)

    def recursive_traverse(node, length):
        if not node or length == 0:  # even list
            return True, node
        elif length == 1:  # odd list
            return True, node.next

        _is_palindrome, fwd_node = recursive_traverse(node.next, length - 2)

        if not _is_palindrome or not fwd_node:
            return False, None

        if node.value == fwd_node.value:
            return True, fwd_node.next
        else:
            return False, None

    return recursive_traverse(ll.head, get_len(ll.head))[0]
