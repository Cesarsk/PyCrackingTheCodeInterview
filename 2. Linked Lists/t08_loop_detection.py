from linked_list import LinkedList


def loop_detection(ll):
    fast = slow = ll.head

    # advance both, the pointers (if there's a loop) will meet inside the loop
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast is slow:
            break

    # means linked list has no loop
    if fast is None or fast.next is None:
        return None

    # the two pointers proceed together, leave fast at meeting point, slow starts from zero
    slow = ll.head
    while fast is not slow:
        fast = fast.next
        slow = slow.next

    return fast  # is the start of the loop


def test_loop_detection():
    looped_list = LinkedList(["A", "B", "C", "D", "E"])
    loop_start_node = looped_list.head.next.next
    looped_list.tail.next = loop_start_node
    tests = [
        (LinkedList(), None),
        ((LinkedList((1, 2, 3))), None),
        (looped_list, loop_start_node),
    ]

    for ll, expected in tests:
        assert loop_detection(ll) == expected
